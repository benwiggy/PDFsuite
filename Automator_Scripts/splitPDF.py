#!/usr/bin/python
# coding=utf-8
"""
SPLITPDF v2.0 : Takes an existing PDF and creates individual page documents in a new folder.
by Ben Byram-Wigfield 

New tool rebuilt using PDFKit, instead of Core Graphics.

"""
import os, sys
import Quartz as Quartz
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, NSURL)

	
def createPDFDocumentWithPath(path):
	path = path.decode('utf-8')
	pdfURL = NSURL.fileURLWithPath_(path)
	if pdfURL:
		return Quartz.PDFDocument.alloc().initWithURL_(pdfURL)

def getFilename(filepath):
	i=0
	newName = filepath
	while os.path.exists(newName):
		i += 1
		newName = filepath + " %02d"%i
	return newName

def strip(filename):
	# 
	pdf = createPDFDocumentWithPath(filename)
	numPages = pdf.pageCount()
	shortName = os.path.splitext(filename)[0]
	prefix = os.path.splitext(os.path.basename(filename))[0]
	metaDict = pdf.documentAttributes()
	folderName = getFilename(shortName)
	try:
		os.mkdir(folderName)
	except:
		print "Can't create directory '%s'"%(folderName)
		sys.exit()
		
	# For each page, create a file. Index starts at ZERO!!!
	# You won't get leading zeros in filenames beyond 99.
	for i in range (1, numPages+1):
		page = pdf.pageAtIndex_(i-1)
		if page:
			newDoc = Quartz.PDFDocument.alloc().initWithData_(page.dataRepresentation())	
			outFile = folderName +"/" + prefix + " %03d.pdf"%i
			newDoc.writeToFile_withOptions_(outFile, metaDict)

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		strip(filename)