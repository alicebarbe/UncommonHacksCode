# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:10:46 2021
"""

from praw import Reddit
from datetime import datetime
from pprint import pprint
from pandas import DataFrame as df
import random
import praw

#this is the reddit api information
reddit = praw.Reddit(client_id="V_XJ0VQSyC9WyQ",      # your client id
                     client_secret="fUsEC3A9CLn1A7dygqiJB16kGBfCfw",  #your client secret
                     user_agent="my user agent", #user agent name
                     username = "TheLinkWithin",     # your reddit username
                     password = "summerfood26!")     # your reddit password
#this input gets the emotion the user wants
useremotion = input("What emotion do you want? ")
#dictionary of subs that will give users the sub stuff depending on what they would like to see
usersub = {"happy":"wholesomememes+eyebleach+funny",
           "cute":"aww+kitten",
           "sad":"sadcringe+meirl",
           "educational":"todayilearned+explainlikeimfive+worldnews",
           "neutral":"mildlyinteresting+showerthoughts",
           "hacker":"ProgrammerHumor+gaming+gadgets",
           "beautiful":"earthporn+space+InternetIsBeautiful"}
#dictates the emotion that users want
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

#the desired sub that i want    
subreddit = reddit.subreddit(desiredSub)
#queries 300 posts from the sub
top_subreddit = subreddit.top(limit=300)
#this function gives us our information into a neat little dataframe
def redditpull(subreddit):
    topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[],
                "subname":[]}
    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
        topics_dict["subname"].append(reddit.subreddit(desiredSub))
        
    topics_data = df(topics_dict)
    #prints the urls of the code
    print(topics_data.url)
    #this randomizes the urls that are given so users see a variety of memes
    global randomize
    randomize = topics_data.url
    random.shuffle(randomize)
    print(topics_dict.get('subname'))
    return randomize


redditpull(usersub)
#print(randomize)
print(usersub.get('sad'))
if '+' in usersub.get('sad'):
    print("it has that")
  #  if topics_data.url in #the subrredit, so which one keeps track of the subreddit