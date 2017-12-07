#!/usr/bin/python
# coding: utf-8
# This script stamps "N Out Of X" on the first page of all PDF documents passed to it,
# where N is the sequential number of each document and X is the total.
# Options for position, size, font are below.
# With thanks to user Hiroto on Apple Support Communities.

import sys
import os
import math
import Quartz.CoreGraphics as Quartz
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)



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

def drawWatermarkText(writeContext, line, xOffset, yOffset, angle, scale, opacity):
	if line:
		rect = CTLineGetImageBounds(line, writeContext)
		imageWidth = rect.size.width
		imageHeight = rect.size.height

		Quartz.CGContextSaveGState(writeContext)
		Quartz.CGContextSetAlpha(writeContext, opacity)
		Quartz.CGContextTranslateCTM(writeContext,  xOffset, yOffset)
		Quartz.CGContextTranslateCTM(writeContext, imageWidth / 2, imageHeight / 2)
		Quartz.CGContextRotateCTM(writeContext, angle * math.pi / 180)
		Quartz.CGContextTranslateCTM(writeContext, -imageWidth / 2, -imageHeight / 2)
		Quartz.CGContextScaleCTM(writeContext, scale, scale)
		Quartz.CGContextSetTextPosition(writeContext, 0.0, 0.0)
		CTLineDraw(line, writeContext)
		Quartz.CGContextRestoreGState(writeContext)


if __name__ == '__main__':


# OPTIONS: Set the distance in points from bottom left corner of page;
# For other uses, set the angle, scale, and opacity of text
# Font must be the PostScript name (i.e. no spaces) (See Get Info in FontBook)
	xOffset, yOffset, angle, scale, opacity = 45.0, 800.0, 0.0, 1.0, 1.0
	font = CTFontCreateWithName('Helvetica-Bold', 12.0, None)


	for index, filename in enumerate(sys.argv[1:], start = 1):
# Get path, create new folder
		totalCount = len(sys.argv[1:])
		text = str(index) + "/" + str(totalCount)
		if index == 1:
			dirPath = os.path.dirname(filename)
			location = os.path.join(dirPath, "Indexed")
			try:
				os.mkdir(location)
			except:
				print "Can't create directory '%s'"%(location)
				sys.exit()
		nameOnly = os.path.basename(filename)
		outFilename = os.path.join(location, nameOnly)
		pdf = createPDFDocumentFromPath(filename)
		pages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)
		writeContext = createOutputContextWithPath(outFilename)

# Write page 1 with the added text
		if pdf:
			page = Quartz.CGPDFDocumentGetPage(pdf, 1)
			if page:
				mbox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
			#	if Quartz.CGRectIsEmpty(mbox): mbox = None
				Quartz.CGContextBeginPage(writeContext, mbox)
				Quartz.CGContextDrawPDFPage(writeContext, page)
				astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : font })
				line = CTLineCreateWithAttributedString(astr)
				drawWatermarkText(writeContext, line, xOffset , yOffset, angle, scale, opacity)
				Quartz.CGContextEndPage(writeContext)

# Write out the rest of the pages				
			for i in range(2, (pages+1)):
				page = Quartz.CGPDFDocumentGetPage(pdf, i)
				if page:
					Quartz.CGContextBeginPage(writeContext, mbox)
					Quartz.CGContextDrawPDFPage(writeContext, page)
					Quartz.CGContextEndPage(writeContext)
		del pdf
	contextDone(writeContext)