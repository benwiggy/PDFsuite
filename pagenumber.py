#!/usr/bin/python
# coding: utf-8
# This script places page numbers on facing pages. Options for position, size, font are below.
# With thanks to user Hiroto on Apple Support Communities.

import sys
import os
import math
import Quartz.CoreGraphics as Quartz
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)

verbose = False

# Creates a PDF Object from incoming file.
def createPDFDocumentFromPath(path):
	global verbose
	if verbose:
		print "Creating PDF document from file %s" % (path)
	return Quartz.CGPDFDocumentCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))
	
# Creates a Context for drawing
def createOutputContextWithPath(path):
	global verbose
	if verbose:
		print "Setting %s as the destination." % (path)
	return Quartz.CGPDFContextCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context

def drawWatermarkText(writeContext, line, xOffset, yOffset, angle, scale, opacity):
    #   CGContextRef writeContext
    #   CTLineRef line
    #   float xOffset, yOffset, angle ([degree]), scale, opacity ([0.0, 1.0])
	if line:
		rect = CTLineGetImageBounds(line, writeContext)
		imageWidth = rect.size.width
		imageHeight = rect.size.height

		Quartz.CGContextSaveGState(writeContext)
		Quartz.CGContextSetAlpha(writeContext, opacity)
		Quartz.CGContextTranslateCTM(writeContext, xOffset, yOffset)
		Quartz.CGContextScaleCTM(writeContext, scale, scale)
		Quartz.CGContextTranslateCTM(writeContext, imageWidth / 2, imageHeight / 2)
		Quartz.CGContextRotateCTM(writeContext, angle * math.pi / 180)
		Quartz.CGContextTranslateCTM(writeContext, -imageWidth / 2, -imageHeight / 2)
		Quartz.CGContextSetTextPosition(writeContext, 0.0, 0.0);
		CTLineDraw(line, writeContext);
		Quartz.CGContextRestoreGState(writeContext)


if __name__ == '__main__':

	for filename in sys.argv[1:]:
		shortName = os.path.splitext(filename)[0]
		outFilename = shortName + " NUM.pdf"
		pdf = createPDFDocumentFromPath(filename)
		writeContext = createOutputContextWithPath(outFilename)
		pages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)


# OPTIONS: Set the RELATIVE distance from outside top corner of page;
# For other uses, set the angle, scale, and opacity of text
# Font must be the PostScript name (i.e. no spaces) (See Get Info in FontBook)
xOffset, yOffset, angle, scale, opacity = 45.0, 45.0, 0.0, 1.0, 1.0
font = CTFontCreateWithName('TimesNewRomanPSMT', 12.0, None)

if pdf:
	for i in range(1, (pages+1)):
		page = Quartz.CGPDFDocumentGetPage(pdf, i)
		if page:
			mbox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
			if Quartz.CGRectIsEmpty(mbox): mbox = None
			Quartz.CGContextBeginPage(writeContext, mbox)
			Quartz.CGContextDrawPDFPage(writeContext, page)
			text = str(i)
			print i
			astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : font })
			line = CTLineCreateWithAttributedString(astr)
			x = Quartz.CGRectGetWidth(mbox)
			y = Quartz.CGRectGetHeight(mbox)
			y -= yOffset
			if i == 1: # Don't put number on page 1
				pass
			elif i%2 == 1:
				textWidth = astr.size().width
				x = x - xOffset
				x = x - textWidth
				drawWatermarkText(writeContext, line, x , y, angle, scale, opacity)
			else:
				x = xOffset
				drawWatermarkText(writeContext, line, x, y, angle, scale, opacity)
				
			Quartz.CGContextEndPage(writeContext)
	del pdf
contextDone(writeContext)