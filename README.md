# PDFsuite
Python scripts for MacOS (OS X) that create, manipulate, and query PDF files

These scripts provide 'front ends' to MacOS's Core Graphics APIs, thereby allowing the automation of a variety of tasks, such as creating bookets, applying Quartz Filters and querying page count of input PDFs. Most can be used directly in a shell, taking one or more PDF files as their argument. As a result, they can be used in Automator actions very easily to produce Services or Drop-applets. One (Apply Quartz Filter) takes three arguments. A few others are PDF Services. PDF Services need to go in the /Library/PDF Services folder (or the same folder in the User Library).

1. Booklet Imposition (booklet.py)

This script is set to work as a PDF Service. However, it could easily be adjusted to work as an Automator workflow. It takes the input PDF file and lays out the pages on a larger sheet, in booklet spread page order. NEW: Checks for page rotation and adjusts if necessary.

2. Apply Quartz Filter (quartzfilter.py)

This replaces Apple's own quartzfilter command, which was removed from OS X (in Lion?). (Also, there was a sample script in Xcode, which used now-deprecated APIs.) Like its predecessors, it takes three arguments: quartz filter, input file and output file.

3. Count pages in PDF (countpages.py)

This uses Core Graphics objects and methods to count the number of pages in one or more PDF files passed to it. It provides a cumulative count for multiple file arguments.

4. Rotate (rotate.py)

This will rotate all the pages of any PDF files by 90˚ into a new file suffixed "+90". There are two rotate scripts: one uses CoreGraphics's CGPDFDocument and CGPDFPage, to create a PDF object, apply a graphical transform to each page and re-save. The second one uses PDFKit's PDFDocument and PDFPage, which allow the direct setting and getting of a rotation parameter for each page. Easier, but not as much fun.

5. Creator (creator.py)

This script writes a copy of the PDF, changing the "Creator" metadata to the value supplied. Other metadata keys are supplied, allowing the script to be easily modified for other metadata values. If no output file is set, it will overwrite the input file.

6. Add Page Number (pagenumber.py)

This script adds a folio number to facing pages of PDFs. Users can set the offset position from the outer top corner, font, size. There are also settings for the scale, opacity and angle of text. A new file is produced, suffixed "NUM".

7. Export pages as images (pdf2tiff.py)

This script exports each page as a 300dpi RGB TIFF image. Options in the script alow for JPEG and PNG filetypes, resolution, transparency and other parameters. Images are saved to a folder with the name of the original file (minus file extension). If the folder cannot be created, the script fails.

8. Combine images to one PDF (imagestopdf.py)

Modified (improved!) version of an Apple open source script (I hope that's ok!), which takes any number of image files and combines them into pages of one PDF file. 

9. Split PDF into separate files (splitPDF.py)

This script creates separate PDFs for each page in an existing PDF. The page files are saved inside a folder with the name of the source file (minus .pdf extension). The script fails if the folder cannot be made.

10. Save As PDF-X PDF Service (Save As PDF-X.py)

This replaces the PDF Service that Apple removed from MacOS, which saved the PDF after applying a filter that makes the PDF conform to PDF-X3 spec. It will even bring up a Save file dialog. Apple's built-in PDF-X filter is quite poor, so you may want to use a better one.

11. Get Info (getInfo.py)

This scripts outputs all the available PDF metadata for a file: Author, Creator, etc, Number of Pages, Version number, flags for encryption and security.

REVISION HISTORY
Minor improvements continue to be made to all the scripts: this includes improved Unicode string handling; standardized variable and API naming conventions, so that the code can be mixed and used in other scripts more easily; and better sanity checking and error handling. Any contributions on these terms are welcome.

NB:
There are some python scripts written by Apple, in /System/Library/Automator, inside the bundles of PDF Automator actions for Combining PDF Pages, Extracting PDF pages, Watermarking PDFs, and adding gridlines to PDFs. You may want to have a look at those.

LICENCE:

"I have gathered a garland of other men's flowers, and nothing is mine but the cord that binds them." These scripts were not possible without looking at other code examples; nor without help and advice from a range of people. I cannot make any claim to them, and they are free to be used and adapted in any way, though I ask that you retain the acknowledgements within. I welcome help in improving them.

Ben Byram-Wigfield
