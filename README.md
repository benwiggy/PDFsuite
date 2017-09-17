# PDFsuite
## Python scripts for MacOS (OS X) that create, manipulate, and query PDF files

This suite of python scripts for MacOS performs a wide range of PDF manipulation:  
* Merging PDFs
* Splitting PDFs
* Booklet imposition
* Converting PDFs to images
* Converting images to PDFs
* Rotating the pages of PDFs
* Adding page numbers, watermarks or other text to PDFs
* Applying Quartz filters to PDFs
* Adding metadata to PDFs and querying existing metadata
* Adding graphics (lines, circles, rectangles) to a PDF.

This is all done by accessing Apple's Core Graphics Quartz APIs. They should therefore run on any Mac using 10.6 Snow Leopard or higher!

Most of these scripts are designed to be used as **Automator Services**, which provide an easy interface for use. Once installed in the user's Library/Services folder, they will be available in the Finder's Services menu (or right-click context menu) when PDF files are selected.  
The bare scripts can also be run directly in a shell (Terminal), taking one or more PDF files as their argument. They are found in the **Automator_Scripts** folder. _(Drag the script file onto a Terminal window; then drag the PDF files you want to the same window; then press Enter!)_ 

Some are designed as **PDF Services**. PDF Services should be installed in the <user>/Library/PDF Services folder (or the top-level /Library/PDF Services folder). They will then be available in the PDF button of the print menu. _See the ReadMe in the subfolder for installation instructions._

A few scripts take more complex arguments and so will work best as Unix **shell scripts**. They may need further work for other purposes. _(Don't forget to set the execute flag!)_

## Automator Services
### Add Blank Page (addpage.py)
This script adds a blank page to the front of a PDF file.

### Add Page Number (pagenumber.py)
This script adds a folio number to facing pages of PDF files supplied as arguments. Users can set the offset position from the outer top corner, font, size. There are also settings for the scale, opacity and angle of text. A new file is produced, suffixed "NUM". A slightly modified version of this script is used to produce text watermarks (watermark.py).

### Combine images to one PDF (imagestopdf.py)
Modified (improved!) version of an Apple open source script, which takes any number of image files (supplied as arguments) and combines them into pages of one PDF file. This script is several seconds faster than Apple's own Automator action.

### Count pages in PDF (countpages.py)
This counts the number of pages in one or more PDF files passed to it. It provides a cumulative count for multiple file arguments.

### Export pages as images (pdf2tiff.py)
This script exports each page as 300dpi RGB TIFF images from PDFs supplied as arguments. Options in the script alow for JPEG and PNG filetypes, resolution, transparency and other parameters. Images are saved to a folder with the name of the original file (minus file extension). If the folder cannot be created, the script fails.

### Join PDF files into one file (myjoin.py)
This script will combine all PDF files supplied as arguments into one file, called "Combined.pdf". 

### Rotate all pages in PDF (rotate.py and rotate2.py)
This will rotate all the pages of any PDF files passed as arguments by 90˚ into a new file suffixed "+90". There are two rotate scripts: one uses CoreGraphics's _CGPDFDocument_ and _CGPDFPage_ to create a PDF object, apply a graphical transform to each page and re-save. The second one uses PDFKit's _PDFDocument_ and _PDFPage_, which allow the direct setting and getting of a rotation parameter for each page.

### Split PDF into separate files (splitPDF.py)
This script creates separate PDFs for each page in an existing PDF. The page files are saved inside a folder with the name of the source file (minus .pdf extension). The script fails if the folder cannot be made.

### Watermark all pages of PDF (watermark.py)
By default, this script adds the word "SAMPLE" in 150pt Helvetica-Bold, at 45˚ angle, with 50% opacity, to every page of PDFs passed to it. These settings can easily be altered.

## PDF Services
### Booklet Imposition (booklet.py)
This script is set to work as a PDF Service. However, it could easily be adjusted to work as an Automator workflow. It takes the input PDF file and lays out the pages on a larger sheet, in booklet spread page order. It checks for page rotation and adjusts if necessary. There's an option to arrange for 4pp signatures (stacked sheets, not gathered). The script brings up a Save dialog.

### Save As PDF-X PDF Service (Save As PDF-X.py)
This replaces the PDF Service that Apple removed from MacOS, which saved the PDF after applying a filter that makes the PDF conform to PDF-X3 spec. It will even bring up a Save file dialog. Apple's built-in PDF-X filter is quite poor, so you may want to use a better one.

## Shell scripts
### Apply Quartz Filter (quartzfilter.py)
This replaces Apple's own _quartzfilter_ command, which was removed from OS X (in Lion?). (Also, there was a sample script in Xcode, which used now-deprecated APIs.) Like its predecessor, it takes three arguments: the input file, the path to the quartz filter, and an output filename. It could be easily modified along the lines of the other scripts, to apply one fixed filter to all files given as arguments.

### Creator (creator.py)
This script alters PDFs, changing the "Creator" metadata to the value supplied. Other metadata keys are supplied, allowing the script to be easily modified for other metadata values. If no output file is set, it will overwrite the input file.  
creator.py -c CreatorName -i inputfile [-o outputfile]

### Get Info (getInfo.py)
This scripts outputs all the available PDF metadata for a file: Author, Creator, etc, Number of Pages, Version number, flags for encryption and security.

### Page Layout (pagelayout.py)
This script provides functions to easily draw rectangles, circles, lines, and text on a PDF page, with colours and transparency. It saves the results to file called "Test.pdf" on the user's Desktop. It is simply a "proof of concept" for a text-based description of graphical items.

## REVISION HISTORY
Minor improvements continue to be made to all the scripts: this includes improved Unicode string handling; standardized naming conventions, so that the code can be mixed and used in other scripts more easily; and better sanity checking and error handling. Any contributions on these terms are welcome.

## Other notes

These scripts are designed to work with the PyObjC Cocoa bridge and Python version currently bundled with MacOS. There are newer versions of python and PyObjC available, but the portability of the vanilla experience is preferred. 

If you're interested in python scripts, there are some python scripts written by Apple, in _/System/Library/Automator_, inside the bundles of PDF Automator actions for Combining PDF Pages, Extracting PDF pages, Watermarking PDFs, and adding gridlines to PDFs. There are also some open source python scripts on Apple's open source pages, though some of these don't work on default installations.

## LICENCE:
_"I have gathered a garland of other men's flowers, and nothing is mine but the cord that binds them."_ These scripts were not possible without looking at other code examples, particularly the [Apple open source python scripts](https://opensource.apple.com/source/pyobjc/); nor without help and advice from a range of people, such as [Jeff Laing](https://stuffineededtoknow.blogspot.co.uk/2009/01/pdf-to-jpeg-conversion.html), user Hiroto on Apple Support Community and the users of [StackOverFlow](http://stackoverflow.com). They are free to be used and adapted in any way, though I ask that you retain the acknowledgements within. I welcome help in improving them.

Ben Byram-Wigfield
