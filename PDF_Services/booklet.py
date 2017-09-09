#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ----------------------------------------------------------------
# PDF Booklet Imposition Script for MacOS
# by Ben Byram-Wigfield v.2.1
# Feel free to use, modify and pass on with acknowledgement.

# 1. Set OPTIONS below for output folder, sheet size, and creep
# 2. Install into ~/Library/PDF Services
# 3. It will then appear as an option in the PDF button of the Print dialog.
# (if it has executable flags set.)

# Script can be configured for stacking 4pp signatures or gathering booklet spreads.
# ----------------------------------------------------------------

# Beware of indexes starting from 0 and 1...!!! CGPDFDocument starts page count at 1.

import os, sys
import copy
import Quartz as Quartz
from Foundation import (NSURL, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)
from AppKit import NSSavePanel, NSApp


# Uncomment the page size you want.
A3 = [[0,0], [1190.55, 841.88]]
# A4 = [[0,0], [841.88, 595.28]]
# USLetter = [[0,0], [792, 612]]
# Tabloid = [[0,0], [1224, 792]]

# OPTIONS
# Change this to one of the sizes listed above, if you want.
sheetSize = A3
# Set the default location for saving the files. 
destination = os.path.expanduser("~/Desktop")
# Set file suffix
suffix = " booklet.pdf"
# If hasSignatures, sheets will be arranged for stacking in 4pp sections.
hasSignatures = False
pagesPerSheet = 4 # Not sure what will happen if this is changed.
creep = 0.5 # in points. NB: Eventually, the pages will collide.
imposedOrder = [] 

# FUNCTIONS

def save_dialog(directory, filename):
	panel = NSSavePanel.savePanel()
	panel.setTitle_("Save PDF booklet")
	myUrl = NSURL.fileURLWithPath_isDirectory_(directory, True)
	panel.setDirectoryURL_(myUrl)
	panel.setNameFieldStringValue_(filename)
	NSApp.activateIgnoringOtherApps_(True)
	ret_value = panel.runModal()
	if ret_value:
		return panel.filename()
	else:
		return ''

def createPDFDocumentWithPath(path):
	return Quartz.CGPDFDocumentCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))

def imposition(pageRange):
	for i in range(1, (len(pageRange)/2), 2):
		# First we do recto
		imposedOrder.append(pageRange[i*-1])
		imposedOrder.append(pageRange[i-1])
		# And now we do verso
		imposedOrder.append(pageRange[i])
		imposedOrder.append(pageRange[(i+1)*-1])

	return imposedOrder

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

def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context	

# MAIN 
def main(argv):
	(title, options, pathToFile) = argv[:]
	shortName = os.path.splitext(title)[0]
	# writeFilename = os.path.join(destination, shortName + suffix)
	writeFilename = save_dialog(destination, shortName + suffix)
	writeFilename = writeFilename.encode('utf-8')
	leftPage = copy.deepcopy(sheetSize)
	shift = sheetSize[1][0]/2
	leftPage[1][0] = shift
	rightPage = copy.deepcopy(leftPage)
	rightPage[0][0] = shift
	blanks = 0

# Initiate new PDF, get source PDF data, number of pages.
	writeContext = Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, writeFilename, len(writeFilename), False), sheetSize, None)
	source = createPDFDocumentWithPath(pathToFile)
	totalPages = Quartz.CGPDFDocumentGetNumberOfPages(source)


# Add blank pages to round up to multiple of pages per sheet.
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
# If the source page number is 0, then move on without drawing.
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
    main(sys.argv[1:])