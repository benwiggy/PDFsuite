#!/usr/bin/python
# coding=utf-8

# REMOVEPAGE v.1.0 : Removes the first page of any PDF file(s) sent as arguments.
# Unless there's only one page.

# by Ben Byram-Wigfield.

from Quartz import PDFDocument
import sys
from Foundation import NSURL

def removePage(filename):
	filename = filename.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		pageNum = pdfDoc.pageCount()
		if pageNum > 1:
			pdfDoc.removePageAtIndex_(0)
			pdfDoc.writeToFile_(filename)
	return

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		removePage(filename)