from CLHome import CLHome


class CLSection(CLHome):
    def __init__(self, city, section):
        """
        Initiate a particular section of the craigslist website
        """
        CLHome.__init__(self, city)
        if section not in self.sections:
            raise ValueError("Section must be in: " + str(self.sections))
        self.section_ext = self.children[section]
        self.section_url = self.url_home + self.section_ext
        if self.section_ext.startswith("/i/"):
            self.section_ext = self.clarify_subsection()
            self.section_url = self.url_home + self.section_ext

    def parse_index(self):
        """
        read teh index page and get all the sections and their
        url extensions.

        :return: dict
            extensions for the index subpage
        """
        index_html = self.get_html(self.section_url)
        body = index_html.xpath('.//section[@class="body"]')[0]
        headers = [x.text + " " for x in body.xpath(".//h3")]
        sub_elements = body.xpath(".//ul")
        paths = dict()
        for i, h in enumerate(sub_elements):
            header = headers[i]
            sub_exts = {header + x.text: x.get("href") for x in h.xpath(".//a")}
            paths.update(sub_exts)
        return paths

    def clarify_subsection(self):
        """
        Get user input to see what the subsection to use if directed
        to an index.

        :return: str
            new extension for specific subcategory
        """
        paths = self.parse_index()
        path_id = {str(i): x for i,x in enumerate(paths)}
        print "Your selection had multiple subsections."
        print "Choose from the following sections by entering the corresponding number and then pressing enter.\n"
        for i in range(len(paths.keys())):
            print("{0}: {1}".format(i, path_id[str(i)]))
        id_selected = raw_input('> ')
        new_ext = paths[path_id[id_selected]]
        return new_ext

    def select_price_limits(self):
        return None

    def select_search_area(self):
        return None

    def select_pics_only(self):
        return None

    def select_title_only_search(self):
        return None

    def select_text_requirements(self):
        return None

    def select_additional_params(self):
        return None