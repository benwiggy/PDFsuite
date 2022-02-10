#! /usr/bin/env python
# coding=utf-8

# CREATOR : Add [Creator] metadata to a PDF file.
# by Ben Byram-Wigfield

# creator -c <creator> - i <inputfile> [-o <outputfile>]
#
import sys
import os
import getopt
import Quartz.CoreGraphics as Quartz

from CoreFoundation import NSURL

def main(argv):
	inputfile = ""
	outputfile = ""
	value=""
	try:
		opts, args = getopt.getopt(argv,"hc:i:o:",["creator=", "input=", "output="])
	except getopt.GetoptError:
		print 'creator.py -c <creator> -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'creator.py -c <creator> -i <inputfile> -o <outputfile>'
			print 'longnames are: --creator, --input, --output'
			print "If no output is specified, the input will be over-written."
			sys.exit()
		elif opt in ("-c", "--creator"):
			value = arg.decode('utf-8')
		elif opt in ("-i", "--input"):
			inputfile = arg.decode('utf-8')
		elif opt in ("-o", "--output"):
			outputfile = arg.decode('utf-8')

	if outputfile == "": outputfile = inputfile
	pdfURL = NSURL.fileURLWithPath_(inputfile)
	pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)

# Default value option:
   # if value == "": value = "Uncle Bob Silly" 
	options = { Quartz.kCGPDFContextCreator: value }
	pdfDoc.writeToFile_withOptions_(outputfile, options)

if __name__ == "__main__":
	main(sys.argv[1:])
   
"""
Other Dict keys include: 

kCGPDFContextAuthor (string)
kCGPDFContextTitle 
kCGPDFContextOwnerPassword
kCGPDFContextUserPassword
kCGPDFContextAllowsPrinting (boolean)
kCGPDFContextAllowsCopying (boolean)

kCGPDFContextMediaBox (CGRect)
kCGPDFContextCropBox (CGRect)
kCGPDFContextBleedBox (CGRect)
kCGPDFContextTrimBox (CGRect)
kCGPDFContextArtBox (CGRect)

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
