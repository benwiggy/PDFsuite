#!/usr/bin/env python
# coding=utf-8

# GET PDF OUTLINES v. 1.2
# by Ben Byram-Wigfield
# This script will list the Table of Contents data from any PDF file(s) given as arguments.
# Haven't sorted out indenting text for each hierarchical level.

from Foundation import  NSURL
import Quartz as Quartz
import sys
	
def recurseOutlines(thisOutline):
	print (thisOutline.label())
	print (thisOutline.destination())
	if thisOutline.numberOfChildren() != 0:
		for n in range(thisOutline.numberOfChildren()):
			recurseOutlines(thisOutline.childAtIndex_(n))

def getOutlines(infile):
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		outline = Quartz.PDFOutline.alloc().init()
		outline = myPDF.outlineRoot()
		if outline:
			if outline.numberOfChildren() != 0:
				for n in range(outline.numberOfChildren()):
					recurseOutlines(outline.childAtIndex_(n))
					
if __name__ == '__main__':
	for filename in sys.argv[1:]:
		getOutlines(filename)