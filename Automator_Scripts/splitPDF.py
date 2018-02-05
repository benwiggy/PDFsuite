#!/usr/bin/python
# coding=utf-8
"""
SPLITPDF v1.3 : Takes an existing PDF and creates individual page documents in a new folder.
by Ben Byram-Wigfield 

"""
import os, sys
import Quartz as Quartz
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, NSURL)

# Creates a Context for drawing
def createOutputContextWithPath(path, dictarray):
	return Quartz.CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, dictarray)

# Gets DocInfo from input file to pass to output.
def getDocInfo(file):
	file = file.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(file)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	return pdfDoc.documentAttributes()

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
	metaDict = getDocInfo(filename)
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
			writeContext = createOutputContextWithPath(outFile, metaDict)
			Quartz.CGContextBeginPage(writeContext, mediaBox)
			Quartz.CGContextDrawPDFPage(writeContext, page)
			Quartz.CGContextEndPage(writeContext)
			contextDone(writeContext)

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		strip(filename)