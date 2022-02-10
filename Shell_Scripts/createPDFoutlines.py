#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CREATE PDF OUTLINES v.1.0 : Add a simple list of Bookmarks to a PDF.
# by Ben Byram-Wigfield 

from Foundation import  NSURL, NSString
import Quartz as Quartz
import sys

# You will need to change these filepaths to a local test pdf and an output file.
infile = "/path/to/file.pdf"
outfile = '/path/to/output.pdf'

def getOutline(page, label):
	# Create Destination
	myPage = myPDF.pageAtIndex_(page)
	pageSize = myPage.boundsForBox_(Quartz.kCGPDFMediaBox)
	x = 0
	y = Quartz.CGRectGetMaxY(pageSize)
	pagePoint = Quartz.CGPointMake(x,y)
	myDestination = Quartz.PDFDestination.alloc().initWithPage_atPoint_(myPage, pagePoint)
	myLabel = NSString.stringWithString_(label)
	myOutline = Quartz.PDFOutline.alloc().init()
	myOutline.setLabel_(myLabel)
	myOutline.setDestination_(myDestination)
	return myOutline

pdfURL = NSURL.fileURLWithPath_(infile)
myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
if myPDF:
	# Create Outlines. Add the Page Index (from 0) and label in pairs here:
	myTableOfContents = [
		(0, 'Page 1'), 
		(1, 'Page 2'),
		(2, 'Page 3')
		]
	allMyOutlines = []
	for index, outline in myTableOfContents:
		allMyOutlines.append(getOutline(index, outline))

	# Create a root Outline and add each outline
	rootOutline = Quartz.PDFOutline.alloc().init()
	for index, value in enumerate(allMyOutlines):
		rootOutline.insertChild_atIndex_(value, index)
	myPDF.setOutlineRoot_(rootOutline)
	myPDF.writeToFile_(outfile)

	
