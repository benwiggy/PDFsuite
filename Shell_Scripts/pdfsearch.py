#! /usr/bin/env python

# PDF TEXT SEARCH v1.0
# by Ben Byram-Wigfield

# Minimal function for searching text in a PDF for a string.
# Useful safety tip: PDFKit's page index starts at zero

import sys
from Quartz import PDFDocument
from Foundation import NSURL
		
def pdfSearch(filepath, searchString):
	pdfURL = NSURL.fileURLWithPath_(filepath)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		searchResults = (pdfDoc.findString_withOptions_(searchString, 0))
		if searchResults:
			for result in searchResults:
				eachPage = result.pages()
				print ("\'"+ searchString+"\' was found on page: "+str(pdfDoc.indexForPage_(eachPage[0])+1)) 
		else:
			print("Nothing found.")
	else:
		print("Not a valid PDF.")
	return

if __name__ == "__main__":
	# Set the filepath and searchString to your desired values
	filepath = '/Users/ben/Desktop/Untitled.pdf'
	searchString = 'office'
	pdfSearch(filepath, searchString)