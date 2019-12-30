#!/usr/bin/env python
# coding: utf-8

# PAGE NUMBER v.1.8
# This script places page numbers on facing pages (excluding page 1). Options for position, size, font are below.
# By Ben Byram-Wigfield.
# With thanks to user Hiroto on Apple Support Communities.

import sys, os, math
import Quartz as Quartz
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault, NSURL)
from AppKit import NSFontManager

# Creates a PDF Object from incoming file.
def createPDFDocumentWithPath(path):
	# return Quartz.CGPDFDocumentCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))
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

# Check that the selected font is active, else use Helvetica Bold.
def selectFont(typeface, pointSize):
	manager = NSFontManager.sharedFontManager()
	fontList = list(manager.availableFonts()) 
	if typeface not in fontList:
		typeface = 'Helvetica-Bold'

	return CTFontCreateWithName(typeface, pointSize, None)

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
		pdf = createPDFDocumentWithPath(filename)
		metaDict = getDocInfo(filename)
		writeContext = createOutputContextWithPath(outFilename, metaDict)
		pages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)

		# OPTIONS: Set the RELATIVE distance from outside top corner of page;
		# For other uses, set the angle, scale, and opacity of text
		# Font must be the PostScript name (i.e. no spaces) (See Get Info in FontBook)
		xOffset, yOffset, angle, scale, opacity = 45.0, 45.0, 0.0, 1.0, 1.0
		font = selectFont('TimesNewRomanPSMT', 12.0)

		if pdf:
			for i in range(1, (pages+1)):
				page = Quartz.CGPDFDocumentGetPage(pdf, i)
				if page:
					mbox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
					if Quartz.CGRectIsEmpty(mbox): mbox = None
					Quartz.CGContextBeginPage(writeContext, mbox)
					Quartz.CGContextDrawPDFPage(writeContext, page)
					text = str(i)
					astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : font })
					line = CTLineCreateWithAttributedString(astr)
					x = Quartz.CGRectGetWidth(mbox)
					y = Quartz.CGRectGetHeight(mbox)
					y -= yOffset
					if i == 1: # Don't put number on page 1
						pass
					elif i%2 == 1: # Move right hand number in by its own width.
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
