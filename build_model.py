# -*- coding: utf-8 -*-

import pickle
from collections import Counter, OrderedDict
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist, ConditionalFreqDist, ConditionalProbDist, LaplaceProbDist

#Load cleaned corpus
main_dict = pickle.load(open("/tmp/cleaned.p", "rb"))
test1 = main_dict['text'].loc[:25]

unigram_fd = FreqDist()
bigram_cfd = ConditionalFreqDist()
trigram_cfd = ConditionalFreqDist()
quadgram_cfd = ConditionalFreqDist()

unigram_pd = None
bigram_cpd = None
trigram_cpd = None
quadgram_cpd = None

prev_word = None
prev_2_word = None
prev_3_word = None

for sentence in test1:
    for word in sentence:
        if word.isalpha():
            unigram_fd[word] += 1
            bigram_cfd[prev_word][word] += 1
            trigram_cfd[tuple([prev_2_word, prev_word])][word] += 1
            quadgram_cfd[tuple([prev_3_word, prev_2_word, prev_word])][word] += 1
            prev_3_word = prev_2_word
            prev_2_word = prev_word
            prev_word = word

unigram_pd = LaplaceProbDist(unigram_fd, bins=unigram_fd.N())
bigram_cpd = ConditionalProbDist(bigram_cfd, LaplaceProbDist, bins=len(bigram_cfd.conditions()))
trigram_cpd = ConditionalProbDist(trigram_cfd, LaplaceProbDist, bins=len(trigram_cfd.conditions()))
quadgram_cpd = ConditionalProbDist(quadgram_cfd, LaplaceProbDist, bins=len(quadgram_cfd.conditions()))

def next_word(text):
    context = word_tokenize(text)
    last_word = context[-1] ### Stuck handling words that are not in the corpus
    if last_word in unigram    
    word = bigram_cfd[context[-2:]].max()
    return word

aa = "This is a funny"
next_word(aa)
