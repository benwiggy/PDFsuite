#! /usr/bin/python

# by Ben Byram-Wigfield
# Script to apply a MacOS Quartz Filter to a PDF file.
#
import sys
import os
import getopt
from Quartz.CoreGraphics import (CGContextBeginPage, CGContextConcatCTM, CGContextDrawPDFPage, CGContextEndPage, CGContextRestoreGState, CGContextRotateCTM, CGContextSaveGState, CGContextScaleCTM, CGContextSetAlpha, CGContextSetTextPosition, CGContextTranslateCTM, CGContextTranslateCTM, CGContextTranslateCTM, CGPDFContextClose, CGPDFContextCreateWithURL, CGPDFDocumentCreateWithURL, CGPDFDocumentGetNumberOfPages, CGPDFDocumentGetPage, CGPDFPageGetBoxRect, CGPDFPageGetDrawingTransform, CGRectGetHeight, CGRectGetWidth, CGRectIsEmpty, CGRectMake, kCGPDFMediaBox, PDFDocument, QuartzFilter)
from CoreText import (kCTFontAttributeName, CTFontCreateWithName, CTLineDraw, CTLineCreateWithAttributedString, kCTFontAttributeName, CTLineGetImageBounds)
from CoreFoundation import (NSURL, CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, kCFAllocatorDefault)


def main(argv):
   inputfile = ""
   outputfile = ""
   filter = ""
   try:
      opts, args = getopt.getopt(argv,"hf:i:o:",["filter=", "input=", "output="])
   except getopt.GetoptError:
      print 'quartzfilter.py -f <filter> -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'quartzfilter.py -f <filter> -i <inputfile> -o <outputfile>'
         print 'longnames are: --filter, --input, --output'
         print "If no output is specified, the input will be over-written."
         sys.exit()
      elif opt in ("-f", "--filter"):
         filter = arg
      elif opt in ("-i", "--input"):
         inputfile = arg
      elif opt in ("-o", "--output"):
         outputfile = arg

   if outputfile == "": outputfile = inputfile
   pdf_url = NSURL.fileURLWithPath_(inputfile)
   pdf_doc = PDFDocument.alloc().initWithURL_(pdf_url)
   furl = NSURL.fileURLWithPath_(filter)
   value = QuartzFilter.quartzFilterWithURL_(furl)
   dict = { 'QuartzFilter': value }
   pdf_doc.writeToFile_withOptions_(outputfile, dict)

if __name__ == "__main__":
   main(sys.argv[1:])