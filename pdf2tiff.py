#!/usr/bin/python

"""
by Ben Byram-Wigfield
Creates a bitmap image from each page of each PDF supplied to it.
Acknowledgement is made to Jeff Laing for a similar script.
"""
import os, sys, objc
import Quartz as CG
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 

# os.environ["CG_CONTEXT_SHOW_BACKTRACE"] = '1'
# os.environ["CGBITMAP_CONTEXT_LOG_ERRORS"] = '1'

resolution = 300.0 #dpi
scale = resolution/72.0

cs = CG.CGColorSpaceCreateWithName(CG.kCGColorSpaceSRGB)
whiteColor = CG.CGColorCreate(cs, (1, 1, 1, 1))
# Options: kCGImageAlphaNoneSkipLast (no trans), kCGImageAlphaPremultipliedLast 
transparency = CG.kCGImageAlphaNoneSkipLast

#Save image to file
def writeImage (image, url, type, options):
	destination = CG.CGImageDestinationCreateWithURL(url, type, 1, None)
	CG.CGImageDestinationAddImage(destination, image, options)
	CG.CGImageDestinationFinalize(destination)
	return

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		pdf = CG.CGPDFDocumentCreateWithProvider(CG.CGDataProviderCreateWithFilename(filename))
		numPages = CG.CGPDFDocumentGetNumberOfPages(pdf)
		shortName = os.path.splitext(filename)[0]
		prefix = os.path.splitext(os.path.basename(filename))[0]
		try:
			os.mkdir(shortName)
		except:
			print "Can't create directory '%s'"%(shortName)
			sys.exit()
					
		# For each page, create a file
		for i in range (1, numPages+1):
			page = CG.CGPDFDocumentGetPage(pdf, i)
			if page:
		#Get mediabox
				mediaBox = CG.CGPDFPageGetBoxRect(page, CG.kCGPDFMediaBox)
				x = CG.CGRectGetWidth(mediaBox)
				y = CG.CGRectGetHeight(mediaBox)
				x *= scale
				y *= scale
				r = CG.CGRectMake(0,0,x, y)
		# Create a Bitmap Context, draw a white background and add the PDF
				ctx = CG.CGBitmapContextCreate(None, int(x), int(y), 8, 0, cs, transparency)
				CG.CGContextSaveGState (ctx)
				CG.CGContextScaleCTM(ctx, scale,scale)
				CG.CGContextSetFillColorWithColor(ctx, whiteColor)
				CG.CGContextFillRect(ctx, r)
				CG.CGContextDrawPDFPage(ctx, page)
				CG.CGContextRestoreGState(ctx)
		# Convert to an "Image"
				image = CG.CGBitmapContextCreateImage(ctx)	
		# Create unique filename per page
				outFile = shortName +"//" + prefix + " %03d.tif"%i
				url = CG.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, outFile, len(outFile), False)
		# kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG
				type = kUTTypeTIFF
		# For some reason, this doesn't seem to be passed to the TIFF file.
				options = {
					CG.kCGImagePropertyTIFFXResolution: 300,
					CG.kCGImagePropertyTIFFYResolution: 300,
					}
				writeImage (image, url, type, options)
				del page
				#CGContextRelease(ctx) # Not needed apparently. Causes crash.
	