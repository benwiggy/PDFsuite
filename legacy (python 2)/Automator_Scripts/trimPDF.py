#! /usr/bin/env python
# coding=utf-8

# TRIM PDF v.1.0 : Crop the mediabox to the size of the trimbox, if different.
# This lets you crop a page containing printers crop marks to the trimmed page size.
# by Ben Byram-Wigfield v1.0

import sys
import os
from Quartz import PDFDocument, kPDFDisplayBoxMediaBox, kPDFDisplayBoxTrimBox, CGRectEqualToRect
from CoreFoundation import NSURL

mediabox = kPDFDisplayBoxMediaBox
trimbox = kPDFDisplayBoxTrimBox
	
def trimPDF(filename):
	hasBeenChanged = False
	filename = filename.decode('utf-8')
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + " TPS.pdf"
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		pages = pdfDoc.pageCount()
		for p in range(0, pages):
			page = pdfDoc.pageAtIndex_(p)
			mediaBoxSize = page.boundsForBox_(mediabox)
			trimBoxSize = page.boundsForBox_(trimbox)
			if not CGRectEqualToRect(mediaBoxSize, trimBoxSize):
				page.setBounds_forBox_(trimBoxSize, mediabox)
				hasBeenChanged = True
		if hasBeenChanged:
			pdfDoc.writeToFile_(outFilename)

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		trimPDF(filename)
