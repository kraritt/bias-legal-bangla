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
			'বাদী',
			'বাদী_লিঙ্গ',
			'বিবাদী',
			'অপরাধ',
			'ভুক্তভোগী_আসামী_সম্পর্ক',
			'ভুক্তভোগী_লিঙ্গ',
			'মূল_দণ্ড',
			'প্রধান_আবেদন',
			'সম্পূরক_আবেদন',
			'আবেদন_কারণ',
			'প্রসিকিউটর_অবস্থান',
			'রায়',
			'রায়_কারণ',
			'বর্তমান_দণ্ড',
			'পক্ষপাত',
			'পক্ষপাত_লক্ষ্য']
annotated_df = pd.DataFrame(columns=attributes)
annotated_df[key] = annotate_subset 
annotated_df.to_csv('annotate.csv')
annotated_df = pd.read_csv('annotate_filled.csv')
