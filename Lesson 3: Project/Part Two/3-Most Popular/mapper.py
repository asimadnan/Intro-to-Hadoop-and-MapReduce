#!/usr/bin/python

#format of a log line is
#10.190.174.142 - - [03/Dec/2011:13:28:09 -0800] "GET /images/filmmediablock/360/07082218.jpg HTTP/1.1" 200 154609

import sys

for line in sys.stdin:
	data = line.strip().split("GET ")
	if(len(data) > 1):
		docname = data[1].split(" ")[0]
		print "{0}\t{1}".format(docname, 1)
