from collections import defaultdict

class SearchString:
    """
    Give a set of search parameters build the query string to pull up the
    appropriate results from craigslist.
    """

    def __init__(self, **kwargs):
        search_parmas = defaultdict(lambda: None)
        search_parmas.update(kwargs)
        self.query = "?"
        self.query_str(query=search_parmas["query"])
        self.price_limits(min_price=search_parmas["min_price"], max_price=search_parmas["max_price"])
        self.distance_from_zip(zipcode=search_parmas["zipcode"], miles=search_parmas["miles"])
        self.search_titles_only(title_only=search_parmas["title_only"])
        self.has_image(image=search_parmas["image"])
        self.posted_today(today=search_parmas["today"])
        self.include_nearby_areas(nearby=search_parmas["nearby"])

    def price_limits(self, min_price=None, max_price=None):
        """
        Set the price limits of a CL search

        :param min_price: int or float
            value to be used as the minimum price for any search. Values
            given will be rounded to an int
        :param max_price: int or float
            value to be used as the maximum price for any search. Values
            given will be rounded to an int
        """
        if min_price is None and max_price is None:
            return
        price_list = []
        if min_price is not None:
            price_list.append("min_price={}".format(int(min_price)))
        if max_price is not None:
            price_list.append("max_price={}".format(int(max_price)))
        self.query = "&".join([self.query] + price_list)

    def distance_from_zip(self, zipcode=None, miles=None):
        """
        The maximum distance from a zip code to search for results.

        :param zipcode: int
            zipcode to be the base of the search
        :param miles: int or float
            maximum number of miles to search from zipcode center. Values
            given will be rounded to an int
        """
        if zipcode is None or miles is None:
            return
        dis_str = "search_distance={m}&postal={z}"
        dis_str = dis_str.format(m=int(miles), z=zipcode)
        self.query = "&".join([self.query, dis_str])

    def search_titles_only(self, title_only=None):
        """
        Indicate wether to only look at the title for the string query

        :param title_only: bool, optional
            whether to search only in the titles
        """
        if title_only is None:
            return
        bool_str = "T" if title_only else "F"
        search_title_str = "srchType={}".format(bool_str)
        self.query = "&".join([self.query, search_title_str])

    def has_image(self, image=None):
        """
        Indicate wether you require an image be in the posting for results.

        :param image: bool, optional
            whether to search only in the titles
        """
        if image is None:
            return
        bool_str = "1" if image else "0"
        has_image_str = "hasPic={}".format(bool_str)
        self.query = "&".join([self.query, has_image_str])

    def posted_today(self, today=None):
        """
        Indicate wether you require results be posted from today.

        :param today: bool, optional
            whether to require post results be from today
        """
        if today is None:
            return
        bool_str = "1" if today else "0"
        posted_today_str = "postedToday={}".format(bool_str)
        self.query = "&".join([self.query, posted_today_str])

    def include_nearby_areas(self, nearby=None):
        """
        Indicate wether you want to also search in adjacent areas.

        :param nearby: bool, optional
            whether to search adjacent ares
        """
        if nearby is None:
            return
        bool_str = "1" if nearby else "0"
        include_nearby_areas_str = "searchNearby={}".format(bool_str)
        self.query = "&".join([self.query, include_nearby_areas_str])

    def query_str(self, query=None):
        """
        The string to use in order to search for results. Though the paramter
        is optional it is highly reccomended in order to limit results.

        :param query: str, optional
            The query you would like to use to limit results
        """
        if query is None:
            return
        query_str = "query=" + query.replace(" ", "+")
        self.query = "".join([self.query, query_str])
