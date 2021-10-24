scrapy news pages python
=======
scrapy news pages python

This is an exercise to scrap RSS news with python and scale up in docker 
 

build images stages:
```
docker build --target pythonApp -t python/app:test .
docker build --target PG_DB -t postgres/DB:test .
```
bind database IP address


````
docker inspect {docker contaner id database} | grep IPAddress
````

