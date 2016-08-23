#! /usr/bin/python

# by Ben Byram-Wigfield
# Script to apply a MacOS Quartz Filter to a PDF file.
#
import sys
import os
import getopt
from Quartz.CoreGraphics import *
from CoreFoundation import (NSURL, QuartzFilter)


def main(argv):
	inputfile = ""
	outputfile = ""
	filter = ""

	try:
		opts,args = getopt.getopt (sys.argv[1:], '', [])
	except getopt.GetoptError:
		usage ()
		sys.exit (1)

	if len (args) != 3:
		usage ()
		sys.exit (1)

	filter = args[0]
	if not filter:
		print 'Unable to create context filter'
		sys.exit (1)

	inputfile =args[1]
	if not inputfile:
		print 'Unable to open input file'
		sys.exit (1)

	outputfile = args[2]
	if not outputfile:
		print 'Unable to create output context'
		sys.exit (1)

	pdf_url = NSURL.fileURLWithPath_(inputfile)
	pdf_doc = CG.PDFDocument.alloc().initWithURL_(pdf_url)
	furl = NSURL.fileURLWithPath_(filter)
	value = QuartzFilter.quartzFilterWithURL_(furl)
	dict = { 'QuartzFilter': value }
	pdf_doc.writeToFile_withOptions_(outputfile, dict)

if __name__ == "__main__":
   main(sys.argv[1:])