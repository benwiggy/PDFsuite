#! /usr/bin/env python
# coding=utf-8

# TITLE : Change Title metadata to filename of a PDF file.
# by Ben Byram-Wigfield


#
import sys
import os
import getopt
import Quartz as Quartz

from CoreFoundation import NSURL

def setMetadata(filename):
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	value  = os.path.splitext(filename)[0]
	options = { Quartz.kCGPDFContextTitle: value }
	pdfDoc.writeToFile_withOptions_(outputfile, options)

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		setMetadata(filename)
   

