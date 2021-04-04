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
print(subreddit.display_name)
import pprint

# assume you have a Reddit instance bound to variable `reddit`
#submission = reddit.submission(id="39zje0")
#print(submission.title)  # to make it non-lazy
#pprint.pprint(vars(submission))
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
        topics_dict["subname"].append(submission.subreddit)
        global subID
        subID = topics_dict.get('subname')
        
      #  substuff = reddit.submission(id=subID)
       # print(topics_dict.get('subname'))
    topics_data = df(topics_dict)
    #prints the urls of the code
    print(topics_data.url)
    
    #this randomizes the urls that are given so users see a variety of memes
    global randomize
    randomize = topics_data.url
    random.shuffle(randomize)
   # print(topics_dict.get('subname'))
    return randomize


redditpull(usersub)
#print(randomize)
print(type(subID))
goodmeme = input("Do you like the meme? ")
memechance = 1/len(set(subID))
subnames = list(set(subID))
#print(subnames[0])

sub1 = subnames[0]
sub2 = subnames[1]
#look at the subreddit it's from
if goodmeme == 'yes':
    #which subreddit is it from
    sub1chance = memechance + 0.05
    sub2chance = memechance - 0.05
elif goodmeme == 'no':
    sub1chance = memechance - 0.05
    sub2chance = memechance + 0.05
if sub1chance > sub2chance:
    #if subID == sub1:
        #sub2 delete 5%
    print(subnames[0], "is a liked sub")
        #remove 5% of the posts from a certain sub
        
    
    

'''
https://www.reddit.com/r/flask/comments/chm0qu/have_upvotedownvotes_buttons_that_dont_reload_the/
do you like the meme? yes?
5% increase, so it shows more of the memes
so now considering the length of the distinct values
of submission subs, i should divide that by one to get 
the probability
then if something is selected, it should be rated higher, 
and the others should decrease
'''
  #  if topics_data.url in #the subrredit, so which one keeps track of the subreddit