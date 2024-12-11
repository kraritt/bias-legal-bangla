import pandas as pd 
import random 
import os 
random.seed(10)

def annotate_select(df):
	for column in list(df):
		if (df[column].nunique() == df.shape[0]):
			key = column 

	annotate_subset = random.sample(df[key].tolist(), k=int(0.1*df.shape[0]))
	annotate_subset.sort()
	return key, annotate_subset 

path = os.path.abspath(os.getcwd()) + "/"
df = pd.read_json(path + 'data_process_full.json')
key, annotate_subset = annotate_select(df)

attributes = [key,
			'appellant',
			'appellant_gender',
			'appellant',
			'crime',
			'victim',
			'victim_gender',
			'penalty_original',
			'requires',
			'requires_subsidy',
			'requer_motive',
			'mp_pj',
			'result',
			'result_reasons',
			'penalty_atual',
			'bias',
			'bias_target']
annotated_df = pd.DataFrame(columns=attributes)
annotated_df[key] = annotate_subset 
annotated_df.to_csv('annotate.csv')
annotated_df = pd.read_csv('annotate_filled.csv')




