# -*- coding: utf-8 -*-
import pickle

##Building unigram dictionary
#def build_unigrams(sentences):
#    unigrams = dict()
#    for sentence in sentences:
#        for word in sentence:
#            if unigrams.has_key(word):
#                unigrams[word] += 1
#            else:
#                unigrams[word] = 1 #new entry for new word
#    #Return sorted list of (word,count) from most to least
#    return sorted(unigrams.items(), key=lambda (_, count): -count)
#
#def build_bigrams(sentences):
#    bigrams = dict()
#    for sentence in sentences:
#        for i in xrange(len(sentence)-1):
#            key = (sentence[i],sentence[i+1])
#            if bigrams.has_key(key):
#                bigrams[key] += 1
#            else:
#                bigrams[key] = 1
#    return sorted(bigrams.items(), key=lambda (_, count): -count)

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

def main():
    #Load cleaned corpus
    csvpath = '/home/ddan/Desktop/github/autocomplete/data/'       
    main_dict=dict()
    with open(csvpath+"cleaned.p","rb") as f:
        main_dict = pickle.load(f)
    
    #Build ngram dictionaries
#    unigrams = build_unigrams(main_dict['text'])
#    bigrams = build_bigrams(main_dict['text'])
    trigrams = build_trigrams(main_dict['text'])
    

    with open(csvpath+'trigrams.p','wb') as f:
        pickle.dump(trigrams,f)
    
if __name__ == "__main__":
    main()