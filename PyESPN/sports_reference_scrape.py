# sports_reference_scrape #

from StringIO import StringIO
import urllib2
import pprint

import lxml.html as lh

pp = pprint.PrettyPrinter(indent=2)
url = 'http://www.basketball-reference.com/players/m/martike02/gamelog/2013/'
doc=lh.parse(urllib2.urlopen(url))

for counter, element in enumerate(doc.iter('tbody')):
    if counter == 0:
        continue
    for row in element.iter('tr'):
        try:
            int(row[0].text)
            print row[2].text_content()
        except ValueError:
            pass
