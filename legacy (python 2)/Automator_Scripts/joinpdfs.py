#! /usr/bin/env python
# coding=utf-8
#
# JOINPDFS v2.2 : Tool to concatenate PDFs.
# New tool built from the ground up using PDFKit, instead of Core Graphics.
# Now writes Table of Contents for each file added; importing existing ToCs in each file!
# by Ben Byram-Wigfield

import sys
import os.path
from CoreFoundation import (CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault, NSURL, NSString)
import Quartz as Quartz

def createPDFDocumentWithPath(path):
	pdfURL = NSURL.fileURLWithPath_(path)
	if pdfURL:
		return Quartz.PDFDocument.alloc().initWithURL_(pdfURL)

def getFilename(filepath, basename):
	fullname = basename + ".pdf"
	i=0
	while os.path.exists(os.path.join(filepath, fullname)):
		i += 1
		fullname = basename + " %02d.pdf"%i
	return os.path.join(filepath, fullname)


def getOutline(page, label, pageObject):
	pageSize = pageObject.boundsForBox_(Quartz.kCGPDFMediaBox)
	x = 0
	y = Quartz.CGRectGetHeight(pageSize)
	pagePoint = Quartz.CGPointMake(x,y-1)
	myDestination = Quartz.PDFDestination.alloc().initWithPage_atPoint_(pageObject, pagePoint)
	myLabel = NSString.stringWithString_(label)
	myOutline = Quartz.PDFOutline.alloc().init()
	myOutline.setLabel_(myLabel)
	myOutline.setDestination_(myDestination)
	return myOutline

def join(incomingFiles):

	# Set the output file location and name.
	prefix = os.path.dirname(incomingFiles[0])
	filename = "Combined"
	outfile = getFilename(prefix, filename)
	# Load in the first PDF file, to which the rest will be added.
	firstPDF = createPDFDocumentWithPath(incomingFiles[0])
	outlineIndex = 0
	rootOutline = Quartz.PDFOutline.alloc().init()
	firstLabel = os.path.basename(incomingFiles[0])
	firstPage = firstPDF.pageAtIndex_(0)
	firstOutline = getOutline(0, firstLabel, firstPage)
	# Check and copy existing Outlines into new structure.
	existingOutline = firstPDF.outlineRoot()
	if existingOutline:
		i=0
		while i < (existingOutline.numberOfChildren()):
			childOutline = existingOutline.childAtIndex_(i)
			firstOutline.insertChild_atIndex_(childOutline, i)
			i +=1
	rootOutline.insertChild_atIndex_(firstOutline, outlineIndex)

	
	# create PDFDocument object for the remaining files.
	pdfObjects = map(createPDFDocumentWithPath, incomingFiles[1:])
	for index, doc in enumerate(pdfObjects):
		if doc:	
			pages = doc.pageCount()
			pageIndex = firstPDF.pageCount()
			tocLabel = os.path.basename(incomingFiles[index+1])
			for p in range(0, pages):
				page = doc.pageAtIndex_(p)
				firstPDF.insertPage_atIndex_(page, pageIndex+p)
				if p == 0:
					outline = getOutline(pageIndex, tocLabel, page)
					existingOutline = doc.outlineRoot()
					if existingOutline:
						i=0
						while i < (existingOutline.numberOfChildren()):
							childOutline = existingOutline.childAtIndex_(i)
							outline.insertChild_atIndex_(childOutline, i)
							i +=1
						
			rootOutline.insertChild_atIndex_(outline, index+1)
	# Add the root Outline to the first PDF.
	firstPDF.setOutlineRoot_(rootOutline)				
	firstPDF.writeToFile_(outfile)			

if __name__ == "__main__":
	if len(sys.argv) > 1:
		join(sys.argv[1:])
