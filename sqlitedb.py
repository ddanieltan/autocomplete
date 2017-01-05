# -*- coding: utf-8 -*-
import pickle
csvpath = '/home/ddan/Desktop/github/autocomplete/data/'       
trigrams=dict()
with open(csvpath+"trigrams.p","rb") as f:
    trigrams = pickle.load(f)
test1 = trigrams[:100]

import sqlite3

sqlite_file = csvpath+'trigrams.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'  # name of the table to be created
id_column = 'trigram' # name of the column
count_column = 'count'
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating table
c.execute('CREATE TABLE IF NOT EXISTS my_table_1 (w1 TEXT, w2 TEXT, w3 TEXT, count INTEGER, PRIMARY KEY (w1, w2, w3))')

# Insert data
for word, count in test1:
    c.execute('INSERT INTO my_table_1 VALUES (?, ?, ?, ?)',(word[0],word[1],word[2],count))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()


