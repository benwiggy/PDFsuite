#!/usr/bin/python

"""
by Ben Byram-Wigfield
Takes an existing PDF and creates individual page documents
"""
import os, sys, objc
import Quartz as Quartz
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation)


# Creates a Context for drawing
def createOutputContextWithPath(path):
	return Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		Quartz.CGPDFContextClose(context)
		del context




def strip(filename):
	# 
	pdf = Quartz.CGPDFDocumentCreateWithProvider(Quartz.CGDataProviderCreateWithFilename(filename))
	numPages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)
	shortName = os.path.splitext(filename)[0]
	prefix = os.path.splitext(os.path.basename(filename))[0]
	try:
		os.mkdir(shortName)
	except:
		print "Can't create directory '%s'"%(shortName)
		sys.exit()
		
	# For each page, create a file
	for i in range (1, numPages+1):
		page = Quartz.CGPDFDocumentGetPage(pdf, i)
		if page:
	#Get mediabox
			mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
			outFile = shortName +"//" + prefix + " %03d.pdf"%i
	# get context?
			writeContext = createOutputContextWithPath(outFile)
			Quartz.CGContextBeginPage(writeContext, mediaBox)
			Quartz.CGContextDrawPDFPage(writeContext, page)
			Quartz.CGContextEndPage(writeContext)
			contextDone(writeContext)


if __name__ == "__main__":
	for filename in sys.argv[1:]:
		strip(filename)