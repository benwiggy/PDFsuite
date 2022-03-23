#!/usr/bin/env python
# coding=utf-8

# GET PDF OUTLINES v. 1.4
# by Ben Byram-Wigfield
# This script will produce rudimentary PDFmark data from any PDF file(s) given as arguments,
# for PDF Outlines (bookmarks, ToCs) with page destinations. (Not Actions.)

from Foundation import  NSURL
import Quartz as Quartz
import sys


def getDestination(thisOutline):
	thisDestination=thisOutline.destination()
	if thisDestination:
		stringDestination= str(thisDestination).split(",")
		OutlineType = stringDestination[0]
		pageNum = stringDestination[1].split("= ")[1]
		pageNum = str(int(pageNum)+1)
		return OutlineType, pageNum

	
def recurseOutlines(thisOutline):
	# print (thisOutline.index())
	print ("[ /Title (" + thisOutline.label() +")")
	Otype, pageNum = getDestination(thisOutline)
	print ("  /Page " + pageNum)
	
	# View wil never be specified. 
	Otype = "qwe"
	if Otype == "XYZ":
		print("  /View [/" + Otype + " 0 0 0]")
	if Otype == "Fit":
		print("  /View [/" + Otype + "]")

	if thisOutline.numberOfChildren() != 0:
		print ("  /Count " + str(thisOutline.numberOfChildren()))
		print("   /OUT pdfmark\n")
		for n in range(thisOutline.numberOfChildren()):
			recurseOutlines(thisOutline.childAtIndex_(n))
	else:
		print("   /OUT pdfmark\n")

def getOutlines(infile):
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		outline = Quartz.PDFOutline.alloc().init()
		outline = myPDF.outlineRoot()
		if outline:
			if outline.numberOfChildren() != 0:
				for n in range(outline.numberOfChildren()):
					recurseOutlines(outline.childAtIndex_(n))
			else:
				print("No Outlines in this PDF.")
					
if __name__ == '__main__':
	for filename in sys.argv[1:]:
		getOutlines(filename)