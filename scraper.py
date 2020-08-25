#!/usr/bin/env python
# encoding: utf-8

import sys
import re
from psaw import PushshiftAPI

api = PushshiftAPI()

def scrape(num):
    f = open("titles.txt","wb")
    gen = api.search_submissions(subreddit='videoessay', limit=num)
    posts = list(gen)

    for submission in posts:
        s = submission.title
        s = re.sub(r" *\[[^\]]*\]:* *", "", s) # removing all tags and trailing whitespace
        s = re.sub(r"&gt;", ">", s)
        s = re.sub(r"&lt;", "<", s)
        s = re.sub(r"&amp;", "&", s)
        s = re.sub(r"(OC)", "", s)
        s = re.sub(r"(Found)", "", s)
        if s == '':
            continue
        s += '\n'
        f.write(s.encode("utf-8"))

scrape(500000)