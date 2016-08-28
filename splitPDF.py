#!/usr/bin/python

"""
by Ben Byram-Wigfield
Takes an existing PDF and creates individual page documents
"""
import os, sys, objc
import Quartz as CG
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation)


# Creates a Context for drawing
def createOutputContextWithPath(path):
	return CG.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, None)

# Closes the Context
def contextDone(context):
	if context:
		CG.CGPDFContextClose(context)
		del context




def strip(filename):
	# 
	pdf = CG.CGPDFDocumentCreateWithProvider(CG.CGDataProviderCreateWithFilename(filename))
	numPages = CG.CGPDFDocumentGetNumberOfPages(pdf)
	shortName = os.path.splitext(filename)[0]
	prefix = os.path.splitext(os.path.basename(filename))[0]
	try:
		os.mkdir(shortName)
	except:
		print "Can't create directory '%s'"%(shortName)
		sys.exit()
		
	# For each page, create a file
	for i in range (1, numPages+1):
		page = CG.CGPDFDocumentGetPage(pdf, i)
		if page:
	#Get mediabox
			mediaBox = CG.CGPDFPageGetBoxRect(page, CG.kCGPDFMediaBox)
			outFile = shortName +"//" + prefix + " %03d.pdf"%i
	# get context?
			ctx = createOutputContextWithPath(outFile)
			CG.CGContextBeginPage(ctx, mediaBox)
			CG.CGContextDrawPDFPage(ctx, page)
			CG.CGContextEndPage(ctx)
			contextDone(ctx)


if __name__ == "__main__":
	for filename in sys.argv[1:]:
		strip(filename)