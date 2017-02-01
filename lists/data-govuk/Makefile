URL='http://data.defra.gov.uk/FloodRisk/IDB_list_updates_Oct_16.csv'

list.tsv:	data.csv map.py
	python3 map.py < data.csv > $@

data.csv:
	curl -s $(URL) > $@

clean:
	rm -f data.html list.tsv

init:
