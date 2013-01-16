## Class for gathering data on players ##

import urllib
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


class PyESPN():
    """Main class for accessing ESPN API

    Contains methods for accessing:
        - List of sports
    """

    def __init__(self, API_KEY):
        self.url_params = {'apikey': API_KEY}
        self.main_url = 'http://api.espn.com/v1/sports?'

    def sports(self):
        """Get list of sports"""
        page = urllib.urlopen(self.main_url + urllib.urlencode(self.url_params))
        raw_dict = json.loads(page.read())
        self.status = raw_dict['status']
        self.sport_list = raw_dict['sports']

if __name__ == '__main__':
    from login_data import *
    s = PyESPN(API_KEY)
    s.sports()
    pp.pprint(s.sport_list[0])
