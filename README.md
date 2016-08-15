# PDFsuite
Python scripts for MacOS (OS X) that create, manipulate, and query PDF files

These scripts provide 'front ends' to MacOS's Core Graphics APIs, thereby allowing the automation of a variety of tasks, such as creating bookets, applying Quartz Filters and querying page count of input PDFs.

1. Booklet Imposition (booklet.py)

This script is set to work as a PDF Service. However, it could easily be adjusted to work as an Automator workflow. It takes the input PDF file and lays out the pages on a larger sheet, in booklet spread page order.

2. Apply Quartz Filter (quartzfilter.py)

This replaces Apple's own quartzfilter command, which was removed from OS X (in Lion?). (Also, there was a sample script in Xcode, which used now-deprecated APIs.) Like its predecessors, it has three filepath arguments: quartz filter, input file and output file.

3. Count pages in PDF (countpages.py)

This again uses Core Graphics objects and methods to count the number of pages in one or more PDF files passed to it. It provides a cumulative count for multiple files.

4. Rotate (rotate.py)

This will rotate all the pages of any PDF files by 90˚ into a new file suffixed "NUM".

5. Creator (creator.py)

This will write a copy of the PDF, changing the "Creator" metadata to the value supplied. Other metadata keys are supplied, allowing the script to be easily modified for other metadata values. If no output file is set, it will overwrite the input file.

6. Add Page Number (pagenumber.py)

This script adds a page number to facing pages of PDFs. Users can set the offset position from the outer top corner, font, size. There are also settings for the scale, opacity and angle of text.

More scripts are planned: Exporting as bitmaps, Querying PDF data; .... and on!

Ben Byram-Wigfield
