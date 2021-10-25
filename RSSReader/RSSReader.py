
import requests
from bs4 import BeautifulSoup


class RSSReader():

    def RSS_TO_Dict(self ,rss):
        article_list = []
        for a in rss:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            article = {
                'title': title,
                'link': link,
                'published': published
            }
            article_list.append(article)

        return article_list

    def Read_RSS(self ,rss):
        try:
            r = requests.get(rss)
            soup = BeautifulSoup(r.content, features='xml')
            articles = soup.findAll('item')
            if articles:
                self.RSS_TO_Dict(articles)

        except ConnectionError as conn:
            print(conn)


