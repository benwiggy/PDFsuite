#!/usr/bin/env python3

# copyOutlines v.1.0
# Copy PDF Table of Contents from one PDF to another.
# by Ben Byram-Wigfield
# copyOutlines.py <source file> <destination file>


from Foundation import  NSURL
import Quartz as Quartz
import sys


def copyOutlines(source, dest):
	pdfURL = NSURL.fileURLWithPath_(source)
	inPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if inPDF:
		outline = Quartz.PDFOutline.alloc().init()
		outline = inPDF.outlineRoot()
	pdfURL = NSURL.fileURLWithPath_(dest)
	outPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	outPDF.setOutlineRoot_(outline)
	outPDF.writeToFile_(dest)	

if __name__ == '__main__':
	copyOutlines(sys.argv[1], sys.argv[2])