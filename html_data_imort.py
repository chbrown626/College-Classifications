#Importing a single file
salton = open('D:/Users/Christianna Brown/Desktop/MSDS 696/Data Files/webkb/data/webkb/course/cornell/http_^^www.cs.cornell.edu^Info^Department^Annual94^Faculty^Salton.html', 'rb')

#Review the data
salton.read()

#Apply Beautiful Soup to the data to clean the html
#Using lxml
from bs4 import BeautifulSoup
soup = BeautifulSoup(salton, 'lxml') #This step keeps completely deleting everything from the salton file

print(soup.prettify())

print(soup)

soup

salton.read()

#Using html.parser
soup = BeautifulSoup(salton, 'html.parser') #This step keeps completely deleting everything from the salton file

print(soup.prettify())

print(soup)

soup

salton.read()

#Importing all files
import os
from bs4 import BeautifulSoup

walk = os.walk('/Users/Christianna Brown/Desktop/MSDS 696/Data Files/webkb/data/webkb')
walk
walk = list(walk)
walk

html_data = []
soup_data = []
text = []

for root, dirs, files in walk:
    for file in files:
        print(root)
        print(file)
        print('/'.join([root, file]))
        full_filepath = os.path.join(root, file)
        print(full_filepath)
        if os.path.isfile(full_filepath):
            print('file')
            with open(full_filepath, 'rb') as open_file:
                data = open_file.read()
#                 print(data)
                html_data.append(data)
                soup_file = BeautifulSoup(data, 'lxml')
                soup_data.append(soup_file)
                text.append(soup_file.text)

len(text)
text[25]
