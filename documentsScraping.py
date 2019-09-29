#Doc Scraping

import time
import requests
from bs4 import BeautifulSoup

#Specify the URL of the archive here
archive_url = "http://www.symmetrical.in/uploads/resume-panel/"

def get_resume_links():
    
    # create responde object
    r = requests.get(archive_url)
    
    # create BeautifulSoup object
    soup = BeautifulSoup(r.content,"html5lib")
    
    # find all links on web-page
    links = soup.find_all("a");
    
    '''
    # filter the link sending with .doc
    resume_links = [archive_url + link["href"] for link in links if link["href"].endswith("doc")]
    '''
    
    # filter the link sending with .docx
    resume_links = [archive_url + link["href"] for link in links if link["href"].endswith("docx")]

    # filter the link sending with .pdf
    resume_links = [archive_url + link["href"] for link in links if link["href"].endswith("pdf")]
    
    return resume_links

def download_resume(resume_links):
    
    for link in resume_links:
        
        '''iterate through all links in resume_links and download them one by one'''
        
        # obtain filename by splitting url and getting last string
        #bad_chars = [';', ':', '!', "*","_","%","-","(",")"]
        
        file_name = link.split("/")[-1]
        
        #for i in bad_chars : 
        #    file_name = file_name.replace(i, '') 
        
        
        #file_name_c = len(file_name
        #file_name = file_name[30:] if int(file_name_c)>30 else file_name
        
                
        print ("Downloading file: %s"%file_name)
        
        # create response object
        r = requests.get(link,stream = True)
        
        # download started
        with open(str(file_name), "wb") as f :
            for chunk in r.iter_content(chunk_size = 10240*1024):
                if chunk:
                    f.write(chunk)
                    
        print ("%s Downloaded!\n"%file_name)
       # time.sleep(1)
    
    print ("All Files Downloaded!")
    
    return

if __name__=="__main__":
    
    # getting all file links
    resume_links = get_resume_links()
    
    # downloads all files
    download_resume(resume_links)
        