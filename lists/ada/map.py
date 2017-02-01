#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup

soup = BeautifulSoup(sys.stdin.read(), "html.parser")
soup.prettify()

"""
				        	<div class="panel panel-primary">
					            <div class="panel-heading">
					            	<a href="http://www.ada.org.uk/members/ainsty-2008-idb/" rel="bookmark" title="Permanent Link to Ainsty (2008) IDB">
										<h2 id="post-1542" class="panel-title">
											Ainsty (2008) IDB			
										</h2>
									</a>
"""

sep='\t'
fields = ['name', 'link']

print(sep.join(fields))

for panel in soup.find_all('div', class_='panel-primary'):
    row = {}

    heading = panel.find('div', class_='panel-heading')
    if heading:

        h2 = heading.find('h2')
        row['name'] = h2.text.strip()

        a = heading.find('a')
        row['link'] = a.get('href').strip()

        print(sep.join([row[field] for field in fields]))
