# -*- coding: utf-8 -*-
import cPickle as pickle

csvpath = '/home/ddan/Desktop/github/autocomplete/data/'       
with open(csvpath+"lhl.p","rb") as f:
    lhl = pickle.load(f)

