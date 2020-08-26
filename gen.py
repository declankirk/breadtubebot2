#!/usr/bin/env python
# encoding: utf-8

import sys
import markovify
from PIL import Image, ImageDraw, ImageFont
from image_utils import ImageText
from random_username.generate import generate_username
from random import randint
import os
import re
from fetch import fetch

def model():
    with open('titles.txt', encoding='utf8') as f:
        titles = f.read()
    model = markovify.NewlineText(titles)
    return model

def gen_channel():
    username = generate_username(1)[0][:-1]
    username = username[0].upper() + username[1:]
    return username

def gen_views():
    views = randint(0, 1000000)
    views = f'{views:,}' + ' views'
    return views

def gen_time():
    mins = ('0' + str(randint(0, 59)))[-2:]
    secs = ('0' + str(randint(0, 59)))[-2:]
    time = mins + ':' + secs
    return time

def gen_img(title, channel, views, time):
    common = {'the', 'and', 'that', 'have', 'for', 'not', 'with', 'you', 'this', 'but', 
                'his', 'from', 'they', 'say', 'her', 'she', 'will', 'one', 'would', 
                'there', 'their', 'how', 'what', 'its', 'why'}
    args = []

    for word in title.lower().split(' '):
        word = re.sub(r'[^a-z0-9]', '', word)
        if (len(word) <= 2 or word in common):
            continue
        args.append(word)

    fetch(args)

    im = Image.open('thumb.jpg')
    draw = ImageDraw.Draw(im)

    im = im.convert('RGB')
    im = im.resize((640, 360))
    draw = ImageDraw.Draw(im)
    draw.rectangle([550, 310, 630, 350], fill='black')
    fnt = ImageFont.truetype('Arial Bold', 27)
    draw.text((555, 315), time, font=fnt, fill='white')

    im.save('thumb.jpg')

    im = Image.open('out.png')
    draw = ImageDraw.Draw(im)

    draw.rectangle([0, 0, 1250, 380], fill='#F1F1F1')
    draw.rectangle([10, 10, 640, 360], fill='white')
    thumb = Image.open('thumb.jpg')
    im.paste(thumb, (10, 10))

    im.save('out.png')

    txt = ImageText('out.png')
    _, y = txt.write_text_box((670, -40), title, box_width=550, font_filename='Arial',
                    font_size=55, color='black')
    txt.save('out.png')

    fnt = ImageFont.truetype('Arial', 40)
    im = Image.open('out.png')
    draw = ImageDraw.Draw(im)
    draw.text((675,y + 30), channel, font=fnt, fill='grey')
    draw.text((675,y + 85), views, font=fnt, fill='grey')

    im.save('out.png')
    print('Image generated!')