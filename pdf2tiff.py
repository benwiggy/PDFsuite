#!/usr/bin/python

"""
by Ben Byram-Wigfield
Creates a bitmap image from each page of each PDF supplied to it.
Acknowledgement is made to Jeff Laing for a similar script.
"""
import os, sys, objc
import Quartz as Quartz
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 

# os.environ["CG_CONTEXT_SHOW_BACKTRACE"] = '1'
# os.environ["CGBITMAP_CONTEXT_LOG_ERRORS"] = '1'

resolution = 300.0 #dpi
scale = resolution/72.0

cs = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceSRGB)
whiteColor = Quartz.CGColorCreate(cs, (1, 1, 1, 1))
# Options: kCGImageAlphaNoneSkipLast (no trans), kCGImageAlphaPremultipliedLast 
transparency = Quartz.kCGImageAlphaNoneSkipLast

#Save image to file
def writeImage (image, url, type, options):
	destination = Quartz.CGImageDestinationCreateWithURL(url, type, 1, None)
	Quartz.CGImageDestinationAddImage(destination, image, options)
	Quartz.CGImageDestinationSetProperties(destination, options)
	Quartz.CGImageDestinationFinalize(destination)
	return

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		pdf = Quartz.CGPDFDocumentCreateWithProvider(Quartz.CGDataProviderCreateWithFilename(filename))
		numPages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)
		shortName = os.path.splitext(filename)[0]
		prefix = os.path.splitext(os.path.basename(filename))[0]
		try:
			os.mkdir(shortName)
		except:
			print "Can't create directory '%s'"%(shortName)
			sys.exit()
					
		# For each page, create a file
		for i in range (1, numPages+1):
			page = Quartz.CGPDFDocumentGetPage(pdf, i)
			if page:
		#Get mediabox
				mediaBox = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
				x = Quartz.CGRectGetWidth(mediaBox)
				y = Quartz.CGRectGetHeight(mediaBox)
				x *= scale
				y *= scale
				r = Quartz.CGRectMake(0,0,x, y)
		# Create a Bitmap Context, draw a white background and add the PDF
				writeContext = Quartz.CGBitmapContextCreate(None, int(x), int(y), 8, 0, cs, transparency)
				Quartz.CGContextSaveGState (writeContext)
				Quartz.CGContextScaleCTM(writeContext, scale,scale)
				Quartz.CGContextSetFillColorWithColor(writeContext, whiteColor)
				Quartz.CGContextFillRect(writeContext, r)
				Quartz.CGContextDrawPDFPage(writeContext, page)
				Quartz.CGContextRestoreGState(writeContext)
		# Convert to an "Image"
				image = Quartz.CGBitmapContextCreateImage(writeContext)	
		# Create unique filename per page
				outFile = shortName +"//" + prefix + " %03d.tif"%i
				url = Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, outFile, len(outFile), False)
		# kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG
				type = kUTTypeTIFF
		# For some reason, this doesn't seem to be passed to the TIFF file.
				options = {
					Quartz.kCGImagePropertyTIFFDictionary: 'TIFFDictionary',
					Quartz.kCGImagePropertyTIFFXResolution: '300',
					Quartz.kCGImagePropertyTIFFYResolution: '300',
					}
				writeImage (image, url, type, options)
				del page
				#CGContextRelease(writeContext) # Not needed apparently. Causes crash.
	