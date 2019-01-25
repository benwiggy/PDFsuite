#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Merge v. 0.1
# Merges two PDFs 

import sys
import os
import Quartz as Quartz
from Foundation import NSURL, kCFAllocatorDefault
from AppKit import NSSavePanel, NSApp

# OPTIONS
# Change this filepath to the PDF you want to use a letterhead / template:
watermark = os.path.expanduser("/System/Library/Assistant/UIPlugins/FMF.siriUIBundle/Contents/Resources/person.pdf")
destination = os.path.expanduser("~/Desktop") # Default destination
suffix = " wm.pdf" # Use ".pdf" if no actual suffix required.

# FUNCTIONS

def save_dialog(directory, filename):
	panel = NSSavePanel.savePanel()
	panel.setTitle_("Save PDF booklet")
	myUrl = NSURL.fileURLWithPath_isDirectory_(directory, True)
	panel.setDirectoryURL_(myUrl)
	panel.setNameFieldStringValue_(filename)
	NSApp.activateIgnoringOtherApps_(True)
	ret_value = panel.runModal()
	if ret_value:
		return panel.filename()
	else:
		return ''

# Loads in PDF document
def createPDFDocumentWithPath(path):
	return Quartz.CGPDFDocumentCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))

# Creates a Context for drawing
def createOutputContextWithPath(path, dictarray):
	return Quartz.CGPDFContextCreateWithURL(Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False), None, dictarray)
	
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

def main(argv):
	(title, options, pathToFile) = argv[:]
	shortName = os.path.splitext(title)[0]
	# If you want to save to a consistent location, use:
	# writeFilename = os.path.join(destination, shortName + suffix)
	writeFilename = save_dialog(destination, shortName + suffix)
	writeFilename = writeFilename.encode('utf-8')
	shortName = os.path.splitext(pathToFile)[0]
	metaDict = getDocInfo(pathToFile)
	writeContext = createOutputContextWithPath(writeFilename, metaDict)
	readPDF = createPDFDocumentWithPath(pathToFile)
	mergePDF = createPDFDocumentWithPath(watermark)
	
	if writeContext != None and readPDF != None:
		numPages = Quartz.CGPDFDocumentGetNumberOfPages(readPDF)
		for pageNum in xrange(1, numPages + 1):	
			page = Quartz.CGPDFDocumentGetPage(readPDF, pageNum)
			mergepage = Quartz.CGPDFDocumentGetPage(mergePDF, 1)
			if page:
				mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				if Quartz.CGRectIsEmpty(mediaBox):
					mediaBox = None			
				Quartz.CGContextBeginPage(writeContext, mediaBox)	
				Quartz.CGContextSetBlendMode(writeContext, Quartz.kCGBlendModeOverlay)
				Quartz.CGContextDrawPDFPage(writeContext, page)
				Quartz.CGContextDrawPDFPage(writeContext, mergepage)
				Quartz.CGContextEndPage(writeContext)
		Quartz.CGPDFContextClose(writeContext)
		del writeContext
			
	else:
		print "A valid input file and output file must be supplied."
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv[1:])
