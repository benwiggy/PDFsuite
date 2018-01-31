#! /usr/bin/python
# coding: utf-8

# PDF2TXT: Output text content of a PDF file to a new text file
# by Ben Byram-Wigfield v.1.0

import os, sys
from Quartz import PDFDocument, kCGPDFContextAllowsCopying, kCGPDFContextUserPassword, kCGPDFContextOwnerPassword
from CoreFoundation import (NSURL, NSString)

# Can't seem to import this constant, so manually creating it.
NSUTF8StringEncoding = 4

def main():
	for filename in sys.argv[1:]:	
		inputfile =filename.decode('utf-8')
		shortName = os.path.splitext(filename)[0]
		outputfile = shortName+" text.txt"
		pdfURL = NSURL.fileURLWithPath_(inputfile)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc :
			pdfString = NSString.stringWithString_(pdfDoc.string())
			pdfString.writeToFile_atomically_encoding_error_(outputfile, True, NSUTF8StringEncoding, None)

if __name__ == "__main__":
   main()
