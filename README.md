# Autocomplete
Building my own autocomplete texting app

### Aim ###
* User inputs 1 word and the app autocompletes a phrase of n words
* App is trained on corpus of postsand comments from Singaporean Facebook pages, and should return uniquely Singaporean results

### 1. Data collection ###
To build a corpus of colloquial Singapore English, I will scrape popular Singaporean Facebook pages and comments using the Facebook Graph API.
* __1a_scrape_fb_posts.py__ : Scrapes post_id and messages of selected Facebook pages, and saves the data in a csv (/data/{}_fb_posts.csv)
* __1b_scrape_fb_comments.py__ : Scrapes comments from each post recorded in a {}_fb_post.csv, and saves the data in a csv (/data/{}_fb_comments.csv)
* __shortlisted_fb_pages.txt__ : Text file with shortlisted Facebook pages based on highest audience

### 2. Data cleaning ###
__2_clean_data.py__ :
* Remove erroneous data
* Decode and remove non-ASCII characters
* Expand apostrophes
* Remove punctuation
* Tokenize words

### 3. Building a Language Model ###
__3_build_model.py__ :
* Build unigram, bigram and trigrams frequency distribution
* Pickle trigrams language model

### 4. Running predictions ###
__4_predict.py__ :
* Load trigrams language model
* Build a predictor based on weighted probabilities of ngram model
* Run app to take user input for the starting word

### 5. Reports ###
Please see my slide presentation [here](https://docs.google.com/presentation/d/1u8lsHsNEAGSwKHDGRSL8axjc1SddkoovV3giyzvpUvU/edit?usp=sharing)
