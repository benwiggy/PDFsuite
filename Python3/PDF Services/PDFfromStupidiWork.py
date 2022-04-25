#!/usr/bin/env python3

# SAVE PDF FROM STUPID iWORK  
# PDF Service to strip iWork file extension before saving PDF to designated folder
# by Ben Byram-Wigfield v1.0

# Save this file in ~/Library/PDF Services. It will then be available in the 
# PDF button of the print menu.

import os
import sys
import Quartz as Quartz
from Foundation import NSURL
from AppKit import NSSavePanel, NSApp


def save_dialog(directory, filename):
    panel = NSSavePanel.savePanel()
    panel.setTitle_("Save PDF document")
    myUrl = NSURL.fileURLWithPath_isDirectory_(directory, True)
    panel.setDirectoryURL_(myUrl)
    panel.setNameFieldStringValue_(filename)
    NSApp.activateIgnoringOtherApps_(True)
    ret_value = panel.runModal()
    if ret_value:
        return panel.filename()
    else:
        return ''
        

# $1 is filename; $3 is complete temp filepath and name.
# $2 is loads of CUPS parameters.

def main(argv):
	(title, options, pathToFile) = argv[:]

	# Set the default location where the PDFs will go (you'll need to make sure this exists)
	
	destination = os.path.expanduser("~/Desktop/")
	

	stripTitle = (os.path.splitext(title)[0])
	stripTitle += ".pdf"
	outputfile = save_dialog(destination, stripTitle)
	
	# Copy file to selected location. 
	if outputfile != "":

		pdfURL = NSURL.fileURLWithPath_(pathToFile)
		pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc:
			pdfDoc.writeToFile_(outputfile)

	# Delete original PDF from spool folder
	os.remove(pathToFile)
	
if __name__ == "__main__":
    main(sys.argv[1:])