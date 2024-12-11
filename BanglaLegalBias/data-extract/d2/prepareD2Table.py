import pandas as pd 

def strips(df):
	for column in df:
		if(df[column].dtypes == 'object' or 
			df[column].dtypes == 'str'):
			df[column] = df[column].str.strip()


def despecialize(df):
	for column in df:
		if(df[column].dtypes == 'object' or 
			df[column].dtypes == 'str'):
			df[column] = df[column].str.replace("(", "")
			df[column] = df[column].str.replace(")", "")

def no_spaces(df):
	for column in df:
		if(df[column].dtypes == 'object' or 
			df[column].dtypes == 'str'):
			df[column] = df[column].str.replace(" ", "_")  

def separate(df):
	for column in df:
		if(df[column].dtypes == 'object' or 
			df[column].dtypes == 'str'):
			df[column] = df[column].str.replace("/", "; ")


tjmg1 = pd.read_csv("jrmg1_violence.csv")
tjmg2 = pd.read_csv("jrmg2_violence.csv")
tjrj = pd.read_csv("jrrj_violence.csv")
tjsp1 = pd.read_csv("jrsp1_violence.csv")
tjsp2 = pd.read_csv("jrsp2_violence.csv")

df_list = [tjmg1, tjmg2, tjrj, tjsp1, tjsp2]

for item in df_list:
	item.drop(["Unnamed: 0"], axis=1, inplace=True)

	strips(item)

	despecialize(item)

	no_spaces(item)

	separate(item)

	item['bias'] = pd.Series(dtype='str')
	item['bias_target'] = pd.Series(dtype='str')

	item.sort_values('date_judgment', inplace=True, ignore_index=True)

tjmg1.to_csv("jrmg1_annotate.csv", escapechar=";")
tjmg2.to_csv("jrmg2_annotate.csv", escapechar=";")
tjrj.to_csv("jrrj_annotate.csv", escapechar=";")
tjsp1.to_csv("jrsp1_annotate.csv", escapechar=";")
tjsp2.to_csv("jrsp2_annotate.csv", escapechar=";")
