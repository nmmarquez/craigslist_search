from SearchString import SearchString
import pandas as pd
import requests
from lxml import html

class CLSection(SearchString):
    """
    Get the results from a query store the data in a pandas data frame.
    """

    def __init__(self, url, **kwargs):
        """
        Initiate a particular section of the craigslist website
        """
        SearchString.__init__(self, **kwargs)
        self.base_url = url
        self.full_url = self.base_url + self.query

    @staticmethod
    def getHTML(url):
        f = requests.get(url)
        return html.fromstring(f.text)

    # def pull_html()
