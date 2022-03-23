#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Merge v. 0.1
# Merges two PDFs 

import sys
import os
import Quartz as Quartz
from Foundation import NSURL, kCFAllocatorDefault

# OPTIONS

watermark = os.path.expanduser("~/Desktop/Test.pdf")


# Loads in PDF document
def createPDFDocumentWithPath(path):
	url = NSURL.fileURLWithPath_(path)
	return Quartz.CGPDFDocumentCreateWithURL(url)

# Creates a Context for drawing
def createOutputContextWithPath(path, dictarray):
	url = NSURL.fileURLWithPath_(path)
	return Quartz.CGPDFContextCreateWithURL(url, None, dictarray)
	
# Gets DocInfo from input file to pass to output.
# PyObjC returns Keywords in an NSArray; they must be tupled.
def getDocInfo(file):
	file = file.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(file)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		metadata = pdfDoc.documentAttributes()
	if "Keywords" in metadata:
		keys = metadata["Keywords"]
		mutableMetadata = metadata.mutableCopy()
		mutableMetadata["Keywords"] = tuple(keys)
		return mutableMetadata
	else:
		return metadata



def merge(filename):

	writeContext = None
			
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + "+wm.pdf"
	metaDict = getDocInfo(filename)

	writeContext = createOutputContextWithPath(outFilename, metaDict)
	readPDF = createPDFDocumentWithPath(filename)
	mergePDF = createPDFDocumentWithPath(watermark)
	
	if writeContext != None and readPDF != None:
		numPages = Quartz.CGPDFDocumentGetNumberOfPages(readPDF)
		for pageNum in range(1, numPages + 1):	
			page = Quartz.CGPDFDocumentGetPage(readPDF, pageNum)
			mergepage = Quartz.CGPDFDocumentGetPage(mergePDF, 1)
			if page:
				mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				if Quartz.CGRectIsEmpty(mediaBox):
					mediaBox = None			
				Quartz.CGContextBeginPage(writeContext, mediaBox)	
				Quartz.CGContextSetBlendMode(writeContext, Quartz.kCGBlendModeOverlay)

				Quartz.CGContextDrawPDFPage(writeContext, page)
				Quartz.CGContextDrawPDFPage(writeContext, mergepage)
				Quartz.CGContextEndPage(writeContext)
		Quartz.CGPDFContextClose(writeContext)
		del writeContext
			
	else:
		print "A valid input file and output file must be supplied."
		sys.exit(1)



if __name__ == "__main__":
	for filename in sys.argv[1:]:
		
		merge(filename)
