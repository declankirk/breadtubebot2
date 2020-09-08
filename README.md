# Video Essay Bot 2
[Facebook](https://www.facebook.com/videoessaybot)/[Twitter](
https://twitter.com/breadtubebot) bot that generates hypothetical YouTube video essays, and posts them every hour. Now with over 5,000 likes!

Titles are generated with a Markov model, built from scraped [r/videoessay](https://www.reddit.com/r/videoessay/) submissions. Suitable thumbnails are searched for and downloaded from [shitpostbot](https://www.shitpostbot.com/). Images are drawn with [Pillow](https://github.com/python-pillow/Pillow).

# Examples
![ex1](/examples/ex1.png)
![ex2](/examples/ex2.png)
![ex3](/examples/ex3.png)

# Usage
To build the model:
```
python model.py
```
To generate and post an image:
```
python bot.py
```
To generate a test image, without posting:
```
python bot.py -test
```
