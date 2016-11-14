import sys, getopt
from functions import *

__author__ = 'agrojas'

def main(argv):
	options, remainder = getopt.getopt(argv, 'f:q', ['file=', 'query=',])

	filename = ""
	query = ""
	for opt, arg in options:
		if opt in ('-f', '--file'):
			filename = arg
		elif opt in ('-q', '--query'):
			query = arg

	if filename != "":
		trainDBwith(filename)

	if query != "":
		(vertex,name) = query.split(":")
		if (vertex != "") and (name != ""):
			print(queryToVertexName(vertex,name))
		else:
			print(queryToVertex(vertex))


if __name__ == '__main__':
    main(sys.argv[1:])
