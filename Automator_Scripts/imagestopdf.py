#!/usr/bin/python
#
# Usage: imagestopdf [image-file ...] 
#
# Some code modified from an Apple open source script.
# https://opensource.apple.com/source/efax/efax-42/efax/imagestopdf

# This script creates a PDF file, with a given name, from images supplied to it.
# The filename will be incremented if it exists.

import sys, os
import Quartz as Quartz
from LaunchServices import kUTTypePDF
from CoreFoundation import (CFURLCreateWithFileSystemPath, kCFAllocatorDefault, kCFURLPOSIXPathStyle)


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
	
	
		url = CFURLCreateWithFileSystemPath(kCFAllocatorDefault, pdfout, kCFURLPOSIXPathStyle, False)
		if url is None :
			sys.exit('imagestopdf: '  + pdfout + ': Can\'t create url')
		
		idr = Quartz.CGImageDestinationCreateWithURL(url, kUTTypePDF, len(argv), None)
		if idr is None :
			sys.exit('imagestopdf: ' + url + ': Can\'t create file')
		
		for arg in argv[:] :
			image = None
			url = CFURLCreateWithFileSystemPath(kCFAllocatorDefault, arg.decode('utf-8'), kCFURLPOSIXPathStyle, False)
			if url :
				isr = Quartz.CGImageSourceCreateWithURL(url, None)
				if isr :
					props = Quartz.CGImageSourceCopyPropertiesAtIndex(isr, 0, None)
					if props :
						image = Quartz.CGImageSourceCreateImageAtIndex(isr, 0, None)
						if image :
							Quartz.CGImageDestinationAddImage(idr, image, props)
							hasImages = True

			if image is None :
				print >> sys.stderr, 'imagestopdf: ' + arg + ': Invalid image file'

		if hasImages is True :
			Quartz.CGImageDestinationFinalize(idr)

		else :
			sys.exit('imagestopdf: No images found!')

	else :
		print >> sys.stderr, 'Usage: imagestopdf [image-file ...]'
		sys.exit(2)


if __name__ == "__main__":
	main(sys.argv[1:])
