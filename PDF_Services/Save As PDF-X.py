#!/usr/bin/python
# coding=utf-8
# PDF Service to apply Quartz filter and move PDF to designated folder
# by Ben Byram-Wigfield v1.2

# Includes MacOS Save dialog.

# $1 is filename; $3 is complete temp filepath and name.
# $2 is loads of CUPS parameters.

import os
import sys
from Quartz.CoreGraphics import PDFDocument
from CoreFoundation import (NSURL, QuartzFilter)
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
	# By default, use the Not-Very-Good System PDFX-3 filter:
	filter = "/System/Library/Filters/Create Generic PDFX-3 Document.qfilter"
	
	# For custom filters in your user Library, use something like this:
	# filter = os.path.expanduser("~/Library/Filters/Better PDF-X3.qfilter")
	
	title += ".pdf"
	outputfile = save_dialog(destination, title)
	
	if outputfile != "":

		pdfURL = NSURL.fileURLWithPath_(pathToFile)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		filterURL = NSURL.fileURLWithPath_(filter)
		value = QuartzFilter.quartzFilterWithURL_(filterURL)
		dict = { 'QuartzFilter': value }
		pdfDoc.writeToFile_withOptions_(outputfile, dict)
	
if __name__ == "__main__":
    main(sys.argv[1:])