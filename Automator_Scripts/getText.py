#! /usr/bin/python
# -*- coding: utf-8 -*-

# Exports text of complete PDF document to .txt file
# by Ben Byram-Wigfield v1.0
#

import os,sys
from Quartz import PDFDocument
from Foundation import NSURL


def getFilename(basename):
	fullname = basename + ".txt"
	i=0
	while os.path.exists(fullname):
		i += 1
		fullname = basename + " %02d.txt"%i
	return fullname

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		filename = filename.decode('utf-8')
		shortName = os.path.splitext(filename)[0]
		pdfURL = NSURL.fileURLWithPath_(filename)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc:
			pdfText = pdfDoc.string().encode('utf-8')
			outfile = getFilename(shortName)
			with open(outfile, "w") as text_file:
				text_file.write(pdfText)