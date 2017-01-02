# -*- coding: utf-8 -*-
import pickle
import random

#Building unigram dictionary
def build_unigrams(sentences):
    unigrams = dict()
    for sentence in sentences:
        for word in sentence:
            if unigrams.has_key(word):
                unigrams[word] += 1
            else:
                unigrams[word] = 1 #new entry for new word
    #Return sorted list of (word,count) from most to least
    return sorted(unigrams.items(), key=lambda (_, count): -count)

def build_bigrams(sentences):
    bigrams = dict()
    for sentence in sentences:
        for i in xrange(len(sentence)-1):
            key = (sentence[i],sentence[i+1])
            if bigrams.has_key(key):
                bigrams[key] += 1
            else:
                bigrams[key] = 1
    return sorted(bigrams.items(), key=lambda (_, count): -count)

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

#Applying weighted probabilities
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w > r:
         return c
      upto += w

def predict_sentence(gram, word, n = 50):
    for i in xrange(n):
        print word,
        # Get all possible elements ((first word, second word), frequency)
        choices = [element for element in gram if element[0][0] == word]
        if not choices:
            break
        
        # Choose a pair with weighted probability from the choice list
        word = weighted_choice(choices)[1]

def main():
    #Load cleaned corpus
    with open("/tmp/cleaned.p","rb") as f:
        main_dict = pickle.load(f)
    test1 = main_dict['text'].loc[:1000]
    
    #Build ngram dictionaries
    unigrams = build_unigrams(main_dict['text'])
    bigrams = build_bigrams(main_dict['text'])
    trigrams = build_trigrams(main_dict['text'])
    
    #Save dictionaries    
    with open("/tmp/unigrams.p","wb") as f:
        unigrams = pickle.dump(main_dict,f)
    with open("/tmp/bigrams.p","wb") as f:
        bigrams = pickle.dump(main_dict,f)
    with open("/tmp/trigrams.p","wb") as f:
        trigrams = pickle.dump(main_dict,f)
    
    #tests
    for word in ['and', 'he', 'she', 'when', 'john', 'never', 'i', 'how']:
        print "Start word: %s" % word
    
        print "3-gram sentence: \"",
        predict_sentence(trigrams,word, 20)
        print "\""
    
if __name__ = "__main__":
    main()