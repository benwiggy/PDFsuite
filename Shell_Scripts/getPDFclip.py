#!/usr/bin/python

# Get PDF from Clipboard. 
# by Ben Byram-Wigfield. 
# This script saves a file with a copy of any PDF data found on the Mac Clipboard.

# If Clipboard.pdf exists, Add Page to it.

from AppKit import NSPasteboard, NSPasteboardTypePDF
from Foundation import NSURL
import Quartz as Quartz
import os
from CoreFoundation import CFDataCreate


outfile=os.path.expanduser("~/Desktop/Clipboard.pdf")

myFavoriteTypes = [NSPasteboardTypePDF]
pb = NSPasteboard.generalPasteboard()
best_type = pb.availableTypeFromArray_(myFavoriteTypes)
if best_type:
	clipData = pb.dataForType_(best_type)
	if clipData:
		data = CFDataCreate(None, clipData, len(clipData))
		# Next line only if you're using CGPDFDocument
		# provider = Quartz.CGDataProviderCreateWithCFData(data)
		clipPDF = Quartz.PDFDocument.alloc().initWithData_(data)
		if os.path.exists(outfile):
			pdfURL = NSURL.fileURLWithPath_(outfile)
			myFile = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
			if myFile:
				pagenum = myFile.pageCount()
				page = clipPDF.pageAtIndex_(0)
				myFile.insertPage_atIndex_(page, pagenum)
				myFile.writeToFile_(outfile)		
		else:
				clipPDF.writeToFile_(outfile)
				print "Clipboard file created."

else:
	print ("No clipboard PDF data retrieved. These types were available:")
	print (pb.types())
