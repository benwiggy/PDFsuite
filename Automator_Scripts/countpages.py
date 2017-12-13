#!/usr/bin/python
# coding=utf-8

# COUNTPAGES: Adds together the sum of pages from all PDFs supplied as arguments.
# by Ben Byram-Wigfield v.1.7

# Uses an Alert dialog to report the number!

import sys
from Quartz import (PDFDocument, CGPDFDocumentCreateWithProvider, CGDataProviderCreateWithFilename, CGPDFDocumentGetNumberOfPages)
from AppKit import (NSApp, NSAlert, NSInformationalAlertStyle, NSURL)

pdfnum=0

def displayAlert(message, info, buttons):
	alert = NSAlert.alloc().init()
	alert.setMessageText_(message)
	alert.setInformativeText_(info)
	alert.setAlertStyle_(NSInformationalAlertStyle)
	for button in buttons:
		alert.addButtonWithTitle_(button)
	NSApp.activateIgnoringOtherApps_(True)	
	buttonPressed = alert.runModal()
	return buttonPressed
	# First button will return 1000, second 1001, etc..

def pageCount(pdfPath):
	# The first way of counting pages, using PDFDocument.
	pdfPath = pdfPath.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(pdfPath)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		return pdfDoc.pageCount()

def pageCount2(pdfPath):
	# The second way of counting pages, using CGPDFDocument.
    pdf = CGPDFDocumentCreateWithProvider(CGDataProviderCreateWithFilename (pdfPath))
    return CGPDFDocumentGetNumberOfPages(pdf)

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		pdfnum=pdfnum+pageCount(filename)

displayAlert("Combined Page Count:", str(pdfnum), ["OK"])

# Or just print the number to stdout.
# print(pdfnum)