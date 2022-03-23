#!/usr/bin/env python
# coding=utf-8

# SAVE AS PDF-X: PDF Service to apply Quartz filter and move PDF to designated folder
# by Ben Byram-Wigfield v1.4

# $1 is filename; $3 is complete temp filepath and name.
# $2 is loads of CUPS parameters.

import os
import sys
import Quartz as Quartz
from Foundation import NSURL
from AppKit import NSSavePanel, NSApp


def save_dialog(directory, filename):
    panel = NSSavePanel.savePanel()
    panel.setTitle_("Save PDF-X3 document")
    myUrl = NSURL.fileURLWithPath_isDirectory_(directory, True)
    panel.setDirectoryURL_(myUrl)
    panel.setNameFieldStringValue_(filename)
    NSApp.activateIgnoringOtherApps_(True)
    ret_value = panel.runModal()
    if ret_value:
        return panel.filename()
    else:
        return ''
        

def main(argv):
	(title, options, pathToFile) = argv[:]

	# Set the default location where the PDFs will go (you'll need to make sure this exists)
	
	destination = os.path.expanduser("~/Desktop/")
	
	# Set the filepath of the filter. 
	# Check for custom user filter; otherwise use the Not-Very-Good System filter.
	filterpath = os.path.expanduser("~/Library/Filters/Better PDF-X3.qfilter")
	if not os.path.exists(filterpath):
		filterpath = "/System/Library/Filters/Create Generic PDFX-3 Document.qfilter"
	
	title += ".pdf"
	outputfile = save_dialog(destination, title)
	
	if outputfile != "":

		pdfURL = NSURL.fileURLWithPath_(pathToFile)
		pdfDoc = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc :
			filterURL = NSURL.fileURLWithPath_(filterpath)
			value = Quartz.QuartzFilter.quartzFilterWithURL_(filterURL)
			options = { 'QuartzFilter': value }
			pdfDoc.writeToFile_withOptions_(outputfile, options)
		
	# Delete original PDF from spool folder
	os.remove(pathToFile)
	
if __name__ == "__main__":
    main(sys.argv[1:])