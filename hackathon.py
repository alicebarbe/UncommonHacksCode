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
useremotion = input("What emotion do you want? ")
usersub = {"happy":"wholesomememes+eyebleach+funny",
           "cute":"aww+kitten",
           "sad":"sadcringe+meirl",
           "educational":"todayilearned+explainlikeimfive+worldnews",
           "neutral":"mildlyinteresting+showerthoughts",
           "hacker":"ProgrammerHumor+gaming+gadgets",
           "beautiful":"earthporn+space+InternetIsBeautiful"}
if useremotion == 'sad':
    desiredSub = usersub.get('sad')
elif useremotion == 'happy':
    desiredSub = usersub.get('happy')
elif useremotion == 'cute':
    desiredSub = usersub.get('cute')
elif useremotion == 'educational':
    desiredSub = usersub.get('educational')
elif useremotion == 'neutral':
    desiredSub = usersub.get('neutral')
elif useremotion == 'hacker':
    desiredSub = usersub.get('hacker')
elif useremotion == 'beautiful':
    desiredSub = usersub.get('beautiful')
else:
    print("Your code is broken and you're dumb smh")
#now i want the length to see how long
print(len(desiredSub))
if len(desiredSub) > 0:
    print("there are multiple subs")
    #so now i want to run a for loop, adding a number until it reaches the end

#for submission in reddit.subreddit("redditdev+learnpython").top("all"):
  #  print(submission)    
subreddit = reddit.subreddit(desiredSub)
top_subreddit = subreddit.top(limit=300)
#for submission in subreddit.top(limit=1):
    #print(submission.title, submission.id)
def redditpull(subreddit):
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
    
    
    topics_data = df(topics_dict)
 
#only images specially, or imgur, or image links
#the url is the most important think
#urls = df['url']
    print(topics_data.url)
#i want to feel sad, cute, funny, happy

redditpull(usersub)

'''
saddness subs:
    eyebleach

happiness subs:
wholesomememes

cute things:
aww
Kitten

hacker:
ProgrammerHumor
    
irony
dankmemes
me_irl


'''