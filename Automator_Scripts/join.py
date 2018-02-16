#! /usr/bin/python
# coding=utf-8
#
# JOINPDFS v1.0 : Tool to concatenate PDFs.
# New tool built from the ground up using PDFKit, instead of Core Graphics.
# by Ben Byram-Wigfield

import sys
import os.path
from CoreFoundation import (CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault, NSURL)
import Quartz as Quartz


def createPDFDocumentWithPath(path):
	pdfURL = NSURL.fileURLWithPath_(path)
	if pdfURL:
		return Quartz.PDFDocument.alloc().initWithURL_(pdfURL)

def getFilename(filepath, basename):
	fullname = basename + ".pdf"
	i=0
	while os.path.exists(os.path.join(filepath, fullname)):
		i += 1
		fullname = basename + " %02d.pdf"%i
	return os.path.join(filepath, fullname)

def join(incomingFiles):
	# Set the output file location and name.
	prefix = os.path.dirname(incomingFiles[0])
	filename = "Combined"
	outfile = getFilename(prefix, filename)
	# Load in the first PDF file, to which the rest will be added.
	firstPDF = createPDFDocumentWithPath(incomingFiles[0])
	pageIndex = firstPDF.pageCount()
	
	# create PDFDocument object for the remaining files.
	docs = map(createPDFDocumentWithPath, incomingFiles[1:])
	for doc in docs:
		if doc:
			pages = doc.pageCount()
			for p in range(0, pages):
				pageIndex = firstPDF.pageCount()
				page = doc.pageAtIndex_(p)
				firstPDF.insertPage_atIndex_(page, pageIndex)
				
	firstPDF.writeToFile_(outfile)		
	

if __name__ == "__main__":
	if len(sys.argv) > 1:
		join(sys.argv[1:])