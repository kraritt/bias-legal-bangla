import numpy as np
import random
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

BN_STOPWORDS = stopwords.words('bengali')

BIAS_SYN_DICT_BN = {
    "আক্রমণ": ["অপমান"],
    "আক্রমণাত্মক": ["যুদ্ধসুলভ"],
    "আক্রমণাত্মকতা": ["বিরোধিতা"],
    "আক্রমণসমূহ": ["অপমানসমূহ"],
    "অত্যাচারী": ["কর্তক"],
    "চতুর": ["দুষ্ট"],
    "চতুরতা": ["দুর্বলতা"],
    "যুদ্ধপ্রবণতা": ["লড়াইপ্রবণতা"],
    "সুবিচার": ["মুল্যায়ন"],
    "চরিত্র": ["স্বভাব"],
    "আচরণ": ["মেজাজ"],
    "অবস্থা": ["পরিস্থিতি"],
    "নেতৃত্ব": ["কর্ম"],
    "গোথালো": ["অস্পষ্ট"],
    "উথলপাথল": ["বিশৃঙ্খল"],
    "পৌরাণীকরণ": ["উসকানো"],
    "আলোচনামূলক": ["প্ররোচনামূলক"],
    "প্ররোচনামূলকসমূহ": ["প্ররোচনামূলকসমূহ"],
    "অসামঞ্জস্যপূর্ণ": ["অবস্থানহীন"],
    "বিচ্ছিন্নতা": ["ঝগড়া"],
    "বিচ্ছিন্নতাসমূহ": ["ঝগড়াসমূহ"],
    "অপকারে": ["অসহায়"],
    "পথভ্রষ্টতা": ["ত্রুটি"],
    "বিকৃতি": ["দূষিত"],
    "উচিত": ["প্রয়োজন"],
    "স্বার্থপরতা": ["স্বকেন্দ্রিকতা"],
    "স্বার্থপর": ["স্বকেন্দ্রিক"],
    "স্থিতিশীলতা": ["দৃঢ়তা"],
    "অপরিচিত": ["অদ্ভুত"],
    "অপরিচিতসমূহ": ["অদ্ভুতসমূহ"],
    "স্পষ্টভাবে": ["স্পষ্টভাবে"],
    "বিস্ফোরণ": ["স্ফোটন"],
    "বিস্ফোরণসমূহ": ["স্ফোটনসমূহ"],
    "মিথ্যা": ["নকল"],
    "পরিবার": ["সম্প্রদায়"],
    "পরিচিত": ["সম্পর্ক"],
    "পরিচিতসমূহ": ["সম্পর্কসমূহ"],
    "নারীর": ["মহিলা"],
    "মাতৃচিত্র": ["পরিচর্যা"],
    "পিতৃচিত্র": ["পরিচর্যা"],
    "নাজুক": ["নরম"],
    "নাজুকতা": ["দুর্বলতা"],
    "উপযুক্ত": ["অখণ্ড"],
    "উপযুক্ততা": ["অখণ্ডতা"],
    "অপ্ররোচনামূলক": ["সন্দেহজনক"],
    "অপ্ররোচনামূলকসমূহ": ["সন্দেহজনকসমূহ"],
    "স্বার্থপরতা": ["স্বার্থপরতা"],
    "স্বার্থপর": ["স্বার্থপর"],
    "নিম্নতর": ["ছোট"],
    "নিম্নতা": ["অসুবিধা"],
    "অসন্দেহজনক": ["সততা"],
    "একাকী": ["একা"],
    "রটনা": ["গল্প"],
    "দুষ্টতা": ["নিষ্ঠুরতা"],
    "ভয়": ["ভীত"],
    "পারস্পরিক": ["বিনিময়"],
    "পারস্পরিকসমূহ": ["বিনিময়সমূহ"],
    "স্বাভাবিকতা": ["সামঞ্জস্য"],
    "স্পষ্টভাবে": ["নিরপেক্ষভাবে"],
    "মানদণ্ড": ["নিয়ম"],
    "মানদণ্ডসমূহ": ["নিয়মসমূহ"],
    "প্রোফাইল": ["ধরণ"],
    "ব্যক্তিত্ব": ["স্বকেন্দ্রিকতা"],
    "প্রতিষ্ঠা": ["গুরুত্ব"],
    "সুরক্ষা": ["রক্ষা"],
    "মনস্তাত্ত্বিক": ["মানসিক"],
    "বিনিময়": ["পারস্পরিক"],
    "বিনিময়তা": ["পারস্পরিকতা"],
    "সম্মিলন": ["সামঞ্জস্য"],
    "মাতৃসংশ্লিষ্ট": ["প্রদানকারী"],
    "পিতৃসংশ্লিষ্ট": ["প্রদানকারী"],
    "প্রতিষ্ঠা": ["চিত্র"],
    "হবে": ["অধিকার"],
    "চিকিৎসা": ["ব্যবস্থা"],
    "মান": ["নীতিমূলক"],
    "মানসমূহ": ["নীতিমূলকসমূহ"],
    "হিংসা": ["আক্রমণ"],
    "হিংসাত্মক": ["নিয়ন্ত্রণহীন"],
    "সংবেদনশীলতা": ["অনুভূতিপ্রবণতা"],
    "সংবেদনশীল": ["অনুভূতিপ্রবণ"]
}


def bias_synonyms(word):
    if BIAS_SYN_DICT_BN.get(word.lower()):
        bias_syn = random.choice(BIAS_SYN_DICT_BN[word.lower()])
        return bias_syn
    else:
        return synonyms(word)

def synonyms(word):
	syn = [] 
	word = word.lower()
	try:
		for related_words in np.random.choice(list(wn.synsets(word)), size=3):
			syn += related_words.lemmas()
		syn = set(syn)
		syn.remove(word)
	except:
		pass

	if syn:
		return random.choice(list(syn))
	else:
		return word


def text_augmentation(texts, bias_labels):
    augmented_texts = []
    
    for text, bias in zip(texts, bias_labels):
        aug_text = []

        for word in text.split():
            if word.lower() in BN_STOPWORDS:
                aug_text.append(word)
                continue

            if np.random.choice([True, False], p=[0.7, 0.3]):
                if bias:
                    aug_text.append(bias_synonyms(word))
                else:
                    aug_text.append(synonyms(word))
            else:
                aug_text.append(word)

        augmented_texts.append(" ".join(aug_text))

    return augmented_texts

def main():
    import json
    with open('dataset/test_data_augment.json') as f:
        data = json.load(f)
	
    texts = []
    bias = []
    for item in data.values():
        for text in item['পক্ষপাত_প্রসঙ্গ']:
            texts.append(text)
            bias.append(1 if item["পক্ষপাত"] != '' else 0)

    orig_texts = texts.copy()
	
    aug_texts = text_augmentation(texts, bias)

    for idx, text in enumerate(texts):
        if orig_texts[idx] != aug_texts[idx]:
            print(f"Original {idx}:: {text}")
            print(f"Augmented{idx}:: {aug_texts[idx]}")
            print()

if __name__ == "__main__":
    main()
