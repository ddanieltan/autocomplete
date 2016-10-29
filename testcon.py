# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:25:15 2016

@author: ddan
"""

import psycopg2
import sys

con = None

try:
     
    con = psycopg2.connect(database='testdb', user='ddan', host='localhost', password='123') 
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print ver    
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()