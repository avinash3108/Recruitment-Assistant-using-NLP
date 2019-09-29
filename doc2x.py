"""
PROBABLY WON'T RUN ON WINDOWS 
"""
import os
import glob
import subprocess
import parsers as pr

files = pr.explore(os.getcwd())
for f in files:
	if(f.endswith(".doc")):
		subprocess.call(['soffice', '--headless', '--convert-to', 'docx', '--outdir', os.path.join(os.getcwd(), 'doc2'), f])
