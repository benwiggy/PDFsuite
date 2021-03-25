## PDF Services

Copy these files to {user}/Library/PDF Services. You may need to create the folder "PDF Services" in your user Library if it isn't there. The scripts will then be available from the PDF button of the print menu.

NOTICE: As of Big Sur, Apple has increased security so that scripts won't work. You have to place them inside an Automator APPLICATION. Print plug-in or other workflow document won't work.  


### Booklet Imposition (booklet.py)
This script is set to work as a PDF Service. However, it could easily be adjusted to work as an Automator workflow. It takes the input PDF file and lays out the pages on a larger sheet, in booklet spread page order. It checks for page rotation and adjusts if necessary. There's an option to arrange for 4pp signatures (stacked sheets, not gathered). The script brings up a Save dialog.
Booklet sheet size is set in the script (default is A3). Other settings and options, such as creep, can also be set.

### Save As PDF/X  (Save As PDF-X.py)
This replaces the PDF Service that Apple removed from MacOS , which saved the PDF after applying a filter that makes the PDF conform to PDF/X-3 spec. It will even bring up a Save file dialog. Apple's built-in PDF/X filter is a very minimal attempt at compliance with the standard, so you may want to use a better one. 
Some better Quartz Filters can be found here: 
https://github.com/benwiggy/QuartzFilters
The script will look for a Filter named "Better PDF-X3.qfilter", and fall back to the System one if not found.

### Save PDF from ~Stupid~ iWork (Save_PDF_from_iWork.py)
iWork apps (Numbers, Pages, KeyNote) have an annoying feature/bug that they do not remove their file extension from saved PDFs. (E.g. "MyFile.number.pdf".) Using this PDF Service will strip the iWork extension before saving the PDF. (E.g. "MyFile.pdf").

### Watermark with PDF (watermark PDF.py)
This will superimpose one PDF on top of another. Ideal for adding 'letterheads' to any printed output from any app. You will need to supply the filepath and name of the template PDF.

More details about PDF Services can be found here:
https://developer.apple.com/library/content/documentation/Printing/Conceptual/PDF_Workflow/pdfwf_concepts/pdfwf_concepts.html
