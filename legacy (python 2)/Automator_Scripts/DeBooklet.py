#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DeBooklet v.1.1 : Split page spreads into separate pages.
# by Ben Byram-Wigfield v1.0

# Doesn't sort the pages.
# Files produced are 'quite large' as some residual data from the cropped area remains.

import sys
import os
from Quartz import PDFDocument, kPDFDisplayBoxMediaBox, CGRectEqualToRect, CGRectMake
from CoreFoundation import NSURL

mediabox = kPDFDisplayBoxMediaBox
# Set to False if you don't want page 1 split.
doPageOne = True
	
def debooklet(filename):
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + " paged.pdf"
	
	# If running python2, uncomment the following line:
	# filename = filename.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(filename)
	leftPDF = PDFDocument.alloc().initWithURL_(pdfURL)
	rightPDF = PDFDocument.alloc().initWithURL_(pdfURL)
	newPDF = PDFDocument.alloc().init()
	if leftPDF:
		if not(doPageOne):
			leftPage = leftPDF.pageAtIndex_(0)
			newPDF.insertPage_atIndex_(leftPage, 0)
		pages = leftPDF.pageCount()
		startPage = int(not(doPageOne))
		for p in range(startPage, pages):
			outPageCount = newPDF.pageCount()
			leftPage = leftPDF.pageAtIndex_(p)
			rightPage = rightPDF.pageAtIndex_(p)
			mediaBoxSize = leftPage.boundsForBox_(mediabox)
			rotation = leftPage.rotation()
			if (rotation == 0) or (rotation == 180):
				halfway = (mediaBoxSize.size.width/2)
				pageHeight = mediaBoxSize.size.height			
				leftHandCrop = CGRectMake(0,0,halfway,pageHeight)
				rightHandCrop = CGRectMake(halfway, 0, halfway, pageHeight)
				leftPage.setBounds_forBox_(leftHandCrop, mediabox)
				rightPage.setBounds_forBox_(rightHandCrop, mediabox)
			else:
				halfway = (mediaBoxSize.size.height/2)
				pageWidth = mediaBoxSize.size.width
				topCrop = CGRectMake(0,0,pageWidth, halfway)
				bottomCrop = CGRectMake(0,halfway, pageWidth,halfway)
				leftPage.setBounds_forBox_(topCrop, mediabox)
				rightPage.setBounds_forBox_(bottomCrop, mediabox)

			newPDF.insertPage_atIndex_(leftPage, outPageCount)			
			newPDF.insertPage_atIndex_(rightPage, outPageCount+1)

		newPDF.writeToFile_(outFilename)

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		debooklet(filename)
