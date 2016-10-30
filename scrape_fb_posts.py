# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:56:12 2016

@author: ddan
"""
import urllib2
import json
import datetime
import csv
import time
import os.path
import fb_credentials #hidden file containing my unique app_id and secret_id

## Setting authentication variables
APP_ID = fb_credentials.set_app_id()
SECRET_ID = fb_credentials.set_secret_id()
access_token = str(APP_ID) + '|' + SECRET_ID

page_id = 'TheStraitsTimes'

def request_until_succeed(url):
  req = urllib2.Request(url)
  success = False
  while success is False:
    try:
      response = urllib2.urlopen(req)
      if response.getcode() == 200:
        success = True
    except Exception, e:
      print e
      time.sleep(5)
      print "Error for URL {}:{}".format(url,datetime.datetime.now())
  return response.read()

def unicode_normalize(text):
    return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22, 0xa0:0x20 }).encode('utf-8')

def getFacebookPageFeedData(page_id, access_token, num_statuses):
    #building url string
    base = 'https://graph.facebook.com'
    node = '/{}/feed'.format(page_id)
    parameters = '/?fields=id,message,shares&limit={}&access_token={}'.format(num_statuses, access_token)
    url = base + node +parameters
    
    #retrieve data
    data = json.loads(request_until_succeed(url))
    return data

def processFacebookPageFeedStatus(status):
    status_id = status['id']
    if 'message' not in status.keys():
        status_message = ''
    else:
        status_message = status['message'].encode('utf-8')
    return (status_id, status_message)

def scrapeFacebookPageStatus(page_id, access_token):
    base_path = '/home/ddan/Desktop/github/autocomplete/data'
    file_name = '{}_fb_posts.csv'.format(page_id)
    full_path_name = os.path.join(base_path, file_name)
    with open(full_path_name, 'wb') as file:
        w = csv.writer(file)
        w.writerow(['status_id','status_message'])
        has_next_page = True
        num_processed = 0
        scrape_start_time = datetime.datetime.now()
        
        print 'Starting to scrape {} Facebook Page : {}'.format(page_id,scrape_start_time)
        
        statuses = getFacebookPageFeedData(page_id, access_token, 100)
        
        while has_next_page:
            for status in statuses['data']:
                w.writerow(processFacebookPageFeedStatus(status))
                num_processed += 1
                if num_processed % 1000 == 0:
                    print '{} statuses processed : {}'.format(num_processed,datetime.datetime.now())
            #check if there's another page
            if 'paging' in statuses.keys():
                statuses = json.loads(request_until_succeed(statuses['paging']['next']))
            else:
                has_next_page = False
        
        print '\nDone! \n{} statuses processed in {}'.format(num_processed, datetime.datetime.now()-scrape_start_time)
  
if __name__ == '__main__':
    scrapeFacebookPageStatus(page_id,access_token)
#    test_status = getFacebookPageFeedData(page_id, access_token, 1)["data"][0]    
#    processed_test_status = processFacebookPageFeedStatus(test_status)
#    print processed_test_status
    #scrapeFacebookPageFeedComments(page_id,access_token)
