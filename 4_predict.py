# -*- coding: utf-8 -*-
import cPickle as pickle
import time
import random

def weighted_choice(choices):
   total = sum(weight for choice, weight in choices)
   r = random.uniform(0, total)
   upto = 0
   for choice, weight in choices:
      if upto + weight > r:
         return choice
      upto += weight

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
    #Load Language Model    
    start = time.time()    
    print 'Loading language model...'
    csvpath = '/home/ddan/Desktop/github/autocomplete/data/'       
    trigrams=dict()
    with open(csvpath+"trigrams.p","rb") as f:
        trigrams = pickle.load(f)
    print 'Model loaded in {} seconds'.format(time.time()-start)
    
    #To test 1 word at a time
    while True:    
        start_word = raw_input('\nEnter your starting word: ')
        predict_sentence(trigrams,start_word,20)    
    
    #To test multiple words
#    for word in ['and', 'he', 'she', 'when', 'what', 'never', 'i', 'how']:
#        print "Start word: %s" % word
#        print "3-gram sentence: \"",
#        predict_sentence(trigrams,word, 20)
#        print "\""

if __name__ == "__main__":
    main()
    

