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


jr3 = pd.read_csv("jr3_violence.csv")
jr4 = pd.read_csv("jr4_violence.csv")
jr = pd.read_csv("jr_violence.csv")
jr1 = pd.read_csv("jr1_violence.csv")
jr2 = pd.read_csv("jr2_violence.csv")

df_list = [jr3, jr4, jr, jr1, jr2]

for item in df_list:
	item.drop(["Unnamed: 0"], axis=1, inplace=True)

	strips(item)

	despecialize(item)

	no_spaces(item)

	separate(item)

	item['bias'] = pd.Series(dtype='str')
	item['bias_target'] = pd.Series(dtype='str')

	item.sort_values('date_judgment', inplace=True, ignore_index=True)

jr3.to_csv("jr3_annotate.csv", escapechar=";")
jr4.to_csv("jr4_annotate.csv", escapechar=";")
jr.to_csv("jr_annotate.csv", escapechar=";")
jr1.to_csv("jr1_annotate.csv", escapechar=";")
jr2.to_csv("jr2_annotate.csv", escapechar=";")
