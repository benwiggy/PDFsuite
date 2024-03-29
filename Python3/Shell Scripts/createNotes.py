#!/usr/bin/env python3

from Foundation import  NSURL, NSString
from AppKit import NSColor
import Quartz as Quartz
import sys, os

os.environ["PDFKIT_LOG_ANNOTATIONS"] = 'True'

# You will need to change these filepaths to a local test pdf and an output file.

outfile = '/path/to/file.pdf'
infile = '/path/to/file.pdf'
myYellow = NSColor.yellowColor()

if __name__ == "__main__":

	myRect = Quartz.CGRectMake(100,100,10,14)
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		pages = myPDF.pageCount()
		myNote = Quartz.PDFAnnotation.alloc().initWithBounds_forType_withProperties_(myRect, "Text", None)
		myNote.setContents_("Qwe qwe qwe ")
		myNote.setColor_(myYellow)
		page = myPDF.pageAtIndex_(0)
		page.addAnnotation_(myNote)
		
		myPDF.writeToFile_(outfile)
	else:
		print("No valid PDF was received.")
