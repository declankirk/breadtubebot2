from gen import model, gen_channel, gen_img, gen_time, gen_views
import facebook
from datetime import datetime, date
from config import access_token
import schedule
import time
import sys

m = model()
graph = facebook.GraphAPI(access_token)

def job(post):
    title = m.make_short_sentence(50, tries=100)
    channel = gen_channel()
    views = gen_views()
    time = gen_time()

    caption = title + ' [' + time + '] by ' + channel + ' (' + views + ')'
    print(caption)

    gen_img(title, channel, views, time)
    
    if (not post):
        return

    post_id = graph.put_photo(image = open('out.png', 'rb'), message='Up next:')['post_id']

    now = datetime.now()
    today = datetime.today()
    current_time = now.strftime('%H:%M:%S')
    current_date = today.strftime('%d/%m/%Y')

    print('Posted to Facebook: ' + post_id + ' at ' + current_time + ' ' + current_date)
    print()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Starting scheduling...')
        print()
        schedule.every(3).hours.do(lambda: job(True)).run()
        while True:
            schedule.run_pending()
            time.sleep(1)
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
        sys.exit (1)