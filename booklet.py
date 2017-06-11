#! /usr/bin/python

# ----------------------------------------------------------------
# PDF Booklet Imposition Script for MacOS
# by Ben Byram-Wigfield v.1.1
# Feel free to use, modify and pass on with acknowledgement.

# 1. Set OPTIONS below for output folder, sheet size, and creep
# 2. Install into ~/Library/PDF Services
# 3. It will then appear as an option in the PDF button of the Print dialog.
# (if it has executable flags set.)

# Script now checks for page rotation.
# Still to do: 
# 1. Allow for multiple booklets from one PDF file.
# ----------------------------------------------------------------
import sys
import os
import copy
import getopt
import Quartz as Quartz
from CoreFoundation import (CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)

# For debugging, turn this on.
verbose = False

# define Page and Sheet Sizes in points
A4 = [[0,0], [841.88, 595.28]]
A3 = [[0,0], [1190.55, 841.88]]

USLetter = [[0,0], [792, 612]]
Tabloid = [[0,0], [1224, 792]]
# ----------------------------------------------------------------
# OPTIONS. Set the location for saving the files. Must end with a /
destination = os.path.expanduser("~/Desktop/")
# Set file suffix
suffix = " booklet.pdf"

creep = 0.5 # in points. NB: Eventually, the pages will collide.

# Change this to one of the sizes listed above, if you want.
sheetSize = A3
# ----------------------------------------------------------------
# For future: non-zero value will make booklets no bigger than _signature
signature = 0 
# ----------------------------------------------------------------
# Dont change this.
pagesPerSheet = 4
leftPage = copy.deepcopy(sheetSize)
shift = sheetSize[1][0]/2
leftPage[1][0] = shift
rightPage = copy.deepcopy(leftPage)
rightPage[0][0] = shift


# FUNCTIONS

def createPDFDocumentWithPath(path):
	global verbose
	if verbose:
		print "Creating PDF document from file %s" % (path)
	return Quartz.CGPDFDocumentCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))


def pageCount(pdfPath):
	global verbose
	if verbose:
		print "Getting number of pages..."
		
	pdf = Quartz.CGPDFDocumentCreateWithProvider(Quartz.CGDataProviderCreateWithFilename (pdfPath))
	return pdf.getNumberOfPages()
    
def imposition(pages):
	global verbose
	blanks = 0
	UnsortedOrder = range(1, pages+1)
	if pages%pagesPerSheet:
		blanks = pagesPerSheet - (pages%pagesPerSheet)
		for i in range(blanks):
			UnsortedOrder.append(0)
	imposedOrder = []
	for i in range(1, (pages+blanks)/2+1, 2):
		# First we do recto
		imposedOrder.append(UnsortedOrder[i*-1])
		imposedOrder.append(UnsortedOrder[i-1])
		# And now we do verso
		imposedOrder.append(UnsortedOrder[i])
		imposedOrder.append(UnsortedOrder[(i+1)*-1])

	if verbose:
		print imposedOrder	
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
		print(displayAngle, rotValue)
	return displayAngle	

def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context
		
# MAIN 
def main(argv):
	(title, options, pathToFile) = argv[0:3]
	global verbose
	writeContext = None
	shortName = os.path.splitext(title)[0]
	writeFilename = destination + shortName + suffix
	writeContext = Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, writeFilename, len(writeFilename), False), sheetSize, None)

# Initiate new PDF, get source PDF, number of pages.
	source = createPDFDocumentWithPath(pathToFile)
	pageNo = Quartz.CGPDFDocumentGetNumberOfPages(source)

# Get imposed page order
	imposedOrder = imposition(pageNo)

# Place pages on sheet
	pagesPerSide = pagesPerSheet/2
	Sides = len(imposedOrder) / pagesPerSide

# For each side of the sheet, we must...
# ... create a PDF page, take two source pages and place them differently, then close the page.
# If the source page number is 0, then move on without drawing.
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