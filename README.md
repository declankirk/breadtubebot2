# Video Essay Bot 2
Facebook/Twitter bot that generates hypothetical YouTube video essays, and posts them every hour.

Titles are generated with a Markov model, built from scraped [r/videoessay](https://www.reddit.com/r/videoessay/) submissions. Suitable thumbnails are searched for and downloaded from [shitpostbot](https://www.shitpostbot.com/). Images are drawn with PIL.

https://www.facebook.com/videoessaybot

https://twitter.com/breadtubebot

# Usage
To generate and post an image:
```
python bot.py
```
To generate a test image, without posting:
```
python bot.py -test
```
