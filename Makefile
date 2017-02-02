DATA=\
	data/internal-drainage-board/internal-drainage-boards.tsv

MAPS=

LISTS=\
	lists/ada/list.tsv\
	lists/legislation/list.tsv

report.html:	bin/report.py $(LISTS) $(MAPS) $(DATA)
	python3 bin/report.py > $@
