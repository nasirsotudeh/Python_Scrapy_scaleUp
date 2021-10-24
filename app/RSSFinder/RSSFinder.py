from bs4 import BeautifulSoup as bs4
import requests
import feedparser
import requests
import feedparser
import urllib.parse
from requests import HTTPError, ConnectionError


class RSSFinder():

    def Process_Feed_URL(self, feed_urls):
        """

        :param feed_urls: List of URls base site
        :return: list of objects contain rss url and title of rss maybe category's of news
        """
        Valid_feeds = []
        Data = {}
        if len(feed_urls) > 1:
            for feed_url in feed_urls:
                Application_Type = feed_url.get("type", None)
                if Application_Type:
                    if "rss" in Application_Type or "xml" in Application_Type:
                        href = feed_url.get("href", None)
                        URL_Titel = feed_url.get("title", None)
                        item = (href, URL_Titel)
                        Valid_feeds.append(item)
        return Valid_feeds

    def Process_IN_Tags(self, HTML, URL):
        """

        :param HTML: HTML of base site to scrap tags
        :param URL: get base url to attach href of rss
        :return:  list of objects contain rss url and title of rss maybe category's of news
        """
        Valid_Feeds = []
        Tags = HTML.findAll("a")
        for Tag in Tags:
            href = Tag.get("href", None)
            if href:
                if "xml" in href or "rss" in href or "feed" in href:
                    Valid_Feeds.append(URL + href)
                    Rss_URL = URL + href
                    URL_Titel = Tag.get("title", None)
                    item = (Rss_URL, URL_Titel)
                    Valid_Feeds.append(item)
            return Valid_Feeds

    def Extract_URLs(self, site):
        """

        :rtype: get base url to attach scheme
        """
        URL_Extract = urllib.parse.urlparse(site)
        URL_Parsed = URL_Extract.scheme + "://" + URL_Extract.hostname
        return URL_Parsed

    def Find_Feeds(self, site):
        """

        :rtype: get base url to get html content and scrap rss in links and tags
                contain Error handling in send requests
        """
        URL_Parsed = self.Extract_URLs(site)
        try:
            raw = requests.get(site).text
            html = bs4(raw)
        except Exception:
            print(Exception)

        Alternate_urls = html.findAll("link", rel="alternate")

        try:
            Valid_Feeds = (self.Process_Feed_URL(Alternate_urls) + self.Process_IN_Tags(html, URL_Parsed))

        except Exception:
            print(Exception)

        return Valid_Feeds
