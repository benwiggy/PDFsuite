#!/usr/bin/python
# coding: utf-8

# WATERMARK: Superimposed text on pages of PDF documents.
# By Ben Byram-Wigfield v1.2
# Options for position, size, font, text and opacity are below.
# With thanks to user Hiroto on Apple Support Communities.

import sys, os, math
import Quartz.CoreGraphics as Quartz
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)
from AppKit import NSFontManager


# Creates a PDF Object from incoming file.
def createPDFDocumentFromPath(path):
	return Quartz.CGPDFDocumentCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))
	
# Creates a Context for drawing
def createOutputContextWithPath(path):
	return Quartz.CGPDFContextCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context

def drawWatermarkText(writeContext, line, xOffset, yOffset, angle, opacity):
	if line:
		rect = CTLineGetImageBounds(line, writeContext)
		imageWidth = rect.size.width
		imageHeight = rect.size.height
		Quartz.CGContextSaveGState(writeContext)
		Quartz.CGContextSetAlpha(writeContext, opacity)
		Quartz.CGContextTranslateCTM(writeContext,  xOffset, yOffset)
		Quartz.CGContextRotateCTM(writeContext, angle * math.pi / 180)
		Quartz.CGContextSetTextPosition(writeContext, 0.0, 0.0)
		CTLineDraw(line, writeContext)
		Quartz.CGContextRestoreGState(writeContext)
	# return

# Check that the selected font is active, else use Helvetica Bold.
def selectFont(typeface, pointSize):
	manager = NSFontManager.sharedFontManager()
	fontList = list(manager.availableFonts()) 
	if typeface not in fontList:
		typeface = 'Helvetica-Bold'

	return CTFontCreateWithName(typeface, pointSize, None)

def getFilename(filepath, suffix):
	fullname = filepath + suffix + ".pdf"
	i=0
	while os.path.exists(fullname):
		i += 1
		fullname = filepath + suffix + " %02d.pdf"%i
	return fullname

if __name__ == '__main__':

# OPTIONS: Set the distance from bottom left of page;
# Set the angle and opacity of text
# Font must be the PostScript name (i.e. no spaces) (See Get Info in FontBook)
	xOffset, yOffset, angle, opacity = 110.0, 200.0, 45.0, 0.5
	font = selectFont('Helvetica-Bold', 150.0)
	text = "SAMPLE"

	for filename in sys.argv[1:]:
		shortName = os.path.splitext(filename)[0]
		outFilename = getFilename(shortName, " WM")
		pdf = createPDFDocumentFromPath(filename)
		writeContext = createOutputContextWithPath(outFilename)
		pages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)

		if pdf:
			for i in range(1, (pages+1)):
				page = Quartz.CGPDFDocumentGetPage(pdf, i)
				if page:
					mbox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				#	if Quartz.CGRectIsEmpty(mbox): mbox = None
					Quartz.CGContextBeginPage(writeContext, mbox)
					Quartz.CGContextDrawPDFPage(writeContext, page)
					astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : font })
					line = CTLineCreateWithAttributedString(astr)
					drawWatermarkText(writeContext, line, xOffset , yOffset, angle, opacity)
					Quartz.CGContextEndPage(writeContext)
	del pdf
contextDone(writeContext)