# Note, this data is © 2014-2017 Association of Drainage Authorities
URL='http://www.ada.org.uk/member_type/idbs/'

list.tsv:	data.html map.py
	python3 map.py < data.html > $@

data.html:
	curl -s $(URL) > $@

clean:
	rm -f data.html list.tsv

init:
	pip install -r requirements.txt
