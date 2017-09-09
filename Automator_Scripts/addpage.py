#!/usr/bin/python
# coding=utf-8
#
#by Ben Byram-Wigfield. v1.0.
# Adds a blank page to the start of any PDF file sent as arguments.
# Can be used as Automator action or as shell script.
# To do: Get page size from PDF and match it

from Quartz import PDFDocument, PDFPage, kPDFDisplayBoxMediaBox
import sys
from Foundation import NSURL


pageSize = [[0,0], [595.28, 841.88]] # A4
# pageSize = [[0,0], [612, 792]] # US Letter
mediabox = kPDFDisplayBoxMediaBox

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		filename = filename.decode('utf-8')
		pdfURL = NSURL.fileURLWithPath_(filename)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		blankPage = PDFPage.alloc().init()
		blankPage.setBounds_forBox_(pageSize, mediabox)
		pdfDoc.insertPage_atIndex_(blankPage, 0)
		pdfDoc.writeToFile_(filename)