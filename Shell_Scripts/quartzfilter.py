#! /usr/bin/python
# coding: utf-8

# QUARTZFILTER  v.1.3: Script to apply a MacOS Quartz Filter to a PDF file.
# by Ben Byram-Wigfield
# 
# quartzfilter.py <input <filter> <output>
#
# The script will check the folders for installed filters if file path not given.

import os, getopt, sys
from Quartz import PDFDocument
from CoreFoundation import (NSURL, QuartzFilter)

def checkFilter(pathname):
	if not os.path.split(pathname)[0]:
		Filters = (Quartz.QuartzFilterManager.filtersInDomains_(None))
		for eachFilter in Filters:
			name = eachFilter.url().fileSystemRepresentation()
			if pathname == os.path.split(name)[1]:
				return name
	else:
		if os.path.exists(pathname):
			return pathname
				
def main(argv):
	inputfile = ""
	outputfile = ""
	filter = ""

	try:
		opts, args = getopt.getopt(sys.argv[1:], "ifo", ["input", "filter", "output"])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)

	if len(args) != 3:
		print("Not enough arguments")
		sys.exit(2)

	inputfile =args[0].decode('utf-8')
	if not inputfile:
		print 'Unable to open input file'
		sys.exit(2)

	filter = args[1].decode('utf-8')
	filter = checkFilter(filter)
	if not filter:
		print 'Unable to find Quartz Filter'
		sys.exit(2)

	outputfile = args[2].decode('utf-8')
	# You could just take the inputfile as the outputfile if not explicitly given.
	if not outputfile:
		print 'No valid output file specified'
		sys.exit(2)

	pdfURL = NSURL.fileURLWithPath_(inputfile)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	filterURL = NSURL.fileURLWithPath_(filter)
	value = QuartzFilter.quartzFilterWithURL_(filterURL)
	dict = { 'QuartzFilter': value }
	pdfDoc.writeToFile_withOptions_(outputfile, dict)

if __name__ == "__main__":
   main(sys.argv[1:])


