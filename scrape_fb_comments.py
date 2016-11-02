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
access_token = APP_ID + '|' + SECRET_ID

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
      #print "Error for URL {}:{}".format(url,datetime.datetime.now())
  return response.read()

def unicode_normalize(text):
    return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22, 0xa0:0x20 }).encode('utf-8')

def getFacebookCommentFeedData(status_id, access_token, num_comments):
  #constructing url request
  base = 'https://graph.facebook.com/v2.6'
  node = '/{}/comments'.format(status_id)
  fields = '?fields=id,message,like_count,created_time,comments,from'
  parameters = '&order=chronological&limit={}&access_token={}'.format(num_comments, access_token)
  url = base + node + fields + parameters
  
  #retrieve data
  data = request_until_succeed(url)
  if data is None:
    return None
  else:
    return json.loads(data)


def processFacebookComment(comment, status_id, parent_id=''):
  comment_id = comment['id']
  if 'message' not in comment:
      comment_message = ''
  else:
      comment_message = unicode_normalize(comment['message'])
  comment_author = unicode_normalize(comment['from']['name'])
  if 'like_count' not in comment:
      comment_likes = 0
  else:
      comment_likes = comment['like_count']
  comment_published = datetime.datetime.strptime(comment['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
  comment_published = comment_published.strftime('%Y-%m-%d %H:%M:%S')  
  return (comment_id, comment_message, comment_author, comment_likes, comment_published)

def scrapeFacebookPageFeedComments(page_id, access_token):
    #writing data to csv
    base_path = '/home/ddan/Desktop/github/autocomplete/data'
    file_name = '{}_fb_comments.csv'.format(page_id)
    full_path_name = os.path.join(base_path, file_name)
    with open(full_path_name, 'wb') as file:
        w = csv.writer(file)
        # Headers
        w.writerow(['comment_id', 'comment_message', 'comment_author', 'comment_likes', 'comment_published'])
        
        num_processed = 0
        scrape_starttime = datetime.datetime.now()
        print 'Scraping {} comments from posts: {}\n'.format(page_id, scrape_starttime)
        
        
        post_file_name = os.path.join(base_path, '{}_fb_posts.csv'.format(page_id))
        with open(post_file_name, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for status in reader:
                has_next_page = True
                comments = getFacebookCommentFeedData(status['status_id'], access_token, 100)
                
                while has_next_page and comments is not None:
                    for comment in comments['data']:
                        w.writerow(processFacebookComment(comment, status['status_id']))
                        if 'comments' in comment:
                            has_next_subpage = True
                            subcomments = getFacebookCommentFeedData(comment['id'], access_token, 100)
                            while has_next_subpage:
                                for subcomment in subcomments['data']:
                                    w.writerow(processFacebookComment(subcomment, status['status_id'], comment['id']))
                                    num_processed += 1
                                    if num_processed % 500 == 0:
                                        print '\n{}-{} subcomments processed : {}\n'.format(page_id, num_processed, datetime.datetime.now())
                                if 'paging' in subcomments:
                                    if 'next' in subcomments['paging']:
                                        subcomments = json.loads(request_until_succeed(subcomments['paging']['next']))
                                    else:
                                        has_next_subpage = False
                                else:
                                    has_next_subpage = False
                        num_processed += 1
                        if num_processed % 500 == 0:
                            print '\n{}-{} comments processed : {}\n'.format(page_id, num_processed, datetime.datetime.now())
                    if 'paging' in comments:
                        if 'next' in comments['paging']:
                            comments = json.loads(request_until_succeed(comments['paging']['next']))
                        else:
                            has_next_page = False
                    else:
                        has_next_page = False
        print '\nDone! \n{} comments processed in {}'.format(num_processed, datetime.datetime.now()-scrape_starttime)

if __name__ == '__main__':
    page_ids = ['nlbsg']
    for page_id in page_ids:
        scrapeFacebookPageFeedComments(page_id,access_token)
