# see: https://www.gov.uk/government/publications/public-sector-organisations-eligible-to-use-cloudstore
URL='https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/254525/CloudStore_eligible_public_sector_bodies__1_.pdf'

# uses https://en.wikipedia.org/wiki/Pdftotext which is bundled with poppler https://en.wikipedia.org/wiki/Poppler_(software)

list.tsv:	data.txt map.py
	./map.py < data.txt > $@

data.txt:	data.pdf
	pdftotext -layout data.pdf $@

data.pdf:
	curl -s $(URL) > $@

clean:
	rm -f data.pdf data.txt list.tsv
