def gen_txt_list(table, court):
	codes = []
	for item in table["process"]:
		codes.append(item.strip())

	filename = "list_" + court + ".txt"
	with open(filename, "w") as f:
		for item in codes:
			f.write("%s\n" % item)


import pandas as pd 
table = pd.ExcelFile("d2_data.xlsx")

sheet_jr3 = table.parse(0)
sheet_jr4 = table.parse(1)
sheet_jr = table.parse(2)
sheet_jr1 = table.parse(3)
sheet_jr2 = table.parse(4)


cn_jr3 = list(sheet_jr3.columns)
cn_jr4 = list(sheet_jr4.columns)
cn_jr = list(sheet_jr.columns)
cn_jr1 = list(sheet_jr1.columns)
cn_jr2 = list(sheet_jr2.columns)

cn_jr3_new = ["process", "mag", "data_judgment", "whole_teor", "subject", 
		       "alleged_pac", "accused_pac", "violence_woman", "violence_minor",
			   "accused_violence", "result_violence", "proof_violence",
			   "result_pac", "proof_pac"]
cn_jr1_new = ["process", "mag", "stick", "data_judgment", "whole_teor", "subject", 
		       "alleged_pac", "accused_pac", "violence_woman", "violence_minor",
			   "accused_violence", "result_violence", "proof_violence",
			   "result_pac", "proof_pac"]
cn_si_new = ["process", "relator", "body_judging", "data_judgment", "type_resource", 
			"collegiality", "whole_teor", "subject", "alleged_pac", "accused_pac", 
			"violence_woman", "violence_minor", "accused_violence", "result_violence", "proof_violence",
			"result_pac", "proof_pac"]

dict_jr3 = {cn_jr3[0]: cn_jr3_new[0], cn_jr3[1]: cn_jr3_new[1], cn_jr3[2]: cn_jr3_new[2],
				  cn_jr3[3]: cn_jr3_new[3], cn_jr3[4]: cn_jr3_new[4], cn_jr3[5]: cn_jr3_new[5],
				  cn_jr3[6]: cn_jr3_new[6], cn_jr3[7]: cn_jr3_new[7], cn_jr3[8]: cn_jr3_new[8],
				  cn_jr3[9]: cn_jr3_new[9], cn_jr3[10]: cn_jr3_new[10], cn_jr3[11]: cn_jr3_new[11],
				  cn_jr3[12]: cn_jr3_new[12], cn_jr3[13]: cn_jr3_new[13]}
dict_jr4 = {cn_jr4[0]: cn_si_new[0], cn_jr4[1]: cn_si_new[1], cn_jr4[2]: cn_si_new[2],
				  cn_jr4[3]: cn_si_new[3], cn_jr4[4]: cn_si_new[4], cn_jr4[5]: cn_si_new[5],
				  cn_jr4[6]: cn_si_new[6], cn_jr4[7]: cn_si_new[7], cn_jr4[8]: cn_si_new[8],
				  cn_jr4[9]: cn_si_new[9], cn_jr4[10]: cn_si_new[10], cn_jr4[11]: cn_si_new[11],
				  cn_jr4[12]: cn_si_new[12], cn_jr4[13]: cn_si_new[13], cn_jr4[14]: cn_si_new[14], 
				  cn_jr4[15]: cn_si_new[15], cn_jr4[16]: cn_si_new[16]}
dict_jr = {cn_jr[0]: cn_si_new[0], cn_jr[1]: cn_si_new[1], cn_jr[2]: cn_si_new[2],
				  cn_jr[3]: cn_si_new[3], cn_jr[4]: cn_si_new[4], cn_jr[5]: cn_si_new[5],
				  cn_jr[6]: cn_si_new[6], cn_jr[7]: cn_si_new[7], cn_jr[8]: cn_si_new[8],
				  cn_jr[9]: cn_si_new[9], cn_jr[10]: cn_si_new[10], cn_jr[11]: cn_si_new[11],
				  cn_jr[12]: cn_si_new[12], cn_jr[13]: cn_si_new[13], cn_jr[14]: cn_si_new[14], 
				  cn_jr[15]: cn_si_new[15], cn_jr[16]: cn_si_new[16]}
dict_jr1 = {cn_jr1[0]: cn_jr1_new[0], cn_jr1[1]: cn_jr1_new[1], cn_jr1[2]: cn_jr1_new[2],
				  cn_jr1[3]: cn_jr1_new[3], cn_jr1[4]: cn_jr1_new[4], cn_jr1[5]: cn_jr1_new[5], 
				  cn_jr1[6]: cn_jr1_new[6], cn_jr1[7]: cn_jr1_new[7], cn_jr1[8]: cn_jr1_new[8], 
				  cn_jr1[9]: cn_jr1_new[9], cn_jr1[10]: cn_jr1_new[10], cn_jr1[11]: cn_jr1_new[11], 
				  cn_jr1[12]: cn_jr1_new[12], cn_jr1[13]: cn_jr1_new[13], cn_jr1[14]: cn_jr1_new[14]}
dict_jr2 = {cn_jr2[0]: cn_si_new[0], cn_jr2[1]: cn_si_new[1], cn_jr2[2]: cn_si_new[2],
				  cn_jr2[3]: cn_si_new[3], cn_jr2[4]: cn_si_new[4], cn_jr2[5]: cn_si_new[5],
				  cn_jr2[6]: cn_si_new[6], cn_jr2[7]: cn_si_new[7], cn_jr2[8]: cn_si_new[8],
				  cn_jr2[9]: cn_si_new[9], cn_jr2[10]: cn_si_new[10], cn_jr2[11]: cn_si_new[11],
				  cn_jr2[12]: cn_si_new[12], cn_jr2[13]: cn_si_new[13], cn_jr2[14]: cn_si_new[14], 
				  cn_jr2[15]: cn_si_new[15], cn_jr2[16]: cn_si_new[16]}

sheet_jr3.rename(mapper=dict_jr3, axis=1, inplace=True)
sheet_jr4.rename(mapper=dict_jr4, axis=1, inplace=True)
sheet_jr.rename(mapper=dict_jr, axis=1, inplace=True)
sheet_jr1.rename(mapper=dict_jr1, axis=1, inplace=True)
sheet_jr2.rename(mapper=dict_jr2, axis=1, inplace=True)


jr3_violence = sheet_jr3.loc[sheet_jr3['violence_minor'].str.contains('sexual', na=False)]
jr4_violence = sheet_jr4.loc[sheet_jr4['violence_minor'].str.contains('sexual', na=False)]
jr_violence = sheet_jr.loc[sheet_jr['violence_minor'].str.contains('sexual', na=False)]
jr1_violence = sheet_jr1.loc[sheet_jr1['violence_minor'].str.contains('sexual', na=False)]
jr2_violence = sheet_jr2.loc[sheet_jr2['violence_minor'].str.contains('sexual', na=False)]

gen_txt_list(jr3_violence, "jr3")
gen_txt_list(jr4_violence, "jr4")
gen_txt_list(jr_violence, "jr")
gen_txt_list(jr1_violence, "jr1")
gen_txt_list(jr2_violence, "jr2")

jr3_violence.to_csv("jr3_violence.csv")
jr4_violence.to_csv("jr4_violence.csv")
jr_violence.to_csv("jr_violence.csv")
jr1_violence.to_csv("jr1_violence.csv")
jr2_violence.to_csv("jr2_violence.csv")
