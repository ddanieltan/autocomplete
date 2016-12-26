# -*- coding: utf-8 -*-
import pandas as pd
import sys
import string
from HTMLParser import HTMLParser
from nltk.tokenize import word_tokenize

## thanks to shahram
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

#Retrieve main_dict
csvpath = '/home/ddan/Desktop/github/autocomplete/main_dict.csv'
main_dict = pd.read_csv(csvpath, encoding='utf-8')
main_dict['text'] = main_dict['text'].astype(str)
test1 = main_dict[-50:]

html_parser = HTMLParser()
APOSTROPHES = {
    "'s" : "is", 
    "'re" : "are",
    "'t" : "not",
    "'ve" : " have",
    "'d" : " would"
    }

#from clean_text()
#    answer = html_parser.unescape(answer) #remove HTML artifacts

def clean_text(sentence):
  answer = sentence.decode('ascii','ignore')
  answer = word_tokenize(answer)
  answer = [word.encode('ascii', 'ignore').lower() for word in answer]
  answer = [APOSTROPHES[word] if word in APOSTROPHES else word for word in answer]
  answer = [word.translate(None, string.punctuation) for word in answer]
  answer = [word.translate(None, string.digits) for word in answer]
  return answer

main_dict['text'] = main_dict['text'].apply(clean_text)
main_dict.head()

