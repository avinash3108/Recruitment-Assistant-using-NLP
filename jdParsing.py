from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
def python_to_txt_file(file_path):
            try:
                file_object = open(file_path, 'a')
                file_object.write(str(words1)+",")
                print(file_path + " created. ")
                file_object.close()
            except FileNotFoundError:
                print(file_path + " not found. ")
                file_object.close()
stop_words = stopwords.words('english')
newstopwords=['&','and/or','of','with','at','from','into','during','including','until',
'against','among','throughout','despite','towards','upon','concerning','to','in','for',
'on','by','about','like','through','over','before','between','after','since','without',
'under','within','along','following','across','behind','beyond','etc','etcetra',
'gathering','identifying','analyzing','large','Services','Collaborate','create','solutions',
'areas','test','knowledge','MUST','hands-on','etc.);','must','ability','track','environment',
'Familiarity','one','popular','Candidate','self-motivated','detail-oriented','willing',
'learn','understanding','willing','Products','Applications','etc.','to','and','with','lol']
stop_words.extend(newstopwords)
file1 = open("C:/Users/Abhinav/Desktop/Project/JD/sampleJD2.txt",'r')
line = file1.read()
words = line.split()
counter=0
for i in words:
    for j in range(0,len(words)):
        if i==words[j]:
            counter=counter+1
            if counter>1:
                words[j]='lol'
    counter=0
porter=PorterStemmer()
for w in words:
    tword=w.strip(",:().'-/")
    words1=porter.stem(tword)
    if not words1 in stop_words:
        if __name__ == '__main__':
            python_to_txt_file("C:/Users/Abhinav/Desktop/Project/JD/data3.txt")
file1.close()