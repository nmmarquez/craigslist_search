import requests
from lxml import html


class CLHome:
    def __init__(self, city):
        """
        Create

        :param city: str
            The city that you would like to search
        """
        self.url_home = "https://{}.craigslist.org".format(city)
        self.children = self.children_extensions()
        self.sections = self.children.keys()

    @staticmethod
    def get_html(url):
        """
        Retrieves the html for a particular url

        :param url:
        :return:
        """
        f = requests.get(url)
        return html.fromstring(f.text)

    def html_home(self):
        """
        Retrieve the home html.

        :return: html object
            home craigslist html
        """

        return self.get_html(url=self.url_home)

    def children_extensions(self):
        """
        Get all the for sale children url extensions

        :return: dict
            all the for sale pages that exist for a cities CL page
        """
        sss = self.html_home().xpath('//div[@id="sss"]')[0]
        list_elements = sss.xpath(".//li")
        paths = dict()
        for l in list_elements:
            row_element = l.xpath(".//a")[0]
            url_ext = row_element.get("href")
            section = row_element.xpath(".//span")[0].text
            paths[section] = url_ext
        return paths
