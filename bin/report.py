#!/usr/bin/env python3

import csv

register_path = 'data/internal-drainage-board/internal-drainage-boards.tsv'
legislation_path = 'lists/legislation/list.tsv'


def legislation_url(legislation):
    slug = legislation.replace('-', '/')
    return "http://www.legislation.gov.uk/%s/made" % (slug)

idbs = {}

# find cited legislation ..
legislations = {}

def add_legislation(legislation, name='', idb=None):
    if legislation not in legislations:
        legislations[legislation] = { 'idbs': [] }
    legislations[legislation]['name'] = name
    if idb:
        legislations[legislation]['idbs'].append(idb)


for row in csv.DictReader(open(register_path), delimiter='\t'):
    add_legislation(row['legislation'], '', row['internal-drainage-board'])
    idbs[row['internal-drainage-board']] = row

for row in csv.DictReader(open(legislation_path), delimiter='\t'):
    add_legislation(row['legislation'], row['name'])


print("""
<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<style>
body {
    font-family: "Helvetica Neue", "Helvetica";
}
table {
    width: 100%;
}
th, td {
    text-align: left;
}
.count {
    text-align: right;
}
td {
    vertical-align: top;
}

</style>
</head>
<body>
<div class="wrapper">

<h2>Internal Drainage Boards</h2>

<table id="internal-drainage-boards" class="tablesorter">
<thead>
    <tr>
      <th class='id'>internal-drainage-board</th>
      <th>name</th>
      <th>legislation</th>
      <th>start-date</th>
      <th>end-date</th>
      <th></th>
    </tr>
</thead>
<tbody>
""")

for row in csv.DictReader(open(register_path), delimiter='\t'):

    print("<tr id='%s'>" % (row['internal-drainage-board']))
    print("<td>%s</td>" % (row['internal-drainage-board']))
    print("<td class='name'>%s</td>" % (row['name']))
    print("<td><a href='%s'>%s</a></td>" % (legislation_url(row['legislation']), row['legislation']))
    print("<td>%s</td>" % (row['start-date']))
    print("<td>%s</td>" % (row['end-date']))
    print("<td></td>")
    print("</tr>")

print("""
</tbody>
</table>

<h2>Drainage boards legislation</h2>

<table id="legislation" class="tablesorter">
<thead>
    <tr>
      <th class='id'>legislation</th>
      <th>IDBs</th>
      <th>name</th>
    </tr>
</thead>
<tbody>
""")

for legislation in sorted(legislations):

    if legislation:
        row = legislations[legislation]
        print("<tr id='%s'>" % (legislation))

        idb_links = []
        for idb in row['idbs']:
            idb_links.append('<a href="#%s" title="%s">%s</a>' % (idb, idbs[idb]['name'], idb))

        print("<td>" + ", ".join(idb_links) + "</td>")
        print("<td><a href='%s'>%s</a></td>" % (legislation_url(legislation), legislation))
        print("<td class='name'>%s</td>" % (row['name']))
        print("</tr>")

print("""
</tbody>
</table>
""")
print("""
</div>
</body>
</html>
""")
