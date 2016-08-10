#! /usr/bin/python
#

#
import sys
import os
import getopt
import tempfile
import shutil
from Quartz.CoreGraphics import *

verbose = True

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

	
def writePageFromDoc(writeContext, doc, pageNum, angle):

	global verbose
	page = CGPDFDocumentGetPage(doc, pageNum)
	if page:
		mediaBox = CGPDFPageGetBoxRect(page, kCGPDFMediaBox)
		if CGRectIsEmpty(mediaBox):
			mediaBox = None
		
		x = CGRectGetWidth(mediaBox)
		y = CGRectGetHeight(mediaBox)
		mediaBox = CGRectMake(0, 0, y, x)
			
		CGContextBeginPage(writeContext, mediaBox)

		CGContextConcatCTM(writeContext, CGPDFPageGetDrawingTransform(page, kCGPDFMediaBox, mediaBox, angle, True))
		CGContextDrawPDFPage(writeContext, page)
		CGContextEndPage(writeContext)
		if verbose:
			print "Copied page %d from %s" % (pageNum, doc)
	
		
if __name__ == '__main__':

	for filename in sys.argv[1:]:

		shortName = os.path.splitext(filename)[0]
		outFilename = shortName + "+90.pdf"
		pdf = createPDFDocumentFromPath(filename)
		writeContext = createOutputContextWithPath(outFilename)
		pages = CGPDFDocumentGetNumberOfPages (pdf)
		if verbose:	print pages
	
		for p in range(1, pages+1):
			writePageFromDoc(writeContext, pdf, p, 90)

	contextDone(writeContext)
