#!/usr/bin/env python3

# Produces new PDF file with all pages rotated by 90 degrees.
# by Ben Byram-Wigfield v3.0 for python3

# There are two ways to rotate a PDF page/file.
# 1: Create a new PDF context, graphically transform each page of the original and save the file.
# 2: Adjust the 'rotation' parameter in each page.
# This is the 2nd way, which is easier.
#  also preserves DocInfo and other metadata.

import sys
import os
from Quartz import PDFDocument
from CoreFoundation import NSURL
		
def doRotate(filename):
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + "+90.pdf"
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		pages = pdfDoc.pageCount()
		for p in range(0, pages):
			page = pdfDoc.pageAtIndex_(p)
			existingRotation = page.rotation()
			newRotation = existingRotation + 90
			page.setRotation_(newRotation)
		pdfDoc.writeToFile_(outFilename)


if __name__ == '__main__':
	for filename in sys.argv[1:]:
		doRotate(filename)