# -*- coding: utf-8 -*-
import pandas as pd
import sys

## thanks to shahram
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
#ab = aa.encode('ascii',errors='ignore')

#Retrieve main_dict
csvpath = '/home/ddan/Desktop/github/autocomplete/main_dict.csv'
main_dict = pd.read_csv(csvpath)
test1 = main_dict[-50:]

def clean_text(r):
    # return the list of decoded cell in the Series instead 
    return r.decode('unicode_escape').encode('ascii', 'ignore')

test1['text'] = test1['text'].apply(clean_text)
test1.head()
#test1['text'] = 'aa'
#s = u'aสุดยอด/คุณคือฮีโร่'
#print text_clean(s)

import string
import re

allow = string.letters + string.digits + ' -'
for index, row in test1.iterrows():
     test1.loc[index, 'text'] = re.sub('[^%s]' % allow, '', row[1])

test1.tail()



#
# test1.loc[index, 'text'] = re.sub('[^%s]' % allow, '', test1)
#
# print test1

#    aa = 'สุดยอด/คุณคือฮีโร่'
#    ab = aa.encode('ascii',errors='ignore')
#import nltk
#nltk.download()
#
#
#from nltk.tokenize import word_tokenize
#
## Apply word_tokenize to each element of the list called incoming_reports
#tokenized_reports = [word_tokenize(report) for report in test1.text]
#
## View tokenized_reports
#tokenized_reports
