from gen import model, gen_channel, gen_img, gen_time, gen_views
import facebook
from datetime import datetime, date, timedelta
from config import fb_access_token, consumer_key, consumer_secret, access_key, access_secret
import time
import sys
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

m = model()

graph = facebook.GraphAPI(fb_access_token)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def job(post):
    title = m.make_short_sentence(50, tries=100)
    channel = gen_channel()
    views = gen_views()
    time = gen_time()

    print(title + ' [' + time + '] by ' + channel + ' (' + views + ')')
    caption = title + ' | ' + channel + '\n' + views

    gen_img(title, channel, views, time)
    
    if (not post):
        return

    fb_post_id = graph.put_photo(image = open('out.png', 'rb'), message='Up next:')['post_id']
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.today().strftime('%d/%m/%Y')
    print('Posted to Facebook: ' + fb_post_id + ' at ' + current_time + ' ' + current_date)

    tw_post_id = str(api.update_with_media('thumb.jpg', status=caption).id)
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.today().strftime('%d/%m/%Y')
    print('Posted to Twitter: ' + tw_post_id + ' at ' + current_time + ' ' + current_date)
    
    print()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Starting scheduling...')
        print()
        sched.add_job(lambda: job(True), 'cron', minute=0)
        sched.start()
    elif sys.argv[1] == '-m':
        print('Manually generating and posting image...')
        print()
        job(True)
    elif sys.argv[1] == '-t':
        print('Generating test image...')
        print()
        job(False)
    else:
        print('Usage: python bot.py [-m|-t]')
        sys.exit(1)