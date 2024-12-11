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

sheet_jrmg1 = table.parse(0)
sheet_jrmg2 = table.parse(1)
sheet_jrrj = table.parse(2)
sheet_jrsp1 = table.parse(3)
sheet_jrsp2 = table.parse(4)


cn_tjmg1 = list(sheet_jrmg1.columns)
cn_tjmg2 = list(sheet_jrmg2.columns)
cn_tjrj = list(sheet_jrrj.columns)
cn_tjsp1 = list(sheet_jrsp1.columns)
cn_tjsp2 = list(sheet_jrsp2.columns)

cn_jrmg1_new = ["process", "mag", "data_judgment", "whole_teor", "subject", 
		       "alleged_pac", "accused_pac", "violence_woman", "violence_minor",
			   "accused_violence", "result_violence", "proof_violence",
			   "result_pac", "proof_pac"]
cn_jrsp1_new = ["process", "mag", "stick", "data_judgment", "whole_teor", "subject", 
		       "alleged_pac", "accused_pac", "violence_woman", "violence_minor",
			   "accused_violence", "result_violence", "proof_violence",
			   "result_pac", "proof_pac"]
cn_si_new = ["process", "relator", "body_judging", "data_judgment", "type_resource", 
			"collegiality", "whole_teor", "subject", "alleged_pac", "accused_pac", 
			"violence_woman", "violence_minor", "accused_violence", "result_violence", "proof_violence",
			"result_pac", "proof_pac"]

dict_tjmg1 = {cn_tjmg1[0]: cn_jrmg1_new[0], cn_tjmg1[1]: cn_jrmg1_new[1], cn_tjmg1[2]: cn_jrmg1_new[2],
				  cn_tjmg1[3]: cn_jrmg1_new[3], cn_tjmg1[4]: cn_jrmg1_new[4], cn_tjmg1[5]: cn_jrmg1_new[5],
				  cn_tjmg1[6]: cn_jrmg1_new[6], cn_tjmg1[7]: cn_jrmg1_new[7], cn_tjmg1[8]: cn_jrmg1_new[8],
				  cn_tjmg1[9]: cn_jrmg1_new[9], cn_tjmg1[10]: cn_jrmg1_new[10], cn_tjmg1[11]: cn_jrmg1_new[11],
				  cn_tjmg1[12]: cn_jrmg1_new[12], cn_tjmg1[13]: cn_jrmg1_new[13]}
dict_tjmg2 = {cn_tjmg2[0]: cn_si_new[0], cn_tjmg2[1]: cn_si_new[1], cn_tjmg2[2]: cn_si_new[2],
				  cn_tjmg2[3]: cn_si_new[3], cn_tjmg2[4]: cn_si_new[4], cn_tjmg2[5]: cn_si_new[5],
				  cn_tjmg2[6]: cn_si_new[6], cn_tjmg2[7]: cn_si_new[7], cn_tjmg2[8]: cn_si_new[8],
				  cn_tjmg2[9]: cn_si_new[9], cn_tjmg2[10]: cn_si_new[10], cn_tjmg2[11]: cn_si_new[11],
				  cn_tjmg2[12]: cn_si_new[12], cn_tjmg2[13]: cn_si_new[13], cn_tjmg2[14]: cn_si_new[14], 
				  cn_tjmg2[15]: cn_si_new[15], cn_tjmg2[16]: cn_si_new[16]}
dict_tjrj = {cn_tjrj[0]: cn_si_new[0], cn_tjrj[1]: cn_si_new[1], cn_tjrj[2]: cn_si_new[2],
				  cn_tjrj[3]: cn_si_new[3], cn_tjrj[4]: cn_si_new[4], cn_tjrj[5]: cn_si_new[5],
				  cn_tjrj[6]: cn_si_new[6], cn_tjrj[7]: cn_si_new[7], cn_tjrj[8]: cn_si_new[8],
				  cn_tjrj[9]: cn_si_new[9], cn_tjrj[10]: cn_si_new[10], cn_tjrj[11]: cn_si_new[11],
				  cn_tjrj[12]: cn_si_new[12], cn_tjrj[13]: cn_si_new[13], cn_tjrj[14]: cn_si_new[14], 
				  cn_tjrj[15]: cn_si_new[15], cn_tjrj[16]: cn_si_new[16]}
dict_tjsp1 = {cn_tjsp1[0]: cn_jrsp1_new[0], cn_tjsp1[1]: cn_jrsp1_new[1], cn_tjsp1[2]: cn_jrsp1_new[2],
				  cn_tjsp1[3]: cn_jrsp1_new[3], cn_tjsp1[4]: cn_jrsp1_new[4], cn_tjsp1[5]: cn_jrsp1_new[5], 
				  cn_tjsp1[6]: cn_jrsp1_new[6], cn_tjsp1[7]: cn_jrsp1_new[7], cn_tjsp1[8]: cn_jrsp1_new[8], 
				  cn_tjsp1[9]: cn_jrsp1_new[9], cn_tjsp1[10]: cn_jrsp1_new[10], cn_tjsp1[11]: cn_jrsp1_new[11], 
				  cn_tjsp1[12]: cn_jrsp1_new[12], cn_tjsp1[13]: cn_jrsp1_new[13], cn_tjsp1[14]: cn_jrsp1_new[14]}
dict_tjsp2 = {cn_tjsp2[0]: cn_si_new[0], cn_tjsp2[1]: cn_si_new[1], cn_tjsp2[2]: cn_si_new[2],
				  cn_tjsp2[3]: cn_si_new[3], cn_tjsp2[4]: cn_si_new[4], cn_tjsp2[5]: cn_si_new[5],
				  cn_tjsp2[6]: cn_si_new[6], cn_tjsp2[7]: cn_si_new[7], cn_tjsp2[8]: cn_si_new[8],
				  cn_tjsp2[9]: cn_si_new[9], cn_tjsp2[10]: cn_si_new[10], cn_tjsp2[11]: cn_si_new[11],
				  cn_tjsp2[12]: cn_si_new[12], cn_tjsp2[13]: cn_si_new[13], cn_tjsp2[14]: cn_si_new[14], 
				  cn_tjsp2[15]: cn_si_new[15], cn_tjsp2[16]: cn_si_new[16]}

sheet_jrmg1.rename(mapper=dict_tjmg1, axis=1, inplace=True)
sheet_jrmg2.rename(mapper=dict_tjmg2, axis=1, inplace=True)
sheet_jrrj.rename(mapper=dict_tjrj, axis=1, inplace=True)
sheet_jrsp1.rename(mapper=dict_tjsp1, axis=1, inplace=True)
sheet_jrsp2.rename(mapper=dict_tjsp2, axis=1, inplace=True)


tjmg1_violence = sheet_jrmg1.loc[sheet_jrmg1['violence_minor'].str.contains('sexual', na=False)]
tjmg2_violence = sheet_jrmg2.loc[sheet_jrmg2['violence_minor'].str.contains('sexual', na=False)]
tjrj_violence = sheet_jrrj.loc[sheet_jrrj['violence_minor'].str.contains('sexual', na=False)]
tjsp1_violence = sheet_jrsp1.loc[sheet_jrsp1['violence_minor'].str.contains('sexual', na=False)]
tjsp2_violence = sheet_jrsp2.loc[sheet_jrsp2['violence_minor'].str.contains('sexual', na=False)]

gen_txt_list(tjmg1_violence, "tjmg1")
gen_txt_list(tjmg2_violence, "tjmg2")
gen_txt_list(tjrj_violence, "tjrj")
gen_txt_list(tjsp1_violence, "tjsp1")
gen_txt_list(tjsp2_violence, "tjsp2")

tjmg1_violence.to_csv("tjmg1_violence.csv")
tjmg2_violence.to_csv("tjmg2_violence.csv")
tjrj_violence.to_csv("tjrj_violence.csv")
tjsp1_violence.to_csv("tjsp1_violence.csv")
tjsp2_violence.to_csv("tjsp2_violence.csv")
