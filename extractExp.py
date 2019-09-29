
import datefinder
from datetime import date
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer 

def Exp(resume_path):
	resume_text = open(resume_path, 'r')
	ps = PorterStemmer()
	lem = WordNetLemmatizer()
	wordindex = []
	resume_lemm = []
	temp = []
	list_lemmatize = []
	for i in resume_text:
		resume_text = resume_text.replace("-", " t ")
	import re
	resume_regex = [re.sub('[^a-zA-Z0-9/]+', '', _) for _ in resume_text.split()]	

	for i in resume_regex:
		resume_lemm.append(ps.stem(i))

	list1 = ["Education" ,"Skills", "STRENGTH" , "Achievements",  "Contact", "Technical",  "Projects", "Address",  'Academic']

	for i in list1:
		list_lemmatize.append(ps.stem(i))
	 
	for st in list_lemmatize:	
		start = resume_lemm.index("experi")
		 
		if st in resume_lemm:
			end_temp = resume_lemm.index(st)
			if start < end_temp:
				end = resume_lemm.index(st)
				temp.append(resume_text[start : end])
				wordindex.append(resume_lemm.index(st))
			else:
				continue
	wordindex.sort()
	index = [i for i in wordindex  if i > start ]
	find_date1 = resume_lemm[start:index[0]]

	for st in find_date1:
		find_date1 = [str(date.today()) if st == "current" else st for st in find_date1]
		find_date1 = [str(date.today()) if st == "present" else st for st in find_date1]
		find_date1 = [str(date.today()) if st == "now" else st for st in find_date1]
		find_date1 = [str(date.today()) if st == "till date" else st for st in find_date1]
		find_date1 = ["jan" if st == "januari" else st for st in find_date1]
		find_date1 = ["feb" if st == "februari" else st for st in find_date1]
		find_date1 = ["july" if st == "juli" else st for st in find_date1]
		find_date1 = ["sep" if st == "septemb" else st for st in find_date1]
		find_date1 = ["oct" if st == "octob" else st for st in find_date1]
		find_date1 = ["nov" if st == "novemb" else st for st in find_date1] 
		find_date1 = ["dec" if st == "decemb" else st for st in find_date1]
	date_string = ' '.join(find_date1)		  	
	matches = datefinder.find_dates(str(date_string))
	dates_list = list(matches)
	
	for i in range(len(dates_list)):
	dates_list[i] = dates_list[i].date()
	
	j = 0
	total_days = 0
	if len(dates_list) == 1:
	dates_list.append(date.today())
	
	for i in dates_list:               
		total_days = total_days + (dates_list[j+1] - dates_list[j]).days
		j = j+2
		if j > (len(dates_list)-1):
			break	
	totalex = round((total_days/365),1)
	return totalex
 	resume_path.close()
