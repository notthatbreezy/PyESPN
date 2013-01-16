## Class for gathering data on players ##

import urllib
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)


class PyESPN():
    """Main class for accessing ESPN API

    Contains methods for accessing:
        - List of sports
    """

    def __init__(self, API_KEY):
        self.url_params = '?' + urllib.urlencode({'apikey': API_KEY})
        self.main_url = 'http://api.espn.com/v1/sports'

    def sports(self):
        """Get list of sports"""
        response = urllib.urlopen(self.main_url + self.url_params)
        raw_dict = json.loads(response.read())
        self.status = raw_dict['status']
        self.sport_list = raw_dict['sports']

    def nba_player(self, player_id):
        """Get information on specific NBA player"""
        built_url = self.main_url + '/basketball/nba/athletes/%s/salary' % (player_id) + self.url_params
        print built_url
        self.player_data = json.loads(urllib.urlopen(built_url).read())

if __name__ == '__main__':
    from login_data import *
    s = PyESPN(API_KEY)
    # s.sports()
    s.nba_player('2394')
    # pp.pprint(s.sport_list[0])
    pp.pprint(s.player_data)
