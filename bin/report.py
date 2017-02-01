#!/usr/bin/env python3

import csv


def legislation_url(legislation):
    slug = legislation.replace('-', '/')
    return "http://www.legislation.gov.uk/%s/made" % (slug)


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

key = 'internal-drainage-board'

register_path = 'data/internal-drainage-board/internal-drainage-boards.tsv'
for row in csv.DictReader(open(register_path), delimiter='\t'):

    print("<tr id='%s'>" % (row[key]))
    print("<td>%s</td>" % (row[key]))
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
      <th>name</th>
    </tr>
</thead>
<tbody>
""")

key = 'legislation'

path = 'lists/legislation/list.tsv'
for row in csv.DictReader(open(path), delimiter='\t'):

    print("<tr id='%s'>" % (row[key]))
    print("<td><a href='%s'>%s</a></td>" % (legislation_url(row['legislation']), row['legislation']))
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
