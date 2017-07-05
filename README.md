# PDFsuite
## Python scripts for MacOS (OS X) that create, manipulate, and query PDF files

These scripts automate a variety of tasks with PDFs, such as creating bookets, rotating pages, converting to/from images and getting or setting metadata. This is done by using Apple's Core Graphics Quartz APIs. Most can be run directly in a shell (Terminal), taking one or more PDF files as their argument. _(Drag the script file onto a Terminal window; then drag the PDF files you want to the same window; then press Enter!)_
They can also be used in Automator actions very easily to make Finder Services or Drop-applets. _(Use the "Run Shell Script" action, copy the script in and set the shell drop-down setting to python, and Pass input to "as arguments".)_

One script -- Apply Quartz Filter -- takes three arguments.

A few are PDF Services. PDF Services need to go in the /Library/PDF Services folder (or the same folder in the User Library). They will then be available in the PDF button of the print menu. _(They also need the executable flag set.)_

### 1. Booklet Imposition (booklet.py)

This script is set to work as a PDF Service. However, it could easily be adjusted to work as an Automator workflow. It takes the input PDF file and lays out the pages on a larger sheet, in booklet spread page order. NEW: Checks for page rotation and adjusts if necessary. NEWER!: Option to arrange for 4pp signatures (stacked sheets, not gathered).

### 2. Apply Quartz Filter (quartzfilter.py)

This replaces Apple's own _quartzfilter_ command, which was removed from OS X (in Lion?). (Also, there was a sample script in Xcode, which used now-deprecated APIs.) Like its predecessors, it takes three arguments: the path to the quartz filter, input file and output file. It could be easily modified along the lines of the other scripts, to apply one fixed filter to all files given as arguments.

### 3. Count pages in PDF (countpages.py)

This counts the number of pages in one or more PDF files passed to it. It provides a cumulative count for multiple file arguments.

### 4. Rotate (rotate.py)

This will rotate all the pages of any PDF files passed as arguments by 90˚ into a new file suffixed "+90". There are two rotate scripts: one uses CoreGraphics's _CGPDFDocument_ and _CGPDFPage_ to create a PDF object, apply a graphical transform to each page and re-save. The second one uses PDFKit's _PDFDocument_ and _PDFPage_, which allow the direct setting and getting of a rotation parameter for each page. Easier, but not as much fun.

### 5. Creator (creator.py)

This script alters PDF, changing the "Creator" metadata to the value supplied. Other metadata keys are supplied, allowing the script to be easily modified for other metadata values. If no output file is set, it will overwrite the input file.

### 6. Add Page Number (pagenumber.py)

This script adds a folio number to facing pages of PDF files supplied as arguments. Users can set the offset position from the outer top corner, font, size. There are also settings for the scale, opacity and angle of text. A new file is produced, suffixed "NUM". 
This script can be easily adjusted to produce watermark text on PDFs.

### 7. Export pages as images (pdf2tiff.py)

This script exports each page as 300dpi RGB TIFF images from PDFs supplied as arguments. Options in the script alow for JPEG and PNG filetypes, resolution, transparency and other parameters. Images are saved to a folder with the name of the original file (minus file extension). If the folder cannot be created, the script fails.

### 8. Combine images to one PDF (imagestopdf.py)

Modified (improved!) version of an Apple open source script (I hope that's ok!), which takes any number of image files (supplied as arguments) and combines them into pages of one PDF file.

### 9. Split PDF into separate files (splitPDF.py)

This script creates separate PDFs for each page in an existing PDF. The page files are saved inside a folder with the name of the source file (minus .pdf extension). The script fails if the folder cannot be made.

### 10. Join PDF files into one file (myjoin.py)

This script will combine all PDF files supplied as arguments into one file, called "Combined.pdf". 

### 11. Save As PDF-X PDF Service (Save As PDF-X.py)

This replaces the PDF Service that Apple removed from MacOS, which saved the PDF after applying a filter that makes the PDF conform to PDF-X3 spec. It will even bring up a Save file dialog. Apple's built-in PDF-X filter is quite poor, so you may want to use a better one.

### 12. Get Info (getInfo.py)

This scripts outputs all the available PDF metadata for a file: Author, Creator, etc, Number of Pages, Version number, flags for encryption and security.

### 13. Page Layout (pagelayout.py)

This script provides functions to draw rectangles, lines, and text on a PDF page, with colours and transparency.

## REVISION HISTORY
Minor improvements continue to be made to all the scripts: this includes improved Unicode string handling; standardized naming conventions, so that the code can be mixed and used in other scripts more easily; and better sanity checking and error handling. Any contributions on these terms are welcome.

## Other notes

These scripts are designed to work with the PyObjC Cocoa bridge and Python version bundled with MacOS. There are newer versions out there, but the portability of the vanilla experience is preferred. 
If you're interested in these, there are some python scripts written by Apple, in _/System/Library/Automator_, inside the bundles of PDF Automator actions for Combining PDF Pages, Extracting PDF pages, Watermarking PDFs, and adding gridlines to PDFs. There are also some open source python scripts on Apple's open source pages, though some of these don't work on default installations.

## LICENCE:
_"I have gathered a garland of other men's flowers, and nothing is mine but the cord that binds them."_ These scripts were not possible without looking at other code examples; nor without help and advice from a range of people. I cannot make much claim to them beyond 'compiling' them, and they are free to be used and adapted in any way, though I ask that you retain the acknowledgements within. I welcome help in improving them.

Ben Byram-Wigfield
