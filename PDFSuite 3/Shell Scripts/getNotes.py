#!/usr/bin/env python

# GETNOTES v1.0
# by Ben Byram-Wigfield
# Lists the Annotations in a PDF file.

from Foundation import  NSURL, NSString
import Quartz as Quartz
import sys

def getNotes(infile):
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		pages = myPDF.pageCount()
		for p in range(0, pages):
			page = myPDF.pageAtIndex_(p)
			if page.annotations():
				for eachNote in page.annotations():
					print (eachNote)
					print (eachNote.contents())
					print("-------")

if __name__ == "__main__":	
	for filename in sys.argv[1:]:
		getNotes(filename)