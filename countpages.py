#!/usr/bin/python

# by Ben Byram-Wigfield

# Script returns the total number of pages in all PDFs supplied as arguments
# Makes no attempt to sanitize input.

import sys
from CoreGraphics import *

pdfnum=0

def pageCount(pdfPath):
	# "Return the number of pages for some PDF file."
 
    pdf = CGPDFDocumentCreateWithProvider (CGDataProviderCreateWithFilename (pdfPath))
    return pdf.getNumberOfPages()

if __name__ == '__main__':

	for filename in sys.argv[1:]:
	 	pdfnum=pdfnum+pageCount(filename)
 
print pdfnum
