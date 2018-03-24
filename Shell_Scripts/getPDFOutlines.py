#!/usr/bin/python

from Foundation import  NSURL
import Quartz as Quartz
import sys


def getOutlines(infile):
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		outline = Quartz.PDFOutline.alloc().init()
		outline = myPDF.outlineRoot()
		for n in range(outline.numberOfChildren()):
			print n
			print outline.childAtIndex_(n).label()
			print outline.childAtIndex_(n).destination()
		
if __name__ == '__main__':
	for filename in sys.argv[1:]:
		getOutlines(filename)