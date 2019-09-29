# -*- coding: utf-8 -*-

import json
import re
from nltk.corpus import wordnet
def extract_email(resume):
    emails = re.findall("[\w\.]+@[\w\.-]+", resume)
    if emails:
        return(emails)
    else:
        return([])
        
def extract_phone(resume):
    phoneno = re.findall("[1-9]\d{9}|\+\d{2}\s?\d{10}",resume)
    if phoneno:
        return(phoneno)
    else:
        return([])

       
def extract_name_regex(resume_text):
    with open(resume_text,"r", encoding="utf8") as nlp_text1:
        list1=[]
        listline=[]
        for lines in nlp_text1:
            line=lines.strip()
            namelist=re.findall("((?:[A-Z](?:[a-z]+|\.)(?:[ ][A-Z](?:[a-z]+|\.)){1,3}$)|([A-Z]+\.?(?:\s[A-Z]+\.?){1,3}$))",line)
            list1.append(namelist) 
            listline.append(line)
    list2 = [x for x in list1 if x != []]
    list2 = [x[0][0] for x in list2]
    
    for words in list2[0:5]:
        word=words.lower().split()
        lis=[]
        for x in word:
            if wordnet.synsets(x):
                lis.append(0)
            else:
                lis.append(1)
        if any(x==1 for x in lis):       
            if word==['curriculum','vitae']:
                continue
            else:
                return(str(words))
                break


if __name__ == '__main__':
    for i in range(0, 5):            
        with open("D:\project\\textresumes\\"+str(i)+".txt",encoding="utf8") as resum:
            resume = resum.read()
            name=extract_name_regex("D:\project\\textresumes\\"+str(i)+".txt")
            print(name)
            emails=list(set(extract_email(resume)))
            print(emails)
            phone=list(set(extract_phone(resume)))
            print(phone)
        resdict={"name":name, "emails":emails, "phone":phone}
        
        with open('D:\\project\\resume json files\\'+str(i)+'.JSON', 'w') as fp:
            rjson=json.dump(resdict, fp)
             
     
        
        