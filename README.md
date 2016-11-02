# Autocomplete
Building my own autocomplete texting app

### Aim ###
* User inputs 1 word and the app autocompletes a phrase of n words
* App is trained on corpus of colloquial Singapore English and will return uniquely Singaporean results

### 1. Data collection ###
To build a corpus of colloquial Singapore English, I will scrape popular Singaporean Facebook pages and comments using the Facebook Graph API.
* __scrape_fb_posts__ : Scrapes post_id and messages of selected Facebook pages, and saves the data in a csv (/data/{}_fb_posts.csv)
* __scrape_fb_comments__ : Scrapes comments from each post recorded in a {}_fb_post.csv, and saves the data in a csv (/data/{}_fb_comments.csv)

### 2. Data cleaning ###

### 3. Model Building ###

### 4. Deploying app ###

### 5. Reports and conclusion ###

### 6. Acknowledgements ###
