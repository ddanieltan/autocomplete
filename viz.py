# -*- coding: utf-8 -*-
import pickle

csvpath = '/home/ddan/Desktop/github/autocomplete/data/'       
main_dict=dict()
with open(csvpath+"cleaned.p","rb") as f:
    main_dict = pickle.load(f)

lhl = main_dict = main_dict[main_dict.fbpage == 'leehsienloong']
