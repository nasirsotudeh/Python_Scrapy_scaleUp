scrapy news pages python
=======
scrapy news pages python

##### This is an exercise to scrap RSS news with python and scale up in docker 
RSS stands for Really Simple Syndication, and it’s is a simple, standardized content distribution method that can help you stay up-to-date with your favorite newscasts, blogs, websites, and social media channels. 
Instead of visiting sites to find new posts or subscribing to sites to receive notification of new posts, [find the RSS feed on a website and read new posts](https://www.lifewire.com/find-an-rss-feed-on-a-website-3486647) in an RSS reader.  


## RSSFinder 

>RSSFinder get list or base url of site and it can find all rss links in tags and urls in homepage 

```
from RSSFinder.RSS_Finder import RSS_Finder
RSSFinder().Find_Feeds('https://www.farsnews.ir')
```

# Docker
### docker-compose:
run 
```` 
docker-compose up
````
contain networks app-tier to create bridge and static IPv4 with subnet
```
    ipam:
      config:
        - subnet: 172.23.0.2/24
```
services database build Image Dockerfile from ./Database with static IPv.
```
networks:
      app-tier:
          ipv4_address: 172.23.0.2
```
we set database environment in docker-compose.yml to create user .
Dockerfile from ./Database create tables automaticly from /docker-entrypoint-initdb.d
`COPY ./sql/*.sql /docker-entrypoint-initdb.d/`



build images stages:
```
docker build --target pythonApp -t python/app:test .
cd Database/ && docker build --target PG_DB -t postgres/db:test .
```
bind database IP address
````
docker inspect {docker contaner id database} | grep IPAddress
````

