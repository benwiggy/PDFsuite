## Shell scripts
### Apply Quartz Filter (quartzfilter.py)
This replaces Apple's own _quartzfilter_ command, which was removed from OS X (in Snow Leopard). (Also, there was a sample script in Xcode, which used now-deprecated APIs.) Like its predecessor, it takes three arguments: the input file, the path to the quartz filter, and an output filename. It could be easily modified along the lines of the other scripts, to apply one fixed filter to all files given as arguments. _(Like the Save As PDF-X.py script in PDF Services.)_

### Creator (creator.py)
This script alters PDFs, changing the "Creator" metadata to the value supplied. Other metadata keys are supplied, allowing the script to be easily modified for other metadata values. If no output file is set, it will overwrite the input file.  
creator.py -c CreatorName -i inputfile [-o outputfile]

### Get Info (getInfo.py)
This script outputs all the available PDF metadata for a file: Author, Creator, etc, Number of Pages, Version number, flags for encryption and security.

### Get PDF from Clipboard (getPDFclip.py)
This script takes PDF data from the MacOS clipboard, and saves it to a named file. If the file already exists, the PDF is added as a new page to the existing file. (Thus making an impromptu Scrapbook of saved PDF data.)

### List Quartz Filters (listFilters.py)
This script returns the internal name and filepath of all Quartz Filters installed. These can be in any of the three Library/Filters folders (user, root, system), or the PDF Services folders.

### Page Layout (pagelayout.py)
This script provides functions to easily draw rectangles, circles, lines, and text on a PDF page, with colours and transparency. It saves the results to file called "Test.pdf" on the user's Desktop. It is simply a "proof of concept" for a text-based description of graphical items.
