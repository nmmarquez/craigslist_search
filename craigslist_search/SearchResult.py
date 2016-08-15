import pandas as pd
import requests
from lxml import html

class SearchResult:
    """
    Parse the results of a craigslist query for an individual page.
    """

    def __init__(self, url):
        self.url = url
        self.html_tree = self.getHTML(url)
        self.price = self.html_tree.xpath("//span[@class='price']")[0].text
        title_list = self.html_tree.xpath("//span[@class='postingtitletext']")[0].getchildren()
        self.title = " ".join([x.text for x in title_list]).replace("\n", "")
        pic_list = self.html_tree.xpath("//img")
        self.pic_url = pic_list[0].attrib.get("src") if len(pic_list) > 0 else None
        self.description = " ".join(self.html_tree.xpath("//section[@id='postingbody']/text()"))

    @staticmethod
    def getHTML(url):
        f = requests.get(url)
        return html.fromstring(f.text)
