scrapy news pages python
=======
scrapy news pages python

##### This is an exercise to scrap RSS news with python and scale up in docker 
RSS stands for Really Simple Syndication, and it’s is a simple, standardized content distribution method that can help you stay up-to-date with your favorite newscasts, blogs, websites, and social media channels. 
Instead of visiting sites to find new posts or subscribing to sites to receive notification of new posts, [find the RSS feed on a website and read new posts](https://www.lifewire.com/find-an-rss-feed-on-a-website-3486647) in an RSS reader.  


## RSSFinder 

>RSSFinder get list or base url of site and it can find all rss links in tags ans urls in homepage 

```
from RSSFinder.RSS_Finder import RSS_Finder
RSSFinder().Find_Feeds('https://www.farsnews.ir')
```

# Docker
build images stages:
```
docker build --target pythonApp -t python/app:test .
docker build --target PG_DB -t postgres/DB:test .
```
bind database IP address


````
docker inspect {docker contaner id database} | grep IPAddress
````

