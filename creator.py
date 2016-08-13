#! /usr/bin/python

# by Ben Byram-Wigfield
# Script to save Creator information into PDF metadata
#
import sys
import os
import getopt
from Quartz.CoreGraphics import (CGContextBeginPage, CGContextConcatCTM, CGContextDrawPDFPage, CGContextEndPage, CGContextRestoreGState, CGContextRotateCTM, CGContextSaveGState, CGContextScaleCTM, CGContextSetAlpha, CGContextSetTextPosition, CGContextTranslateCTM, CGContextTranslateCTM, CGContextTranslateCTM, CGPDFContextClose, CGPDFContextCreateWithURL, CGPDFDocumentCreateWithURL, CGPDFDocumentGetNumberOfPages, CGPDFDocumentGetPage, CGPDFPageGetBoxRect, CGPDFPageGetDrawingTransform, CGRectGetHeight, CGRectGetWidth, CGRectIsEmpty, CGRectMake, kCGPDFMediaBox, kCGPDFContextCreator, kCGPDFContextAuthor, PDFDocument, QuartzFilter)

from CoreFoundation import (NSURL, CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)


def main(argv):
   inputfile = ""
   outputfile = ""
   filter = ""
   try:
      opts, args = getopt.getopt(argv,"hc:i:o:",["input=","creator=","output="])
   except getopt.GetoptError:
      print 'creator.py -c <creator> -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'creator.py -c <filter> -i <inputfile> -o <outputfile>'
         print 'longnames are: --creator, --input, --output'
         print "If no output is specified, the input will be over-written."
         sys.exit()
      elif opt in ("-c", "--creator"):
         value = arg
      elif opt in ("-i", "--input"):
         inputfile = arg
      elif opt in ("-o", "--output"):
         outputfile = arg

   if outputfile == "": outputfile = inputfile
   pdf_url = NSURL.fileURLWithPath_(inputfile)
   pdf_doc = PDFDocument.alloc().initWithURL_(pdf_url)
# Default value option:
#   if value == "": value = "Uncle Bob Silly" 
   dict = { 'kCGPDFContextCreator': value }
   pdf_doc.writeToFile_withOptions_(outputfile, dict)

if __name__ == "__main__":
   main(sys.argv[1:])
   
"""
Other Dict keys include: (Don't forget to add them to the header)

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
