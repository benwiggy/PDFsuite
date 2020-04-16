#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ----------------------------------------------------------------
# PDF Booklet Imposition Script for MacOS  v2.4 (Automator)
# by Ben Byram-Wigfield
# Feel free to use, modify and pass on with acknowledgement.
#
# Usage: As a script in Automator, or: bookletPDF.py <file1> <file2> ... 
# Original file is preserved, and output file has suffix added.
# NB: The script will overwrite existing output file of the same name.
#
# Script can be configured for stacking 4pp signatures or gathering booklet spreads.
# ----------------------------------------------------------------

# Beware of indexes starting from 0 and 1...!!! CGPDFDocument starts page count at 1.

import os, sys
import copy
import Quartz as Quartz
from Foundation import (NSURL, kCFAllocatorDefault)

# Uncomment the sheet size you want.
A3 = [[0,0], [1190.55, 841.88]]
A4 = [[0,0], [841.88, 595.28]]
# USLetter = [[0,0], [792, 612]]
# Tabloid = [[0,0], [1224, 792]]

# OPTIONS
# Change this to one of the sizes listed above, if you want.
sheetSize = A3

# Set file suffix
suffix = " booklet.pdf"
# If hasSignatures, sheets will be arranged for stacking in 4pp sections.
hasSignatures = False
pagesPerSheet = 4 # Not sure what will happen if this is changed.
creep = 0.5 # in points. NB: Eventually, the pages will collide.
imposedOrder = [] 

# FUNCTIONS
# Loads in PDF document
def createPDFDocumentFromPath(path):
	url = NSURL.fileURLWithPath_(path)
	return Quartz.CGPDFDocumentCreateWithURL(url)

# Creates a Context for drawing
def createOutputContextFromPath(path, dictarray):
	url = NSURL.fileURLWithPath_(path)
	return Quartz.CGPDFContextCreateWithURL(url, None, dictarray)

# Get page sequence for imposition order (e.g. 4,1,2,3)
def imposition(pageRange):
	for i in range(1, (len(pageRange)/2), 2):
		# First we do recto
		imposedOrder.append(pageRange[i*-1])
		imposedOrder.append(pageRange[i-1])
		# And now we do verso
		imposedOrder.append(pageRange[i])
		imposedOrder.append(pageRange[(i+1)*-1])
	return imposedOrder

# Make sure pages are portrait in orientation.
def getRotation(pdfpage):
	displayAngle = 0
	rotValue = Quartz.CGPDFPageGetRotationAngle(pdfpage)
	mediaBox = Quartz.CGPDFPageGetBoxRect(pdfpage, Quartz.kCGPDFMediaBox)
	if not Quartz.CGRectIsEmpty(mediaBox):
		x = Quartz.CGRectGetWidth(mediaBox)
		y = Quartz.CGRectGetHeight(mediaBox)
		if (x > y): displayAngle = -90
		displayAngle -=  rotValue
	return displayAngle	

# Gets DocInfo from input file to pass to output.
# PyObjC returns Keywords in an NSArray; they must be tupled.
def getDocInfo(file):
	# file = file.decode('utf-8')
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

# Close Context when finished
def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context	

# MAIN 
def makeBooklet(argv):

	leftPage = copy.deepcopy(sheetSize)
	shift = sheetSize[1][0]/2
	leftPage[1][0] = shift
	rightPage = copy.deepcopy(leftPage)
	rightPage[0][0] = shift
	blanks = 0

# Initiate new PDF, get source PDF data, number of pages.
	shortName = os.path.splitext(argv)[0]
	writeFilename = shortName + suffix
	# writeFilename = writeFilename.encode('utf-8')
	metaDict = getDocInfo(argv)
	writeContext = createOutputContextFromPath(writeFilename, metaDict)
	source = createPDFDocumentFromPath(argv)
	totalPages = Quartz.CGPDFDocumentGetNumberOfPages(source)

# Add 0 to Unsorted Order for each blank page required to be a multiple of pages per sheet.
	UnsortedOrder = range(1, totalPages+1)
	if totalPages%pagesPerSheet:
		blanks = pagesPerSheet - (totalPages%pagesPerSheet)
		for i in range(blanks):
			UnsortedOrder.append(0)
	totalPages = len(UnsortedOrder)

	if hasSignatures:
		signatureSize = pagesPerSheet
	else:
		signatureSize = totalPages

	for something in range(0, totalPages, signatureSize):
		imposition(UnsortedOrder[something:(something+signatureSize)])

# For each side of the sheet, we must...
# ... create a PDF page, take two source pages and place them differently, then close the page.
# If the source page number is 0 (i.e. blank), then move on without drawing.
	Sides = totalPages/2
	count = 0
	for n in range(Sides):
		Quartz.CGContextBeginPage(writeContext, sheetSize)
		for position in [leftPage, rightPage]:
			if imposedOrder[count]:
				page = Quartz.CGPDFDocumentGetPage(source, imposedOrder[count])
				Quartz.CGContextSaveGState(writeContext)
				# Check PDF page rotation AND mediabox orientation.
				angle = getRotation(page)
				Quartz.CGContextConcatCTM(writeContext, Quartz.CGPDFPageGetDrawingTransform(page, Quartz.kCGPDFMediaBox, position, angle, True))
				# Uncomment next line to draw box round each page
				# Quartz.CGContextStrokeRectWithWidth(writeContext, leftPage, 2.0)
				Quartz.CGContextDrawPDFPage(writeContext, page)
				Quartz.CGContextRestoreGState(writeContext)
			count += 1
		Quartz.CGContextEndPage(writeContext) 
		
		# Set creep for next sheet.		
		if count%4 == 0:
			leftPage[0][0] += creep
			rightPage[0][0] -= creep
			
	# Do tidying up
	contextDone(writeContext)	

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		makeBooklet(filename)
