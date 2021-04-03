# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:10:46 2021
"""

from praw import Reddit
from datetime import datetime
from pprint import pprint
from pandas import DataFrame as df
import praw

#from myKeys import keys
reddit = praw.Reddit(client_id="V_XJ0VQSyC9WyQ",      # your client id
                     client_secret="fUsEC3A9CLn1A7dygqiJB16kGBfCfw",  #your client secret
                     user_agent="my user agent", #user agent name
                     username = "TheLinkWithin",     # your reddit username
                     password = "summerfood26!")     # your reddit password
#print(reddit.read_only)
#only image posts
subreddit = reddit.subreddit('Eyebleach')
top_subreddit = subreddit.top()
for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)
topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[]}
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    print(top_subreddit.url)
    
topics_data = df(topics_dict)
 
#only images specially, or imgur, or image links
#the url is the most important think
#urls = df['url']
print(topics_data.url)
#i want to feel sad, cute, funny, happy



#sadness
#happi
#https://www.reddit.com/r/wholesomememes/