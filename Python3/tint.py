#!/usr/bin/env python3
#
# TINT: v1.1
# Overlays a tint over the entire PDF.
# by Ben Byram-Wigfield

import sys
import os
import Quartz as Quartz
from Foundation import NSURL, kCFAllocatorDefault

# Loads in PDF document
def createPDFDocumentFromPath(path):
	url = NSURL.fileURLWithPath_(path)
	return Quartz.CGPDFDocumentCreateWithURL(url)

# Creates a Context for drawing
def createOutputContextWithPath(path, dictarray):
	url = NSURL.fileURLWithPath_(path)
	return Quartz.CGPDFContextCreateWithURL(url, None, dictarray)


def makeRectangle(x, y, xSize, ySize, color, alpha):
	red, green, blue = color[:]
	Quartz.CGContextSetRGBFillColor (writeContext, red, green, blue, alpha)
	Quartz.CGContextFillRect (writeContext, Quartz.CGRectMake(x, y, xSize, ySize))
	return
	
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
			
def tint(filename): 
	global writeContext	
	# The color of the tint. Sepia is 0.44, 0.26, 0.08. Some transparency may help.
	red = 1.0
	green = 0.93
	blue = 0.81
	alpha = 1.0
	myColor=[red, green, blue]
	
	writeContext = None
			
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + "+tint.pdf"
	metaDict = getDocInfo(filename)

	writeContext = createOutputContextWithPath(outFilename, metaDict)
	readPDF = createPDFDocumentFromPath(filename)
	
	if writeContext != None and readPDF != None:
		numPages = Quartz.CGPDFDocumentGetNumberOfPages(readPDF)
		for pageNum in range(1, numPages + 1):	
			page = Quartz.CGPDFDocumentGetPage(readPDF, pageNum)
			if page:
				mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				if Quartz.CGRectIsEmpty(mediaBox):
					mediaBox = None			
				Quartz.CGContextBeginPage(writeContext, mediaBox)	
				Quartz.CGContextSetBlendMode(writeContext, Quartz.kCGBlendModeOverlay)
				Quartz.CGContextDrawPDFPage(writeContext, page)
				makeRectangle(0, 0, mediaBox.size.width, mediaBox.size.height, myColor, alpha)
				Quartz.CGContextEndPage(writeContext)
		Quartz.CGPDFContextClose(writeContext)
		del writeContext
			
	else:
		print ("A valid input file and output file must be supplied.")
		sys.exit(1)
if __name__ == "__main__":
	for filename in sys.argv[1:]:
		
		tint(filename)
