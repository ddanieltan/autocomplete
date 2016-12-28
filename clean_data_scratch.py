# -*- coding: utf-8 -*-
import pandas as pd
import sys
from HTMLParser import HTMLParser
from nltk.tokenize import word_tokenize
import re

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
    "'s" : " is", 
    "'re" : " are",
    "'t" : " not",
    "'ve" : " have",
    "'d" : " would"
    }

#from clean_text()
#    answer = html_parser.unescape(answer) #remove HTML artifacts
#  answer = [word.encode('ascii', 'ignore').lower() for word in answer]
#  

def remove_punctuation_digits(text):
    return re.sub("[\.\t\,\:;\(\)\.\d]", "", text, 0, 0)

def replace_apostrophes(text):
    pattern = re.compile(r'\b(' + '|'.join(APOSTROPHES.keys()) + r')\b')
    result = pattern.sub(lambda x: APOSTROPHES[x.group()], text)    
    return result

def clean_text(sentence):##remove HTML
  answer = sentence.decode('ascii','ignore')
  answer = answer.decode('ascii','ignore').lower()
  answer = replace_apostrophes(answer)
  answer = remove_punctuation_digits(answer)
  answer = word_tokenize(answer)
  return answer

main_dict['text'] = main_dict['text'].apply(clean_text)
main_dict.head()



#
#
#aa = "thi3s is a t22e,,,2st's 111"
#aa = aa.decode('ascii','ignore')
#aa = aa.encode('ascii','ignore').lower()
#aa = replace_apostrophes(aa)
#aa = remove_punctuation_digits(aa) ## this has to happen first
#aa
#aa = word_tokenize(aa)
#aa = [APOSTROPHES[word] if word in APOSTROPHES else word for word in aa]
#
#aa