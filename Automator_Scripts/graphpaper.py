#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# GRAPHPAPER: v1.1
# Modified from /System/Library/Automator/Add Grid to PDF Documents.action/Contents/Resources/graphpaper.py
# to include small and large gradations; better handling of existing metadata; and made faster!

import sys
import os
import Quartz as Quartz
from Foundation import NSURL, kCFAllocatorDefault

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

def drawLines(pdf, mediaBox, grid, red, green, blue, alpha) :
	Quartz.CGContextSetRGBStrokeColor(pdf, red, green, blue, alpha)
	x = mediaBox.origin.x
	count = -1
	while x <= mediaBox.size.width:
		count += 1
		if not count%grid[1]:
			Quartz.CGContextSetLineWidth(pdf, 0.5)
		else:
			Quartz.CGContextSetLineWidth(pdf, 0.1)
		Quartz.CGContextMoveToPoint(pdf, x, mediaBox.origin.y)
		Quartz.CGContextAddLineToPoint(pdf, x, mediaBox.origin.y + mediaBox.size.height)
		Quartz.CGContextStrokePath(pdf)
		x += grid[0]

	y = mediaBox.origin.y
	count = -1
	while y < mediaBox.size.height:
		count += 1
		if not count%grid[1]:
			Quartz.CGContextSetLineWidth(pdf, 0.5)
		else:
			Quartz.CGContextSetLineWidth(pdf, 0.1)
		Quartz.CGContextMoveToPoint(pdf, mediaBox.origin.x, y)
		Quartz.CGContextAddLineToPoint(pdf, mediaBox.origin.x + mediaBox.size.width, y)
		Quartz.CGContextStrokePath(pdf)
		y += grid[0]	
		
def makeGrid(filename):
  
	# The distance, in points, between each grid line, and frequency of thicker lines:
	# Default is 10pt, 10 (Useful for determining values in points)
	# Other useful values are:
	# [12, 6] (Points and Inches)
	# [9, 8] (1/8ths and Inches)
	# [2.835, 10] (mm, cm)
	gridSize = [10,10]
	
	# The color of the grid lines
	# Default is dark Yellow
	red = 1
	green = 0.6
	blue = 0.1
	alpha = 1
	
	over = 1
	
	writeContext = None
			
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + "+grid.pdf"
	metaDict = getDocInfo(filename)

	writeContext = createOutputContextWithPath(outFilename, metaDict)
	readPDF = createPDFDocumentWithPath(filename)
	
	if writeContext != None and readPDF != None:
		numPages = Quartz.CGPDFDocumentGetNumberOfPages(readPDF)
		for pageNum in xrange(1, numPages + 1):	
			page = Quartz.CGPDFDocumentGetPage(readPDF, pageNum)
			if page:
				mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				if Quartz.CGRectIsEmpty(mediaBox):
					mediaBox = None			
				Quartz.CGContextBeginPage(writeContext, mediaBox)	
				if (not over) :
					drawLines(writeContext, mediaBox, gridSize, red, green, blue, alpha)
				Quartz.CGContextDrawPDFPage(writeContext, page)
				if (over) :
					drawLines(writeContext, mediaBox, gridSize, red, green, blue, alpha)			
				Quartz.CGContextEndPage(writeContext)			
		Quartz.CGPDFContextClose(writeContext)
		del writeContext
			
	else:
		print "A valid input file and output file must be supplied."
		sys.exit(1)
		
if __name__ == "__main__":
	for filename in sys.argv[1:]:
		makeGrid(filename)
    