#!/usr/bin/env python

# getPDFclip v.1.2 : Get PDF from Clipboard image data.
# by Ben Byram-Wigfield. 
# This script saves a PDF with a copy of any image data found on the Mac Clipboard.

# If Clipboard.pdf exists, the image is added as an extra page.

from AppKit import NSPasteboard, NSPasteboardTypePDF, NSTIFFPboardType, NSPICTPboardType, NSImage
from Foundation import NSURL
import Quartz as Quartz
import os, syslog

# Change this to whatever filepath you want:
outfile=os.path.expanduser("~/Desktop/Clipboard.pdf")


myFavoriteTypes = [NSPasteboardTypePDF, NSTIFFPboardType, NSPICTPboardType, 'com.adobe.encapsulated-postscript']
pb = NSPasteboard.generalPasteboard()
best_type = pb.availableTypeFromArray_(myFavoriteTypes)
if best_type:
	clipData = pb.dataForType_(best_type)
	if clipData:
		image = NSImage.alloc().initWithPasteboard_(pb)
		if image:
			page = Quartz.PDFPage.alloc().initWithImage_(image)
		if os.path.exists(outfile):
			pdfURL = NSURL.fileURLWithPath_(outfile)
			myFile = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
			if myFile:
				pagenum = myFile.pageCount()
				myFile.insertPage_atIndex_(page, pagenum)
				print "Image added to Clipboard file."
		
		else:
			pageData = page.dataRepresentation()
			myFile = Quartz.PDFDocument.alloc().initWithData_(pageData)
		myFile.writeToFile_(outfile)
		print "Clipboard file created."

else:
	print ("No clipboard image data was retrieved.")
	# print ("These types were available:")
	# print (pb.types())
