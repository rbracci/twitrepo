# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
import re
from bs4 import BeautifulSoup

print ('\n\n\n Program is running')

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
y = requests.get(base_url)
soup = BeautifulSoup(y.text, "html.parser")


findword = soup.find_all(text = re.compile('student')) #using a real expression to find all forms of student on the page
for word in findword:
    fixed_text = str(word).replace('student', 'AMAZING student') #replaces all possibilities of student with AMAzing student
    word.replace_with(fixed_text)

for new_image in soup.findAll('iframe'):
	new_image['src'] = "/Users/robertbracci/desktop/project3/SI206/icecream.jpg" #replaces the iframe image with the image I assigned it from my desktop

for local_image in soup.findAll('img'):
	local_image['src'] = "/Users/robertbracci/desktop/project3/SI206/HW3-StudentCopy/Media/logo.png" #replaces the local image 'img' with the image I assigned it

file = open("UMSI_ROBBIE.html", "w")
print('Generating complete html file')
file.write(str(soup)) #creates and writes the html file
file.close()
print('Done')