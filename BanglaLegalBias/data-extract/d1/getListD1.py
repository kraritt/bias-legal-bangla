import pandas as pd 
table = pd.read_excel("process with status.xlsx")


codes = []
for item in table["process"]:
	codes.append(item)

with open("list_process.txt", "w") as f:
	for item in codes:
		f.write("%s\n" % item)