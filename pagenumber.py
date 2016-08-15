#!/usr/bin/python
# coding: utf-8
# This script places page numbers on facing pages. Options for position, size, font are below.
# With thanks to user Hiroto on Apple Support Communities.

import sys
import os
import math
import Quartz.CoreGraphics as CG
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)

verbose = False

# Creates a PDF Object from incoming file.
def createPDFDocumentFromPath(path):
	global verbose
	if verbose:
		print "Creating PDF document from file %s" % (path)
	return CG.CGPDFDocumentCreateWithURL(CG.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))
	
# Creates a Context for drawing
def createOutputContextWithPath(path):
	global verbose
	if verbose:
		print "Setting %s as the destination." % (path)
	return CG.CGPDFContextCreateWithURL(CG.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		CG.CGPDFContextClose(context)
		del context

def drawWatermarkText(ctx, line, xOffset, yOffset, angle, scale, opacity):
    #   CGContextRef ctx
    #   CTLineRef line
    #   float xOffset, yOffset, angle ([degree]), scale, opacity ([0.0, 1.0])
    if line:
        rect = CTLineGetImageBounds(line, ctx)
        imageWidth = rect.size.width
        imageHeight = rect.size.height
        
        CG.CGContextSaveGState(ctx)
        CG.CGContextSetAlpha(ctx, opacity)
        CG.CGContextTranslateCTM(ctx, xOffset, yOffset)
        CG.CGContextScaleCTM(ctx, scale, scale)
        CG.CGContextTranslateCTM(ctx, imageWidth / 2, imageHeight / 2)
        CG.CGContextRotateCTM(ctx, angle * math.pi / 180)
        CG.CGContextTranslateCTM(ctx, -imageWidth / 2, -imageHeight / 2)
        CG.CGContextSetTextPosition(ctx, 0.0, 0.0);
        CTLineDraw(line, ctx);
        CG.CGContextRestoreGState(ctx)


if __name__ == '__main__':

	for filename in sys.argv[1:]:
		shortName = os.path.splitext(filename)[0]
		outFilename = shortName + " NUM.pdf"
		pdf = createPDFDocumentFromPath(filename)
		ctx = createOutputContextWithPath(outFilename)
		pages = CG.CGPDFDocumentGetNumberOfPages(pdf)


# OPTIONS: Set the RELATIVE distance from outside top corner of page;
# For other uses, set the angle, scale, and opacity of text
# Font must be the PostScript name (i.e. no spaces) (See Get Info in FontBook)
xOffset, yOffset, angle, scale, opacity = 45.0, 45.0, 0.0, 1.0, 1.0
font = CTFontCreateWithName('TimesNewRomanPSMT', 12.0, None)

if pdf:
    for i in range(1, (pages+1)):
        page = CG.CGPDFDocumentGetPage(pdf, i)
        if page:
            mbox = CG.CGPDFPageGetBoxRect(page, CG.kCGPDFMediaBox)
            if CG.CGRectIsEmpty(mbox): mbox = None
            CG.CGContextBeginPage(ctx, mbox)
            CG.CGContextDrawPDFPage(ctx, page)
            text = str(i)
            print i
            astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : font })
            line = CTLineCreateWithAttributedString(astr)
            x = CG.CGRectGetWidth(mbox)
            y = CG.CGRectGetHeight(mbox)
            y -= yOffset
            if i%2 == 1:
            	x = xOffset
            	drawWatermarkText(ctx, line, x, y, angle, scale, opacity)
            else:
            	x = x - xOffset
            	drawWatermarkText(ctx, line, x , y, angle, scale, opacity)
            

            CG.CGContextEndPage(ctx)
    del pdf
    contextDone(ctx)