# -*- coding: utf-8 -*-
import pickle

def build_trigrams(sentences):
    trigrams = dict()
    for sentence in sentences:
        for i in xrange(len(sentence)-2):
            key = tuple(sentence[i:i+3])
            if trigrams.has_key(key):
                trigrams[key] += 1
            else:
                trigrams[key] = 1
    return sorted(trigrams.items(), key=lambda (_, count): -count)

csvpath = '/home/ddan/Desktop/github/autocomplete/data/'       
main_dict=dict()
with open(csvpath+"cleaned.p","rb") as f:
    main_dict = pickle.load(f)

lhl = main_dict = main_dict[main_dict.fbpage == 'leehsienloong']
