#! /usr/bin/python
# coding=utf-8
# Produces new PDF file with all pages rotated by 90 degrees.
# by Ben Byram-Wigfield v1.1

# This graphically transforms the page, rather the easier method of just changing the rotation
# value associated with each page.
#
import sys
import os
import Quartz as Quartz

from CoreFoundation import (CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)


# Creates a PDF Object from incoming file.
def createPDFDocumentFromPath(path):
	return Quartz.CGPDFDocumentCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))
	
# Creates a Context for drawing
def createOutputContextWithPath(path):
	return Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context

	
def writePageFromDoc(writeContext, doc, pageNum, angle):

	page = Quartz.CGPDFDocumentGetPage(doc, pageNum)
	if page:
		mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
		if Quartz.CGRectIsEmpty(mediaBox):
			mediaBox = None
		
		x = Quartz.CGRectGetWidth(mediaBox)
		y = Quartz.CGRectGetHeight(mediaBox)
		mediaBox = Quartz.CGRectMake(0, 0, y, x)
			
		Quartz.CGContextBeginPage(writeContext, mediaBox)

		Quartz.CGContextConcatCTM(writeContext, Quartz.CGPDFPageGetDrawingTransform(page, Quartz.kCGPDFMediaBox, mediaBox, angle, True))
		Quartz.CGContextDrawPDFPage(writeContext, page)
		Quartz.CGContextEndPage(writeContext)

	
		
if __name__ == '__main__':

	for filename in sys.argv[1:]:

		shortName = os.path.splitext(filename)[0]
		outFilename = shortName + "+90.pdf"
		pdf = createPDFDocumentFromPath(filename)
		writeContext = createOutputContextWithPath(outFilename)
		pages = Quartz.CGPDFDocumentGetNumberOfPages (pdf)	
		for p in range(1, pages+1):
			writePageFromDoc(writeContext, pdf, p, 90)

	contextDone(writeContext)
