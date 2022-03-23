#!/usr/bin/env python3

# ADDPAGE v.3 : Adds a blank page to the END of any PDF file(s) sent as arguments.

# by Ben Byram-Wigfield.

# Rewritten for python3. You may need to pip install pyobjc.

# Page size of blank page is taken from first page of PDF.
# Can be used as Automator action or as shell script.


from Quartz import PDFDocument, PDFPage, kPDFDisplayBoxMediaBox
import sys
from Foundation import NSURL

# kPDFDisplayBoxMediaBox = 0 ; crop = 1; bleed = 2; trim = 3; artbox = 4
mediabox = kPDFDisplayBoxMediaBox

def addPage(filename):
	# filename = filename.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		pageNum = pdfDoc.pageCount()
		page = pdfDoc.pageAtIndex_(0)
		pageSize = page.boundsForBox_(mediabox)
		blankPage = PDFPage.alloc().init()
		blankPage.setBounds_forBox_(pageSize, mediabox)
		pdfDoc.insertPage_atIndex_(blankPage, pageNum)
		pdfDoc.writeToFile_(filename)
	return

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		addPage(filename)