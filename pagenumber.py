#!/usr/bin/python
# coding: utf-8
# This script places page numbers on facing pages. Options for position, size, font are below.
# With thanks to user Hiroto on Apple Support Communities.

import sys
import os
import math
from Quartz.CoreGraphics import (CGContextBeginPage, CGContextConcatCTM, CGContextDrawPDFPage, CGContextEndPage, CGContextRestoreGState, CGContextRotateCTM, CGContextSaveGState, CGContextScaleCTM, CGContextSetAlpha, CGContextSetTextPosition, CGContextTranslateCTM, CGContextTranslateCTM, CGContextTranslateCTM, CGPDFContextClose, CGPDFContextCreateWithURL, CGPDFDocumentCreateWithURL, CGPDFDocumentGetNumberOfPages, CGPDFDocumentGetPage, CGPDFPageGetBoxRect, CGPDFPageGetDrawingTransform, CGRectGetHeight, CGRectGetWidth, CGRectIsEmpty, CGRectMake, kCGPDFMediaBox)
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)

verbose = False

# Creates a PDF Object from incoming file.
def createPDFDocumentFromPath(path):
	global verbose
	if verbose:
		print "Creating PDF document from file %s" % (path)
	return CGPDFDocumentCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))
	
# Creates a Context for drawing
def createOutputContextWithPath(path):
	global verbose
	if verbose:
		print "Setting %s as the destination." % (path)
	return CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		CGPDFContextClose(context)
		del context

def drawWatermarkText(ctx, line, xOffset, yOffset, angle, scale, opacity):
    #   CGContextRef ctx
    #   CTLineRef line
    #   float xOffset, yOffset, angle ([degree]), scale, opacity ([0.0, 1.0])
    if line:
        rect = CTLineGetImageBounds(line, ctx)
        imageWidth = rect.size.width
        imageHeight = rect.size.height
        
        CGContextSaveGState(ctx)
        CGContextSetAlpha(ctx, opacity)
        CGContextTranslateCTM(ctx, xOffset, yOffset)
        CGContextScaleCTM(ctx, scale, scale)
        CGContextTranslateCTM(ctx, imageWidth / 2, imageHeight / 2)
        CGContextRotateCTM(ctx, angle * math.pi / 180)
        CGContextTranslateCTM(ctx, -imageWidth / 2, -imageHeight / 2)
        CGContextSetTextPosition(ctx, 0.0, 0.0);
        CTLineDraw(line, ctx);
        CGContextRestoreGState(ctx)


if __name__ == '__main__':

	for filename in sys.argv[1:]:
		shortName = os.path.splitext(filename)[0]
		outFilename = shortName + " NUM.pdf"
		pdf = createPDFDocumentFromPath(filename)
		ctx = createOutputContextWithPath(outFilename)
		pages = CGPDFDocumentGetNumberOfPages(pdf)


# OPTIONS: Set the RELATIVE distance from outside top corner of page;
# For other uses, set the angle, scale, and opacity of text
# Font must be the PostScript name (i.e. no spaces) (See Get Info in FontBook)
xOffset, yOffset, angle, scale, opacity = 45.0, 45.0, 0.0, 1.0, 1.0
font = CTFontCreateWithName('TimesNewRomanPSMT', 12.0, None)

if pdf:
    for i in range(1, pages+1):
        page = CGPDFDocumentGetPage(pdf, i + 1)
        if page:
            mbox = CGPDFPageGetBoxRect(page, kCGPDFMediaBox)
            if CGRectIsEmpty(mbox): mbox = None
            CGContextBeginPage(ctx, mbox)
            CGContextDrawPDFPage(ctx, page)
            text = str(i)
            astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : font })
            line = CTLineCreateWithAttributedString(astr)
            x = CGRectGetWidth(mbox)
            y = CGRectGetHeight(mbox)
            y -= yOffset
            if i%2 == 1:
            	x = xOffset
            	drawWatermarkText(ctx, line, x, y, angle, scale, opacity)
            else:
            	x = x - xOffset
            	drawWatermarkText(ctx, line, x , y, angle, scale, opacity)
            

            CGContextEndPage(ctx)
    del pdf
    contextDone(ctx)