#! /usr/bin/python
# coding=utf-8
#
# Tool to concatenate PDFs.
# Modified from the Apple script in /System/Library/Automator/Combine PDF Pages.action
# Optimized for speed (importing * takes many seconds); shuffle and verbose modes removed.
# Joins all PDF files given as arguments. No sanity checking: if used in Automator, no need.

import sys
import os
from CoreFoundation import (CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)
import Quartz as Quartz

def createPDFDocumentWithPath(path):
	return Quartz.CGPDFDocumentCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))


def writePageFromDoc(writeContext, doc, pageNum):

	page = Quartz.CGPDFDocumentGetPage(doc, pageNum)
	if page:
		mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
		if Quartz.CGRectIsEmpty(mediaBox):
			mediaBox = None

		Quartz.CGContextBeginPage(writeContext, mediaBox)
		Quartz.CGContextDrawPDFPage(writeContext, page)
		Quartz.CGContextEndPage(writeContext)


def append(writeContext, docs, maxPages):

	for doc in docs:
		for pageNum in xrange(1, maxPages + 1) :
			writePageFromDoc(writeContext, doc, pageNum)


def getFilename(filepath, basename):
	fullname = basename + ".pdf"
	i=0
	while os.path.exists(os.path.join(filepath, fullname)):
		i += 1
		fullname = basename + " %02d.pdf"%i
	return os.path.join(filepath, fullname)


def main(incomingFiles):

	# Set the output file
	prefix = os.path.dirname(incomingFiles[0])
	filename = "Combined"
	outfile = getFilename(prefix, filename)
	
	# The PDF context we will draw into to create a new PDF
	writeContext = Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, outfile, len(outfile), False), None, None)
	
	if writeContext:
		# create PDFDocuments for all of the files.
		docs = map(createPDFDocumentWithPath, incomingFiles)
		
		# find the maximum number of pages.
		maxPages = 0
		for doc in docs:

			if Quartz.CGPDFDocumentGetNumberOfPages(doc) > maxPages:
				maxPages = Quartz.CGPDFDocumentGetNumberOfPages(doc)
	
		append(writeContext, docs, maxPages)
		
		Quartz.CGPDFContextClose(writeContext)
		del writeContext
		#CGContextRelease(writeContext)




if __name__ == "__main__":
	main(sys.argv[1:])
