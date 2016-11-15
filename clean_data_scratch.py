# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:23:31 2016

@author: ddan
"""
import pandas as pd
import os

 #Retrieve main_dict
csvpath = '/home/ddan/Desktop/github/autocomplete/main_dict.csv'    
main_dict = pd.read_csv(csvpath)

    
test1 = main_dict[-50:]

import string
import re

allow = string.letters + string.digits + '-'
for index, row in test1.iterrows():
    test1.loc[index, 'text'] = re.sub('[^%s]' % allow, '', row[0])
    
text1 = test1.text
text1[-20:]


test1.loc[index, 'text'] = re.sub('[^%s]' % allow, '', test1)


 
        
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