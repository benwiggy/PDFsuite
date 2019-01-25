#!/usr/bin/python
# coding=utf-8

# CROP PDF v.1.0 : Crop the mediabox by a given set of margins.
# by Ben Byram-Wigfield v1.0

# Use on the Command line with filenames as arguments (e.g. cropPDF.py /path/to/file.pdf)
# Or in Automator as a Quick Action/Service. Select "Receives PDF Files in Finder"
# Then Add "Run Shell Script" action. Select /usr/bin/python from the drop-down list;
# Select "Pass Input" as "as arguments".
# Paste script into area for scripts, replacing existing text.

import sys
import os
from Quartz import PDFDocument, kPDFDisplayBoxMediaBox, kPDFDisplayBoxTrimBox, CGRectEqualToRect, CGRectMake
from CoreFoundation import NSURL

mediabox = kPDFDisplayBoxMediaBox
# Margins: left margin, bottom margin, right margin, top margin.
margins = [45, 45, 45, 45]

	
def trimPDF(filename):
	filename = filename.decode('utf-8')
	shortName = os.path.splitext(filename)[0]
	outFilename = shortName + " TPS.pdf"
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		pages = pdfDoc.pageCount()
		for p in range(0, pages):
			page = pdfDoc.pageAtIndex_(p)
			mediaBoxSize = page.boundsForBox_(mediabox)
			trimBoxSize = CGRectMake(margins[0], margins[1], (mediaBoxSize.size.width - margins[2] - margins[0]), (mediaBoxSize.size.height - margins[3] - margins[1]))
			page.setBounds_forBox_(trimBoxSize, mediabox)

		pdfDoc.writeToFile_(outFilename)

if __name__ == '__main__':
	for filename in sys.argv[1:]:
		trimPDF(filename)
