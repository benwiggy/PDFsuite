#!/usr/bin/env python3
#
# IMAGE2PDF v.3.0 : Convert image files to one PDF.
# by Ben Byram-Wigfield 
# Rewritten using PDFKit. Now for python 3

import sys, os
import Quartz as Quartz
from LaunchServices import kUTTypePDF
from CoreFoundation import NSImage

def getFilename(filepath, basename):
	fullname = basename + ".pdf"
	i=0
	while os.path.exists(os.path.join(filepath, fullname)):
		i += 1
		fullname = basename + " %02d.pdf"%i
	return os.path.join(filepath, fullname)


def imageToPdf(argv):
	prefix = os.path.dirname(argv[0]) 
	filename = "Combined"
	pdfout = getFilename(prefix, filename)

	for index, eachFile in enumerate(argv):

		image = NSImage.alloc().initWithContentsOfFile_(eachFile)
		if image:
			page = Quartz.PDFPage.alloc().initWithImage_(image)
			if index == 0:
				pageData = page.dataRepresentation()
				pdf = Quartz.PDFDocument.alloc().initWithData_(pageData)
			else:
				pdf.insertPage_atIndex_(page, index)

	pdf.writeToFile_(pdfout)


if __name__ == "__main__":
	imageToPdf(sys.argv[1:])