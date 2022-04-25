#!/usr/bin/env python3

"""
PDF2PNG v.3.0: Creates a bitmap image from each page of each PDF supplied to it.
by Ben Byram-Wigfield
Now written for python3. You may need to install pyobjc with pip3.

"""
import os, sys
import Quartz as Quartz
# from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault) 

kUTTypeJPEG = 'public.jpeg'
kUTTypeTIFF = 'public.tiff'
kUTTypePNG = 'public.png'
kCFAllocatorDefault = None

resolution = 300.0 #dpi
scale = resolution/72.0

cs = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceSRGB)
whiteColor = Quartz.CGColorCreate(cs, (1, 1, 1, 1))
# Options: Quartz.kCGImageAlphaNoneSkipLast (no trans), Quartz.kCGImageAlphaPremultipliedLast 
transparency = Quartz.kCGImageAlphaNoneSkipLast

#Save image to file
def writeImage (image, url, type, options):
	destination = Quartz.CGImageDestinationCreateWithURL(url, type, 1, None)
	Quartz.CGImageDestinationAddImage(destination, image, options)
	Quartz.CGImageDestinationFinalize(destination)
	return

def getFilename(filepath):
	i=0
	newName = filepath
	while os.path.exists(newName):
		i += 1
		newName = filepath + " %02d"%i
	return newName

if __name__ == '__main__':

	for filename in sys.argv[1:]:
		filenameNonU = filename.encode('utf8')
		pdf = Quartz.CGPDFDocumentCreateWithProvider(Quartz.CGDataProviderCreateWithFilename(filenameNonU))
		print(pdf, filenameNonU)
		numPages = Quartz.CGPDFDocumentGetNumberOfPages(pdf)
		shortName = os.path.splitext(filename)[0]
		prefix = os.path.splitext(os.path.basename(filename))[0]
		folderName = getFilename(shortName)
		try:
			os.mkdir(folderName)
		except:
			print("Can't create directory '%s'"%(folderName))
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
				outFile = folderName +"/" + prefix + " %03d.png"%i
				outFile_nonU = outFile.encode('utf8')
				url = Quartz.CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, outFile_nonU, len(outFile_nonU), False)
		# kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG
				type = kUTTypePNG
		# See the full range of image properties on Apple's developer pages.
				options = {
					Quartz.kCGImagePropertyDPIHeight: resolution,
					Quartz.kCGImagePropertyDPIWidth: resolution
					}
				writeImage (image, url, type, options)
				del page
				