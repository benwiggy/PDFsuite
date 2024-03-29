#!/usr/bin/env python3


# ENCRYPT : Encrypt PDF and lock with password.
# by Ben Byram-Wigfield v.1.1
# but copying or extracting requires the Owner Password.
# WARNING: Some versions of OS X (High Sierra) corrupt PDF metadata after encryption.

import os, sys
from Quartz import PDFDocument, kCGPDFContextAllowsCopying, kCGPDFContextAllowsPrinting, kCGPDFContextUserPassword, kCGPDFContextOwnerPassword
from CoreFoundation import (NSURL)

copyPassword = "12345678" # Password for copying and printing
# openPassword = copyPassword # Or enter a different password to open the file.
openPassword = '' # to allow opening.

def encrypt(filename):
	if not filename:
		print ('Unable to open input file')
		sys.exit(2)
	shortName = os.path.splitext(filename)[0]
	outputfile = shortName+" locked.pdf"
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc :
		options = { 
			kCGPDFContextAllowsCopying: False, 
			kCGPDFContextAllowsPrinting: False, 
			kCGPDFContextOwnerPassword: copyPassword,
			kCGPDFContextUserPassword: openPassword}
		pdfDoc.writeToFile_withOptions_(outputfile, options)
	return

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		encrypt(filename)