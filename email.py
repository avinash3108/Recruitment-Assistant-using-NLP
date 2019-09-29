import re

def extract_email(email):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
    if email:
        try:
            print(email[0].split()[0].strip(';'))
        except IndexError:
            return None
extract_email(open("C:/Users/Rohan/Desktop/1801.txt").read())        