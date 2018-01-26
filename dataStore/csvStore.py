# coding=utf-8

import csv
from collections import namedtuple

# headers = ['ID','UserName','Password','Age','Country']
# rows = [(1001,"qiye","qiye_pass",24,"China"),
#          (1002,"Mary","Mary_pass",20,"USA"),
#          (1003,"Jack","Jack_pass",20,"USA"),
#        ]
#
# with open('qiye.csv','wb') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(headers)
#     csv_writer.writerows(rows)

# headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
# rows = [{'ID': 1001, 'UserName': "qiye", 'Password': "qiye_pass", 'Age': 24, 'Country': "China"},
#         {'ID': 1002, 'UserName': "Mary", 'Password': "Mary_pass", 'Age': 20, 'Country': "USA"},
#         {'ID': 1003, 'UserName': "Jack", 'Password': "Jack_pass", 'Age': 20, 'Country': "USA"},
#         ]
#
# with open('qiye.csv', 'w') as f:
#     csv_f = csv.DictWriter(f, headers)
#     csv_f.writeheader()
#     csv_f.writerows(rows)

# with open('qiye.csv', 'r') as csvReader:
#     csv_reader = csv.reader(csvReader)
#     header = next(csv_reader)
#     print header
#     for row in csv_reader:
#         print row

# with open('qiye.csv', 'r') as r:
#     csv_r = csv.reader(r)
#     header = next(csv_r)
#     rows = namedtuple('Row', header)
#     for row in csv_r:
#         row = rows(*row)
#         print row.UserName, row.Password
#         print row

with open('qiye.csv','r') as reader:
    csv_r = csv.DictReader(reader)
    for row in csv_r:
        print row.get('UserName')
