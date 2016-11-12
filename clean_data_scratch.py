# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:23:31 2016

@author: ddan
"""
import pandas as pd
import os
import csv
import regex

if __name__ == '__main__':
    #Retrieve main_dict
    csvpath = os.getcwd()+'/main_dict.csv'    
    main_dict = pd.read_csv('main_dict.csv')
#    print main_dict  
    
    test1 = main_dict[-50:]
    result = test1.text.encode('ascii',errors='ignore')
        
    aa = 'สุดยอด/คุณคือฮีโร่'
    ab = aa.encode('ascii',errors='ignore')
    