#! /usr/bin/python

# by Ben Byram-Wigfield
# Script to apply a MacOS Quartz Filter to a PDF file.
#
import sys
import os
import getopt
from CoreFoundation import *
from Quartz.CoreGraphics import *


def main(argv):
   inputfile = ""
   outputfile = ""
   filter = ""
   try:
      opts, args = getopt.getopt(argv,"hi:f:o:",["input=","filter=","output="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -f <filter> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -f <filter> -o <outputfile>'
         print 'longnames are: --input, --filter, --output'
         print "If no output is specified, the input will be over-written."
         sys.exit()
      elif opt in ("-i", "--input"):
         inputfile = arg
      elif opt in ("-f", "--filter"):
         filter = arg
      elif opt in ("-o", "--output"):
         outputfile = arg
   print 'Input file is ', inputfile
   print "Filter is ", filter
   print 'Output file is ', outputfile
   if outputfile == "": outputfile = inputfile
   pdf_url = NSURL.fileURLWithPath_(inputfile)
   pdf_doc = PDFDocument.alloc().initWithURL_(pdf_url)
   furl = NSURL.fileURLWithPath_(filter)
   fobj = QuartzFilter.quartzFilterWithURL_(furl)
   fdict = { 'QuartzFilter': fobj }
   pdf_doc.writeToFile_withOptions_(outputfile, fdict)

if __name__ == "__main__":
   main(sys.argv[1:])