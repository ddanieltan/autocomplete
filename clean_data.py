# -*- coding: utf-8 -*-
import pandas as pd
import sys
from HTMLParser import HTMLParser
from nltk.tokenize import word_tokenize
import re
import pickle

## thanks to shahram
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

#Globals
html_parser = HTMLParser()
APOSTROPHES = {
    "'s" : " is", 
    "'re" : " are",
    "'t" : " not",
    "'ve" : " have",
    "'d" : " would",
    "'ll" : " will",
    "'m" : " am"
    }

def remove_urls(text):
    text = html_parser.unescape(text) #remove HTML artifacts e &amp
    return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)

def replace_apostrophes(text):
    pattern = re.compile(r'\b(' + '|'.join(APOSTROPHES.keys()) + r')\b')
    return pattern.sub(lambda x: APOSTROPHES[x.group()], text)
    
def remove_punctuation_digits(input_text):
    cleaned = input_text.lower()
    cleaned = re.sub('["#$%&\()*+,/:;<=>@[\\]^-_`{|}~]', '', cleaned)
    cleaned = re.sub(' [^ai1234567890][ |\.]', ' ', cleaned)
    cleaned = re.sub('[1234567890]+\.[1234567890]+', '', cleaned)
    cleaned = re.sub('[1234567890]+', '', cleaned)
    cleaned = re.sub('\r\n', '', cleaned)
    cleaned = re.sub('\s+', ' ', cleaned)
    cleaned = re.sub('[!?]', '', cleaned)
    cleaned = re.sub(' \.', '', cleaned)
    cleaned = re.sub('\.+', '', cleaned)
    cleaned = re.sub('\'\'','', cleaned)
    cleaned = re.sub('nan','',cleaned)
    return cleaned

def clean_text(sentence):
    answer = sentence.decode('utf8','ignore')
    answer = sentence.encode('ascii','ignore').lower()
    answer = remove_urls(answer)
    answer = replace_apostrophes(answer)
    answer = remove_punctuation_digits(answer)
    answer = word_tokenize(answer)
    answer = filter(None,answer) #removing blank elements
    return answer

def main():
    #Retrieve main_dict
    csvpath = '/home/ddan/Desktop/github/autocomplete/main_dict.csv'
    main_dict = pd.read_csv(csvpath, encoding='utf-8')
    main_dict['text'] = main_dict['text'].astype(str)
    
    main_dict['text'] = main_dict['text'].apply(clean_text)
    main_dict = main_dict
    
    #Saving cleaned dataframe as a pickle
    with open("/tmp/cleaned.p","wb") as f:
        pickle.dump(main_dict,f)

if __name__ == "__main__":
    main()




