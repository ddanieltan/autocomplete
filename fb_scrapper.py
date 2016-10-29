# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:00:44 2016

@author: ddan
"""
import json
import urllib2
import fb_credentials #hidden file containing my unique app_id and secret_id



def create_post_url(graph_url, APP_ID, SECRET_ID):
  #method to return 
  post_args = "/posts/?key=value&access_token=" + str(APP_ID) + "|" + SECRET_ID
  post_url = graph_url + post_args
  return post_url

def render_to_json(graph_url):
  #render graph url call to JSON
  web_response = urllib2.urlopen(graph_url)
  readable_page = web_response.read()
  json_data = json.loads(readable_page)	
  return json_data

def main():

  ## Setting authentication variables
  APP_ID = fb_credentials.set_app_id()
  SECRET_ID = fb_credentials.set_secret_id()

  #to find go to page's FB page, at the end of URL find username
  #e.g. http://facebook.com/walmart, walmart is the username
  #list_companies = ["walmart", "cisco", "pepsi", "facebook"]
  graph_url = "https://graph.facebook.com/"
    
  current_page = graph_url+'TheStraitsTimes'
  #extract post data
  post_url = create_post_url(current_page, APP_ID, SECRET_ID)
  json_postdata = render_to_json(post_url)
  json_fbposts = json_postdata['data']

  #print json_fbposts
  for post in json_fbposts:
    try:
      print post['id']
      print post['message']
    except Exception:
      print 'Error'
    
if __name__ == '__main__':
    main()

