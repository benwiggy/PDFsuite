#!/usr/bin/env python3

# PAGE LAYOUT : Adds user-definable objects to a PDF page.
# by Ben Byram-Wigfield v. 0.5
# TO DO: 
# Add bitmap image or PDF file.
# Include Rounded Rectangles and other BezierPaths.

import os, sys
import Quartz as Quartz
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)
from math import pi as PI

pageSize = [[0.,0.], [595.28, 841.88]] # A4
whiteSwatch = [1.,1.,1.]
redSwatch = [1.,0.,0.]
blueSwatch = [0.,0.,1.]
greenSwatch = [0.,1.,0.]
blackSwatch = [0.,0.,0.]

# Use inches instead of points e.g. "inch(1.5)"
def inch(x):
	return 72.0*x

# Use centimetres instead of points e.g. "cm(2.5)"
def cm(x):
	return 28.25*x


def makeRectangle(x, y, xSize, ySize, color, alpha):
	red, green, blue = color[:]
	Quartz.CGContextSetRGBFillColor (writeContext, red, green, blue, alpha)
	Quartz.CGContextFillRect (writeContext, Quartz.CGRectMake(x, y, xSize, ySize))
	return


def centerText(y, text, font, pointSize):
	typeStyle = CTFontCreateWithName(font, pointSize, None)
	astr = CFAttributedStringCreate(kCFAllocatorDefault, text, { kCTFontAttributeName : typeStyle })
	line = CTLineCreateWithAttributedString(astr)
	textWidth = astr.size().width

	if line:
		x = (pageSize[1][0]-textWidth)/2
		# Quartz.CGContextSetAlpha(writeContext, opacity)
		Quartz.CGContextSetTextPosition(writeContext, x, y)
		CTLineDraw(line, writeContext)

	return
	
def line(x, y, xSize, ySize, stroke, color, alpha):
	red, green, blue = color[:]
	Quartz.CGContextSetLineWidth(writeContext, stroke)
	Quartz.CGContextSetRGBStrokeColor(writeContext, red, green, blue, alpha)
	Quartz.CGContextMoveToPoint(writeContext, x, y)
	Quartz.CGContextAddLineToPoint(writeContext, x+xSize, y+ySize)
	Quartz.CGContextStrokePath(writeContext)
	return

def circle(x, y, radius, color, alpha):
	red, green, blue = color[:]
	Quartz.CGContextSetRGBStrokeColor(writeContext, red, green, blue, alpha)
	Quartz.CGContextSetRGBFillColor(writeContext, red, green, blue, alpha)
	Quartz.CGContextAddArc(writeContext, x, y, radius, 0, 2*PI, 1)
	Quartz.CGContextClosePath(writeContext)
	Quartz.CGContextFillPath(writeContext)
	Quartz.CGContextSetLineWidth(writeContext, 2)
	Quartz.CGContextStrokePath(writeContext)
	return

def addImage(x, y, path):
	# CGContextDrawImage(writeContext, rect, CGImageRef image)
	return

def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context	

def main(argv):
	global writeContext
	writeFilename = (os.path.expanduser("~/Desktop/Test.pdf")).encode('UTF-8')
	writeContext = Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, writeFilename, len(writeFilename), False), pageSize, None)
	Quartz.CGContextBeginPage(writeContext, pageSize)


#  HERE IS WHERE YOU WRITE YOUR PAGE!
# ------------------------------------------------------------------

	circle(100,100,100, blackSwatch, 0.5)
	circle(100,750,100, blackSwatch, 0.5)
	makeRectangle(100., 100., 400., 50., redSwatch, 0.75)
	makeRectangle(100., 700., 400., 50., greenSwatch, 0.75)
	line(100, 300, 400, 200, 12, blueSwatch, 1)
	circle(300.,400., 150., blueSwatch, 0.5)
	centerText(600, "Sample Text", "Helvetica-Bold", 12.0)
	
# ------------------------------------------------------------------	

	Quartz.CGContextEndPage(writeContext)
		# Do tidying up
	contextDone(writeContext)	

if __name__ == "__main__":
    main(sys.argv[1:])