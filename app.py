# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:48:25 2021

@author: Alice
"""

from praw import Reddit
from datetime import datetime
from pprint import pprint
import pandas as pd
import praw
from flask import Flask, jsonify, request, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'name':'eyebleach'}, {'name':'Me_irl'}, {'name':'wholesomememes'}])

#@app.route("/test" , methods=['GET', 'POST'])
#def test():
#    select = request.form.get('comp_select')
#    return(str(select)) # just to see what select is

@app.route('/memes', methods=['GET', 'POST'])
def memes():
    subreddit_name = request.form.get('comp_select')
    #from myKeys import keys
    reddit = praw.Reddit(client_id="V_XJ0VQSyC9WyQ",      # your client id
                         client_secret="fUsEC3A9CLn1A7dygqiJB16kGBfCfw",  #your client secret
                         user_agent="my user agent", #user agent name
                         username = "TheLinkWithin",     # your reddit username
                         password = "summerfood26!")     # your reddit password
    #only image posts
    #subreddit = reddit.subreddit('Eyebleach')
    subreddit = reddit.subreddit(subreddit_name)
    top_subreddit = subreddit.top()
    print(top_subreddit)
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
        
    topics_data = pd.DataFrame(topics_dict)
    #topics_data = topics_data[0:30] # temporarily reduce number of rows
    topics_data['url_corrected'] = topics_data['url'].map(checkValidMeme)
    topics_data = topics_data.dropna(subset=['url_corrected'])
    embed_list = list(topics_data['url_corrected'])
    return render_template('memes.html', embed=embed_list)

# this runs slowly because of all the internet queries, but it checks for valid URL
def checkValidMeme2(url):
    # check if image format
    image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif", 'video/mp4')
    r = requests.head(url)
    if 200 <= requests.head(url).status_code < 300: # check if valid
        if r.headers["content-type"] in image_formats:
            #print(url)
            return url
        else:
            if url[-5:] == '.gifv':
                url = url.replace('.gifv', '.mp4')
                if requests.head(url).headers["content-type"] in image_formats:
                    print("conversion happening")
                    return url
                else:
                    print("error2: " + url)
    else:
        print("error: " + url)
    return None

def checkValidMeme(url):
    image_formats = ['.jpg', '.jpeg.', '.png', '.gif', '.mp4']
    if url[-5:] == '.gifv':
        url = url.replace('.gifv', '.mp4')
    if any(image_format in url for image_format in image_formats):
        return url
    else:
        return None


if __name__ == '__main__':
    app.debug = True
    app.run()