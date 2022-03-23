#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PASSWORD v1.0: Concept script to unlock encrypted PDFs, (if you know the password)
# by Ben Byram-Wigfield
# Currently, the script doesn't do anything with the unlocked data. But the code could be
# added to other PDFSuite scripts in order to process locked PDFs.

from Foundation import NSAppleScript, NSURL
import Quartz as Quartz
import sys

# Sneaky call to AppleScript to get input from a dialog. 
def getTextFromDialog():
	textOfMyScript = """
tell application "System Events"
	set myWords to "This PDF is protected" & return & "Please enter the password:"
	set theResponse to (display dialog myWords with title "Encrypted PDF" default answer "" buttons {"Cancel", "Continue"} default button 2 with icon 0 with hidden answer)
end tell
	"""
	myScript = NSAppleScript.initWithSource_(NSAppleScript.alloc(), textOfMyScript)
	results, err = myScript.executeAndReturnError_(None)
	# results is an NSAppleEventDescriptor, which describes two things:
	# The button pressed (1), and the text returned (2).

	if not err:
		try:
			returnedInput = results.descriptorAtIndex_(2).stringValue()
		except:
			return None
		else:
			if returnedInput:
				return returnedInput
			else:
				return None
	else:
		print err
		return None


def checkLock(infile):
	pdfURL = NSURL.fileURLWithPath_(infile)
	myPDF = Quartz.PDFDocument.alloc().initWithURL_(pdfURL)
	if myPDF:
		if myPDF.isLocked:
			print "Locked"
			password = getTextFromDialog()
			if myPDF.unlockWithPassword_(password):
				print infile, "Unlocked!"
			else:
				print "Unable to unlock", infile
	else:
		print "No PDF data retrieved from", infile

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		checkLock(filename)