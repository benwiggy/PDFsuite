#!/usr/bin/env python3

# This script will list the Table of Contents data from any PDF file(s) given as arguments.

from Foundation import  NSURL
import Quartz as Quartz
import sys


def getOutlines(infile):
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		outline = Quartz.PDFOutline.alloc().init()
		outline = myPDF.outlineRoot()
		if outline:
			print (f'Root Outline: {outline.label()}')
			print (f'Number of Children: {outline.numberOfChildren()}')
			print (outline.index())
			for n in range(outline.numberOfChildren()):
				print (f'Child: {n}')
				print (outline.childAtIndex_(n).label())
				print (outline.childAtIndex_(n).destination())
				print (outline.childAtIndex_(n).parent().label())
if __name__ == '__main__':
	for filename in sys.argv[1:]:
		getOutlines(filename)