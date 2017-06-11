#! /usr/bin/python

# Gets PDF metadata for any PDF file provided as an argument
# by Ben Byram-Wigfield v1.1
#

import sys
from Quartz import PDFDocument
from CoreFoundation import NSURL
		
if __name__ == '__main__':

	for filename in sys.argv[1:]:
		pdfURL = NSURL.fileURLWithPath_(filename)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		print "File:", pdfDoc.documentURL()
		metadata = pdfDoc.documentAttributes()
		for key in metadata:
			print key, ":", metadata[key]
		print "Number of Pages:", pdfDoc.pageCount()
    	print "Is Encrypted:", pdfDoc.isEncrypted()
    	print "Is Locked:", pdfDoc.isLocked()
    	print "Allows Copying:", pdfDoc.allowsCopying()
    	print "Allows Printing:", pdfDoc.allowsPrinting()
    	print "Version:", pdfDoc.majorVersion(), pdfDoc.minorVersion()
