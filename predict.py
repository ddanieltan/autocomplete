# -*- coding: utf-8 -*-
import pickle
import time



def main():
    start = time.time()    
    print 'Loading language model...'
    with open("/tmp/unigrams.p","rb") as f:
        unigrams = pickle.load(f)
    with open("/tmp/bigrams.p","rb") as f:
        bigrams = pickle.load(f)
    with open("/tmp/trigrams.p","rb") as f:
        trigrams = pickle.load(f)
    print 'Language model loaded. Time taken: {} seconds'.format(time.time()-start)

if __name__ == "__main__":
    main()
    

