#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CREATE PDF OUTLINES v.1.1 : Add a simple list of Bookmarks to a PDF.

from Foundation import  NSURL, NSString
import Quartz as Quartz
import sys

# You will need to change these filepaths to a local test pdf and an output file.
infile = "/Users/Ben/Desktop/Blow Salvator.pdf"
outfile = '/Users/Ben/Desktop/Blow SalvatorX2.pdf'

def makeOutline(page, label):
	# Create Destination
	myPage = myPDF.pageAtIndex_(page)
	pageSize = myPage.boundsForBox_(Quartz.kCGPDFMediaBox)
	x = 50
	y = Quartz.CGRectGetMaxY(pageSize)
	pagePoint = Quartz.CGPointMake(x,y)
	myDestination = Quartz.PDFDestination.alloc().initWithPage_atPoint_(myPage, pagePoint)
	myLabel = NSString.stringWithString_(label)
	myOutline = Quartz.PDFOutline.alloc().init()
	myOutline.setLabel_(myLabel)
	myOutline.setDestination_(myDestination)
	return myOutline


if __name__ == "__main__":

	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		# Create Outlines. Add the Page Index (from 0) and label in pairs here:
		myTableOfContents = [
			(0, 'Page 1')
			]
		allMyOutlines = []
		for index, outline in myTableOfContents:
			allMyOutlines.append(makeOutline(index, outline))

		# Create a root Outline and add each outline
		rootOutline = Quartz.PDFOutline.alloc().init()
		
		#for index, eachOutline in enumerate(allMyOutlines):
		
		rootOutline.insertChild_atIndex_(allMyOutlines[0], 0)
		myPDF.setOutlineRoot_(rootOutline)
		myPDF.writeToFile_(outfile)

	