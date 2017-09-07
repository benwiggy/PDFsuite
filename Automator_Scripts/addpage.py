#!/usr/bin/python
# coding=utf-8
#
# Adds a blank page to the start of any PDF file sent as arguments.
# Can be used as Automator action or as shell script.

from Quartz import PDFDocument, PDFPage, kPDFDisplayBoxMediaBox
import sys
from CoreFoundation import NSURL


A4p = [[0,0], [595.28, 841.88]]
# USLetter = [[0,0], [612, 792]]
mediabox = kPDFDisplayBoxMediaBox

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		filename = filename.decode('utf-8')
		pdfURL = NSURL.fileURLWithPath_(filename)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		blankPage = PDFPage.alloc().init()
		blankPage.setBounds_forBox_(A4p, mediabox)
		pdfDoc.insertPage_atIndex_(blankPage, 0)
		pdfDoc.writeToFile_(filename)