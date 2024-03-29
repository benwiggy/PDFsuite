#!/usr/bin/env python3
#
# Scale PDF v. 0.1
# Scales PDFs to a given size
# DOESN'T WORK YET

import sys
import os
import Quartz as Quartz
from Foundation import NSURL, kCFAllocatorDefault

# OPTIONS
scaleSize = 1.41
A3 = [[0,0], [1190.55, 841.88]]

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

def scale(filename):
	writeContext = None
	mediabox = 0 # Quartz.kPDFDisplayBoxMediaBox
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + " size.pdf"
	metaDict = getDocInfo(filename)
	writeContext = createOutputContextWithPath(outFilename, metaDict)
	pdfDoc = createPDFDocumentWithPath(filename)
	if pdfDoc:
		pages = Quartz.CGPDFDocumentGetNumberOfPages(pdfDoc)
		for p in range(0, pages):
			page = Quartz.CGPDFDocumentGetPage(pdfDoc, p)
			if page:
				mediaBoxSize = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				Quartz.CGContextBeginPage(writeContext, mediaBoxSize)
				Quartz.CGContextSaveGState(writeContext)

				Quartz.CGContextDrawPDFPage(writeContext, page)
				print("qwe")
				# Quartz.CGContextDrawPDFPage(writeContext, mergepage)
				Quartz.CGContextEndPage(writeContext)
		Quartz.CGPDFContextClose(writeContext)
		del writeContext

	else:
		print ("A valid input file and output file must be supplied.")
		sys.exit(1)



if __name__ == "__main__":
	for filename in sys.argv[1:]:
		
		scale(filename)
		