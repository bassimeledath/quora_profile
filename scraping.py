import numpy as np
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import seaborn as sns

my_page = 'https://www.quora.com/profile/Bassim-Eledath-1'
page = urllib.request.urlopen(my_page)
soup = BeautifulSoup(page, 'html.parser')

links = soup.find_all('a', href=True)
list_questions = []
for link in links:
    list_questions.append(link['href'])
    
my_stats = []
numbers = []
labels = []
for x in soup.find_all('a',href=True):
    if x.find_all('span', {'class' : 'list_count'})!=[]:
        my_stats.append(x.text)
        
for x in my_stats:
    numbers.append(re.findall('\d+', x ))
numbers = [int(item) for sublist in numbers for item in sublist]
for x in my_stats:
    word = ''.join([i for i in x if not i.isdigit()])
    labels.append(word)

    
# formatting 
questions = []
knows_about = []
for x in list_questions:
    if x.find('#') == -1:
        if x.find('profile') == -1:
            if x.find('api') == -1:
                x = x.replace('/','')
                x = x.replace('-',' ')
                x = x.replace('Bassim Eledath','')
                x = x.replace('answer 1','')
                if x.startswith('topic'):
                    x = x.replace('topic','')
                    x = x.replace(' 1','')
                    x = x.replace(' 1','')
                    knows_about.append(x)
                else:
                    questions.append(x)
                    
questions  = [x for x in questions if x not in ['','about', 'careers', 'aboutprivacy', 'abouttos','contact']]
knows_about = list(set(knows_about))
page_title = soup.title.string
answers = [x.text for x in soup.find_all('p')]