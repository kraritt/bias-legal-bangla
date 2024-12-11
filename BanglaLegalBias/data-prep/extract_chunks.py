import pandas as pd 
import re 
import json
import random


N_SENTENCES_INTRO = 5
N_SENTENCES_END = 10  
N_SENTENCES_RANDOM = 3
N_CHUNKS = 32 

def bias_extractor(text, bias, n):
	bias  = [b.replace('“',"").replace('”', "") for b in bias]  
	sentences = re.split("[?!;.\s]+\s", text)
	sentences = [s.strip() for s in sentences] 
	bias_sentences = []
	for sent_idx, sentence in enumerate(sentences):
		for b in bias:
			if b in sentence:
				idx_start = max(0, sent_idx-n)
				idx_end = min(sent_idx+n, len(sentences))
				bias_sentences.append(" ".join([sent for sent in sentences[idx_start:idx_end]]))
	return bias_sentences


def intro_extractor(text, n):
	sentences = re.split("[;.\s]+\s", text)
	sentences = [s.strip() for s in sentences] 
	sent_idx = 0
	intro_sentences = []
	idx_start = sent_idx
	idx_end = min(sent_idx+n, len(sentences))
	intro_sentences.append(" ".join([sent for sent in sentences[idx_start:idx_end]]))
	return intro_sentences   


def end_extractor(text, n):
	sentences = re.split("[;.\s]+\s", text)
	sentences = [s.strip() for s in sentences] 
	sent_idx = len(sentences)
	end_sentences = []
	idx_start = max(0, sent_idx-n)
	idx_end = sent_idx
	end_sentences.append(" ".join([sent for sent in sentences[idx_start:idx_end]]))
	return end_sentences 


def random_extractor(text, n):
	sentences = re.split("[;.\s]+\s", text)
	sentences = [s.strip() for s in sentences] 
	sent_idx = random.randint(0, len(sentences)) 
	random_sentences = []
	idx_start = max(0, sent_idx-n)
	idx_end = min(sent_idx+n, len(sentences))
	random_sentences.append(" ".join([sent for sent in sentences[idx_start:idx_end]]))
	return random_sentences


def full_extractor(text):
	sentences = re.split("[;.\s]+\s", text)
	sentences = [s.strip() for s in sentences] 

	while(len(sentences) < N_CHUNKS):
		sentences.append(random.choice(sentences)) 

	if(len(sentences) == N_CHUNKS):
		return sentences
	else:
		chunk_size = len(sentences) // N_CHUNKS 

		chunks = []
		start = 0

		for i in range(N_CHUNKS):
			stop = start + chunk_size
			if(i==N_CHUNKS-1): 
				stop = len(sentences)
				chunks.append(' '.join(sentences[start:stop]))
			else:
				chunks.append(' '.join(sentences[start:stop]))

			start+=chunk_size

		return chunks 


df_annotation = pd.read_csv('annotate_filled.csv')
json_annotation = {}
n_bias = 0
n_unbias = 0

for idx, row in df_annotation.iterrows():
	json_annotation[row["name_file"]] = {
				 k:v for k,v in row.items() if k!='Unnamed: 0'}
			 
	json_annotation[row["name_file"]].update({
				 k:"" for k,v in json_annotation[row["name_file"]].items()
				  if type(v) is float })

	filename = row["name_file"] + ".txt"
	with open(filename) as f:
		text = f.read()

	if type(row["bias"]) is float:
		bias_chunks = []
		for n in [2, 3]:
			bias_chunks += random_extractor(text, n) 
		n_unbias += len(bias_chunks)
	else:
		bias_chunks = []
		for n in [1, 2, 3]:
			bias = row["bias"].split(";")
			bias_chunks += bias_extractor(text, bias, n)
		n_bias += len(bias_chunks)

	intro_chunks = intro_extractor(text, N_SENTENCES_INTRO)
	end_chunks = end_extractor(text, N_SENTENCES_END)
	random_chunks = []
	for i in range(10):
		random_chunks +=random_extractor(text, N_SENTENCES_RANDOM)
	all_chunks = full_extractor(text)

	json_annotation[row["name_file"]].update({
		k:v.replace(" ", "") for k,v in json_annotation[row["name_file"]].items() if type(v) is str and k!='bias'}) 

	json_annotation[row["name_file"]].update({"bias_context":bias_chunks})
	json_annotation[row["name_file"]].update({"intro":intro_chunks})
	json_annotation[row["name_file"]].update({"end":end_chunks})
	json_annotation[row["name_file"]].update({"random":random_chunks})
	json_annotation[row["name_file"]].update({"full":all_chunks})

	json_annotation[row["name_file"]].update({
		k:v.replace('“',"").replace('”', "") for k,v in json_annotation[row["name_file"]].items() if k=='bias'})

	json_annotation[row["name_file"]].update({
		k:v.split(";") for k,v in json_annotation[row["name_file"]].items() if type(v) is str and k!='name_file'})

print("# of biased chunks", n_bias)
print("# of unbiased chunks", n_unbias)

with open("annotate_filled.json", "w") as f:
	json.dump(json_annotation, f)