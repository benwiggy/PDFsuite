#! /usr/bin/python
# coding: utf-8

# QUARTZFILTER  v.1.4: Script to apply a MacOS Quartz Filter to a PDF file.
# by Ben Byram-Wigfield
# 
# quartzfilter.py <input <filter> <output>
#
# The script will accept the bare name of a filter (without .qfilter) if file path not given.
# E.g. quartzfilter.py /path/to/myPDF.pdf 'Sepia Tone.qfilter' /path/to/output.pdf

import os, getopt, sys
import Quartz as Quartz
from Foundation import NSURL

def checkFilter(name):
	if not os.path.split(name)[0]:
		Filters = (Quartz.QuartzFilterManager.filtersInDomains_(None))
		found = False
		for eachFilter in Filters:
			filterPath = eachFilter.url().fileSystemRepresentation()
			if name == os.path.split(filterPath)[1]:
				found = True
		if found:
			return name
	else:
		if os.path.exists(name):
			return name
				
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

	inputfile =args[0] #.decode('utf-8')
	if not inputfile:
		print ('Unable to open input file')
		sys.exit(2)

	filter = args[1] #.decode('utf-8')
	filter = checkFilter(filter)
	if not filter:
		print ('Unable to find Quartz Filter')
		sys.exit(2)

	outputfile = args[2] #.decode('utf-8')
	if not outputfile:
		print ('No valid output file specified')
		sys.exit(2)
	# You could just take the inputfile as the outputfile if not explicitly given.
		# outputfile = inputfile

	pdfURL = NSURL.fileURLWithPath_(inputfile)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	filterURL = NSURL.fileURLWithPath_(filter)
	value = Quartz.QuartzFilter.quartzFilterWithURL_(filterURL)
	dict = { 'QuartzFilter': value }
	pdfDoc.writeToFile_withOptions_(outputfile, dict)

if __name__ == "__main__":
   main(sys.argv[1:])