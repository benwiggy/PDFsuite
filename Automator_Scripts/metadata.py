#!/usr/bin/python
# coding=utf-8

# METADATA : Add or Change metadata to a PDF file.
# by Ben Byram-Wigfield
#
import sys
import os
import getopt
import Quartz.CoreGraphics as Quartz

from CoreFoundation import NSURL

def setMetadata(filename):
	options = {}
	author='Ben Byram-Wigfield'
	creator = 'PDFSuite Python Scripts'
	subject = ''
	keywords = 'PDF Magic'
	
# Get Title from filename. Or delete these two lines and set a string value.
	title = os.path.basename(filename)
	title = os.path.splitext(title)[0]
	
	authorKey = Quartz.kCGPDFContextAuthor
	creatorKey = Quartz.kCGPDFContextCreator
	subjectKey = Quartz.kCGPDFContextSubject
	keywordsKey = Quartz.kCGPDFContextKeywords
	titleKey = Quartz.kCGPDFContextTitle

	filename = filename.decode('utf-8')
	shortName = os.path.splitext(filename)[0]
	pdfURL = NSURL.fileURLWithPath_(filename)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)

# Default value option:
	if author:
		options[authorKey] = author
	if creator:
		options[creatorKey] = creator
	if subject:
		options[subjectKey] = subject
	if keywords:
		options[keywordsKey] = keywords
	if title:
		options[titleKey] = title
	
	print options
		
# To save to a separate file, uncomment the next line.
	# filename = shortName + " data.pdf"
	pdfDoc.writeToFile_withOptions_(filename, options)

if __name__ == "__main__":
	for filepath in sys.argv[1:]:
		setMetadata(filepath)
   
"""
Dict keys include: 

kCGPDFContextAuthor (string)
kCGPDFContextCreator
kCGPDFContextTitle 


kCGPDFContextOwnerPassword
kCGPDFContextUserPassword
kCGPDFContextAllowsPrinting (boolean)
kCGPDFContextAllowsCopying (boolean)

kCGPDFContextOutputIntent
kCGPDFContextOutputIntents
kCGPDFContextSubject
kCGPDFContextKeywords
kCGPDFContextEncryptionKeyLength

kCGPDFXOutputIntentSubtype
kCGPDFXOutputConditionIdentifier
kCGPDFXOutputCondition
kCGPDFXRegistryName
kCGPDFXInfo
kCGPDFXDestinationOutputProfile

See the Apple Documentation page on Auxiliary Dictionary Keys for PDF Context for more.

"""