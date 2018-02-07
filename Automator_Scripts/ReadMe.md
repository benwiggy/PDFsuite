## Automator Services

1. Download the scripts.
2. Launch Automator and create a New Service.
3. Set the drop-down menus to read "Service receives **PDF Files** in **Finder**".
4. Add "Run Shell Script" action. (under "Utilities".)
5. Set the shell drop-down list to **/usr/bin/python** and "Pass input" to **as arguments**.
6. Paste in the script you want to use (replacing the existing text). 

### Add Blank Page (addpage.py)
This script adds a blank page to the front of a PDF file. Currently, the page size is set in the script. Default is A4.

### Add Index Numbers (indexnumbers.py)
This script adds the text "n of x" on the first page of all PDFs passed to it, where x is the number of files in the batch and n is the ordinal number of each file, e.g. _1 of 3, 2 of 3, 3 of 3_

### Add Page Number (pagenumber.py)
This script adds a folio number to facing pages of PDF files supplied as arguments. Users can set the offset position from the outer top corner, font, size. There are also settings for the scale, opacity and angle of text. A new file is produced, suffixed "NUM". A slightly modified version of this script is used to produce text watermarks (watermark.py).

### Combine images to one PDF (imagestopdf.py)
Modified (improved!) version of an Apple open source script, which takes any number of image files (supplied as arguments) and combines them into pages of one PDF file. This script is several seconds faster than Apple's own Automator action.

### Count pages in PDF (countpages.py)
This counts the number of pages in one or more PDF files passed to it. It provides a cumulative count for multiple file arguments.

### Encrypt PDF or add security (encrypt.py)
This adds encryption and passwords to prevent unauthorized copying, printing, or opening.

### Export Text to txt file (pdf2txt.py)
This script outputs the entire readable text from a PDF file to a .txt file. The text file has the same name as the PDF, with the different file extension. If it already exists, an index number will be added to the filename.

### Export pages as images (pdf2tiff.py)
This script exports each page as 300dpi RGB TIFF images from PDFs supplied as arguments. Options in the script alow for JPEG and PNG filetypes, resolution, transparency and other parameters. Images are saved to a folder with the name of the original file (minus file extension). If the folder cannot be created, the script fails.

### Join PDF files into one file (myjoin.py)
This script will combine all PDF files supplied as arguments into one file, called "Combined.pdf". Files are passed in the order they appear in the Finder window, so re-ordering the List or Column will change the order of selected items for combining.

### Rotate all pages in PDF (rotate.py and rotate2.py)
This will rotate all the pages of any PDF files passed as arguments by 90˚ into a new file suffixed "+90". There are two rotate scripts: one uses CoreGraphics's _CGPDFDocument_ and _CGPDFPage_ to create a PDF object, apply a graphical transform to each page and re-save. The second one uses PDFKit's _PDFDocument_ and _PDFPage_, which allow the direct setting and getting of a rotation parameter for each page.

### Split PDF into separate files (splitPDF.py)
This script creates separate PDFs for each page in an existing PDF. The page files are saved inside a folder with the name of the source file (minus .pdf extension). The script fails if the folder cannot be made.

### Watermark all pages of PDF (watermark.py)
By default, this script adds the word "SAMPLE" in 150pt Helvetica-Bold, at 45˚ angle, with 50% opacity, to every page of PDFs passed to it. These settings can easily be altered.
