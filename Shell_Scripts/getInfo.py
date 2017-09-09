#! /usr/bin/python
# -*- coding: utf-8 -*-

# Gets PDF metadata for any PDF file provided as an argument
# by Ben Byram-Wigfield v1.2
#

import sys
from Quartz import PDFDocument
from Foundation import NSURL
		
if __name__ == '__main__':

	for filename in sys.argv[1:]:
		filename = filename.decode('utf-8')
		pdfURL = NSURL.fileURLWithPath_(filename)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc:
			print "URL:", pdfDoc.documentURL() # Might be nice to Unicode this.
			metadata = pdfDoc.documentAttributes()
			for key in metadata:
				print "{}: {}".format(key, metadata[key])
			print "Number of Pages:", pdfDoc.pageCount()
			print "Is Encrypted:", pdfDoc.isEncrypted()
			print "Is Locked:", pdfDoc.isLocked()
			print "Allows Copying:", pdfDoc.allowsCopying()
			print "Allows Printing:", pdfDoc.allowsPrinting()
			print "Version: {}.{}".format(pdfDoc.majorVersion(),pdfDoc.minorVersion())
		else: print "Cannot get this file. (Not a PDF? / Bad filename?)"