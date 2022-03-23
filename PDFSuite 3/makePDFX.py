#!/usr/bin/env python3

# Make PDFX: Create a PDF/X-3 compliant document
# v.3.0 Now written in python 3
#

import sys
import os
import Quartz as Quartz
from CoreFoundation import (NSURL, QuartzFilter)

filterpath = os.path.expanduser("~/Library/Filters/Better PDFX-3.qfilter")
if not os.path.exists(filterpath):
	filterpath = "/System/Library/Filters/Create Generic PDFX-3 Document.qfilter"
	print ("Using System filter, which is not very good")

for inputfile in sys.argv[1:]:
	prefix = os.path.splitext(inputfile)
	outfile = prefix[0] + 'X.pdf'
	pdfURL = NSURL.fileURLWithPath_(inputfile)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		filterURL = NSURL.fileURLWithPath_(filterpath)
		value = QuartzFilter.quartzFilterWithURL_(filterURL)
		options = { 'QuartzFilter': value }
		pdfDoc.writeToFile_withOptions_(outfile, options)
