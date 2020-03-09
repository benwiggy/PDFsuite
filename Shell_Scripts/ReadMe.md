## Shell scripts
### Apply Quartz Filter (quartzfilter.py)
This replaces Apple's own _quartzfilter_ command, which was removed from OS X (in Snow Leopard). (Also, there was a sample script in Xcode, which used now-deprecated APIs.) Like its predecessor, it takes three arguments: the input file, the path to the quartz filter, and an output filename.  
If the filter is supplied as a name only, without full filepath (e.g. "Sepia Tone.qfilter"), the script will search for installed filters of that name and get the complete filepath.  
It could be easily modified along the lines of the other scripts, to apply one fixed filter to all files given as arguments. _(Like the Save As PDF-X.py script in PDF Services.)_

### Create Table of Contents (createPDFOutlines.py)
This script automates the addition of entries ('outlines') in the Table of Contents of a PDF file. Currently, the filepath of the PDF (and the output) must be set in the script, along with the page numbers and names of the bookmarks.

### Get PDF Outlines (getPDFOutlines.py)  
This script returns the Table of Contents data from a PDF file, as text. The results are an index number, the name ('label') of the entry, and the 'action' it represents, (usually a page value, co-ordinate, and zoom factor). 

### Creator (creator.py)
This script alters PDFs, changing the "Creator" metadata to the value supplied. Other metadata keys are supplied, allowing the script to be easily modified for other metadata values. If no output file is set, it will overwrite the input file.  
creator.py -c CreatorName -i inputfile [-o outputfile]

### Get Info (getInfo.py)
This script outputs all the available PDF metadata for a file: Author, Creator, etc, Number of Pages, Version number, flags for encryption and security.

### Make PDF from Clipboard (getPDFclip.py)
This script takes image data from the MacOS clipboard, and saves it to a named PDF file. If the file already exists, the PDF is added as a new page to the existing file. (Thus making an impromptu Scrapbook of saved image data.)

### List Quartz Filters (listFilters.py)
This script returns the internal name and filepath of all Quartz Filters installed. These can be in any of the three Library/Filters folders (user, root, system), or the PDF Services folders.

### PDF Text Search (pdfsearch.py)
This script provides the necessary functionality to search a PDF for a given text string. Results may depend on the way that the text has been encoded and formatted.

### Page Layout (pagelayout.py)
This script provides functions to allow the drawing of rectangles, circles, lines, and text on a PDF page, with colours and transparency, using simple, one-line commands. It saves the results to file called "Test.pdf" on the user's Desktop. It is simply a "proof of concept" for the creation of graphical items using a simple text description. (PostScript it aint!)
