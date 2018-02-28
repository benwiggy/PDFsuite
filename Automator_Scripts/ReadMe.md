## Automator Scripts

Automator workflows containing these scripts, for use as MacOS 'Services', can be found in the 'Automator Services' folder. You can also make your own Automator workflows with them following these instructions:
1. Download the scripts.
2. Launch Automator and create a New Service.
3. Set the drop-down menus to read "Service receives **PDF Files** in **Finder**".
4. Add "Run Shell Script" action. (under "Utilities".)
5. Set the shell drop-down list to **/usr/bin/python** and "Pass input" to **as arguments**.
6. Paste in the script you want to use (replacing the existing text). 

Alternatively, you can use them in the Terminal with PDF files as arguments. Drop the script into a Terminal window, then drop all the files you want to process.

### Add Blank Page (addpage.py)
This script adds a blank page to the end of a PDF file. The page size for the blank page is the same as the first page of the PDF.

### Count pages in PDF (countpages.py)
This counts the number of pages in one or more PDF files passed to it. It provides a cumulative count for multiple file arguments.

### Encrypt PDF or add security (encrypt.py)
This adds encryption and passwords to prevent unauthorized copying, printing, or opening. Note that the passwords are stored in plain text within the body of the script.

### Combine images to one PDF (imagestopdf.py)
Entirely rewritten v2.0 script, that merges all image files into one PDF. This script is several seconds faster than Apple's own Automator action!

### Add Index Numbers (indexnumbers.py)
This script adds the text "n of x" on the first page of all PDFs passed to it, where x is the number of files in the batch and n is the ordinal number of each file, e.g. _1 of 3, 2 of 3, 3 of 3_

### Join PDF files into one file (myjoin.py)
This script will combine all PDF files supplied as arguments into one file, called "Combined.pdf". Files are passed in the order they appear in the Finder window, so re-ordering the List or Column will change the order of selected items for combining.

### Add Page Number (pagenumber.py)
This script adds a folio number to facing pages of PDF files supplied as arguments. Users can set the offset position from the outer top corner, font, size. There are also settings for the scale, opacity and angle of text. A new file is produced, suffixed "NUM". A slightly modified version of this script is used to produce text watermarks (watermark.py).

### Export pages as images (pdf2tiff.py)
This script exports each page as 300dpi RGB TIFF images from PDFs supplied as arguments. Options in the script alow for JPEG and PNG filetypes, resolution, transparency and other parameters. Images are saved to a folder with the name of each original file (minus file extension). If the folder exists, a new one with an incremental number will be made.

### Export Text to txt file (pdf2txt.py)
This script outputs the entire readable text from a PDF file to a .txt file. The text file has the same name as the PDF, with the different file extension. If it already exists, an index number will be added to the filename.

### Rotate all pages in PDF (rotate.py)
This will rotate all the pages of any PDF files passed as arguments by 90˚ into a new file suffixed "+90". (Suffixes are cumulative.)

### Split PDF into separate files (splitPDF.py)
This script creates separate PDFs for each page in an existing PDF. The page files are saved inside a folder with the name of the source file (minus .pdf extension). 

### Trim pages to the Crop Marks (trimPDF.py)
This script compares the trimbox to the mediabox. If the two are different, it crops the page to the trimbox. This may be useful for cropping a PDF that contains crop marks and bleed area to the trimmed page size.

### Watermark all pages of PDF (watermark.py)
By default, this script adds the word "SAMPLE" in 150pt Helvetica-Bold, at 45˚ angle, with 50% opacity, to every page of PDFs passed to it. These settings can easily be altered.
