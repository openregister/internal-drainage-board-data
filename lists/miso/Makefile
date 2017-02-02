# see: https://www.gov.uk/guidance/current-crown-commercial-service-suppliers-what-you-need-to-know
URL=https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/549702/2016-09-01_customer_URN_list.xlsx

list.tsv:	data.xlsx map.py
	map.py data.xlsx > $@

data.xlsx:
	curl -s $(URL) > $@

clean:
	rm -f data.xlsx list.tsv

init:
	pip install -r requirements.txt
