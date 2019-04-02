#!/usr/bin/python

# RINSE PDF v1.0 : This script will re-save a PDF, which may fix some errors in the PDF data.
# by Ben Byram-Wigfield

import sys
import os
import Quartz as Quartz
from CoreFoundation import NSURL


for inputfile in sys.argv[1:]:
	outfile = inputfile
# To save with a new name, uncomment the lines below.
#	prefix = os.path.splitext(inputfile)
#	outfile = prefix[0] + 'rinsed.pdf'
	pdfURL = NSURL.fileURLWithPath_(inputfile)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	pdfDoc.writeToFile_(outfile)
