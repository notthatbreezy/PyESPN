## Class for gathering data on players ##

import urllib
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

main_url = 'http://api.espn.com/v1/sports?'


class PyESPN():
    """Main class for accessing ESPN API

    Contains methods for accessing:
        - List of sports
    """

    def __init__(self, main_url, API_KEY):
        self.url_params = {'apikey': API_KEY}
        self.main_url = main_url

    def sports(self):
        """Get list of sports"""
        page = urllib.urlopen(main_url + urllib.urlencode(self.url_params))
        self.sports = json.dumps(page.read())
