#!/usr/bin/python
#
# Usage: imagestopdf [image-file ...] 
#
# Modified from an Apple open source script.
# https://opensource.apple.com/source/efax/efax-42/efax/imagestopdf

# This script creates the specified PDF file. The contents of each image file
# are placed into a PDF named "Combined.pdf", in the same folder as the first image.
# The filename will be incremented if it exists.

import sys, os
from Quartz.CoreGraphics import *
from Quartz.ImageIO import *
from LaunchServices import kUTTypePDF


def getFilename(filepath, basename):
	fullname = basename + ".pdf"
	i=0
	while os.path.exists(os.path.join(filepath, fullname)):
		i += 1
		fullname = basename + " %02d.pdf"%i
	return os.path.join(filepath, fullname)
		

def main(argv):

	if len(argv) > 0 :

		hasImages = False
		prefix = os.path.dirname(argv[0]) 
		filename = "Combined"
		pdfout = getFilename(prefix, filename)
		print pdfout
	
	
		url = CFURLCreateWithFileSystemPath(kCFAllocatorDefault, pdfout, kCFURLPOSIXPathStyle, False)
		if url is None :
			sys.exit('imagestopdf: '  + pdfout + ': Can\'t create url')
		
		idr = CGImageDestinationCreateWithURL(url, kUTTypePDF, len(argv), None)
		if idr is None :
			sys.exit('imagestopdf: ' + url + ': Can\'t create file')
		
		for arg in argv[:] :
			image = None
			url = CFURLCreateWithFileSystemPath(kCFAllocatorDefault, arg, kCFURLPOSIXPathStyle, False)
			if url :
				isr = CGImageSourceCreateWithURL(url, None)
				if isr :
					props = CGImageSourceCopyPropertiesAtIndex(isr, 0, None)
					if props :
						image = CGImageSourceCreateImageAtIndex(isr, 0, None)
						if image :
							CGImageDestinationAddImage(idr, image, props)
							hasImages = True

			if image is None :
				print >> sys.stderr, 'imagestopdf: ' + arg + ': Invalid image file'

		if hasImages is True :
			CGImageDestinationFinalize(idr)

		else :
			sys.exit('imagestopdf: No images found!')

	else :
		print >> sys.stderr, 'Usage: imagestopdf [image-file ...]'
		sys.exit(2)


if __name__ == "__main__":
	main(sys.argv[1:])
