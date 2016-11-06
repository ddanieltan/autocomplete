# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 15:47:54 2016

@author: ddan
"""

import pandas as pd
import os
import csv

#Reads posts from csv files and returns a df
def record_post(page):
    path = base_path + page + '_fb_posts.csv'
    csvfile = pd.read_csv(path, quoting=csv.QUOTE_NONE, #Quote_none solves EOF error
                          error_bad_lines=False, na_values=['.'], 
                          delimiter=',',index_col=False) #index_cols=False to not use ID as index
    csvfile['fbpage'] = page
    csvfile['isPost'] = True
    csvfile = csvfile.rename(columns={'status_message':'text'})
    col_names = ['text','fbpage','isPost']
    merge_dict = csvfile[col_names]
    merge_dict['text'] = merge_dict['text'].apply(str)
    return merge_dict

#Reads comments from csv files and returns a df
def record_comments(page):
    path = base_path + page + '_fb_comments.csv'
    csvfile = pd.read_csv(path, quoting=csv.QUOTE_NONE, 
                          error_bad_lines=False, na_values=['.'], 
                          delimiter=',',index_col=False)
    csvfile['fbpage'] = page
    csvfile['isPost'] = False
    csvfile = csvfile.rename(columns={'comment_message':'text'})
    col_names = ['text','fbpage','isPost']
    merge_dict = csvfile[col_names]
    merge_dict['text'] = merge_dict['text'].apply(str)
    return merge_dict 


if __name__ == '__main__':
    fb_pages =['leehsienloong','TheStraitsTimes','nlbsg','TharmanShanmugaratnam','k.shanmugam.page',
           'TanChuanJin1','Vivian.Balakrishnan.Sg','flyscoot',
           'sgag.sg','singaporeair','josephprince','TheMiddleGroundSG','yoursingapore']
    
    #Creating main dictionary with 3 columns
    col_names = ['text','fbpage','isPost']
    main_dict = pd.DataFrame(columns=col_names)
    
    base_path = os.getcwd()+'/data/'

    # Recording posts into main dictionary
    for page in fb_pages:
        merge_dict = None        
        try:
            merge_dict = record_post(page)
            main_dict = main_dict.append(merge_dict)              
        except Exception, e:
            print e
            pass
    
    # Recording comments into main dictionary
    for page in fb_pages:
        merge_dict = None        
        try:
            merge_dict = record_comments(page)
            main_dict = main_dict.append(merge_dict)              
        except Exception, e:
            print e
            pass

    main_dict.index = range(len(main_dict)) #Re-labeling index
    print main_dict    
#    [3025638 rows x 3 columns]
#    >>> print main_dict.describe()
#           text        fbpage   isPost
#           count   3025638       3025638  3025638
#           unique   780478            12        2
#           top         nan  josephprince    False
#           freq    1339816       2079589  2817373
    
#    test_dict = main_dict[-35:]
#    print test_dict




