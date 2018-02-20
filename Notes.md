# PDFSuite Notes #

PDF Suite was last updated February 2018. If you have downloaded before then, please update.

Future plans for these scripts, which are also an indication of their current limitations, include (in no particular order):

1. When processing multiple files with scripts that create one new file for each input, _(e.g. Watermark, page numbers, etc)_, it might be beneficial to collate the output files into one folder. Otherwise, you get your input and output files all mixed up together. I find that I often want to select and further process the created files.)

2. It is assumed that all PDFs are not encrypted. Future versions should check for encryption and ask for passwords or exit gracefully. (A demonstration script that checks for encryption, ask for a password, unlocks the data and reports on its success is included here as password.py.)

3. While a feature of these scripts is that they will work on any Mac (from Snow Leopard up) without additional software, some scripts using additional third-party python libraries are planned, in order to produce features beyond the scope of MacOS's native capabilities, and to redress concerns about bugs in the OS _(See below)_. This will include PyPDF2, a python PDF library.

4. The scripts should be a bit more python-y, and be more readily 'pluggable' into larger projects.
 
5. If there's something you want these scripts to do, or something they're not doing that you think they should, please let me know.

## Limitations ##

1. Other PDF-creating software, like Adobe Acrobat, can produce PDFs that contain features not supported by MacOS (3D objects, advanced encryption, compression and metadata, PDF-X and PDF-A specifications, embedded scripts and files). Re-saving these documents using the PDF routines built-in to MacOS may cause the loss of these capabilities in the document.  While this should not affect the 'visible' aspects of the files, PDF files that need to include additional features may need further processing in other software in order to restore any such characteristics.

It is therefore worth mentioning that because many of the utilities in _PDFsuite_ create new PDF files, and some can over-write the original, you should check whether the created files will work for you, if you need these additional features.

2. Recent versions of OS X (Sierra 10.12 and High Sierra 10.13) have introduced a number of bugs into the PDFKit framework.  **Sierra should be avoided where possible for MacOS-based PDF workflows.** High Sierra seems to have made some improvements. However, the bugs are mainly in areas such as annotations and hidden text layers, which are not the focus of these scripts (yet). The only known issue that affects the scripts is that PDFs encrypted on Sierra will have their metadata (Title, Creator, Author, etc.) corrupted. The last two characters of each field will be lost.

***I use these scripts on a daily basis, as part of a print workflow!*** I needed to find an alternative to Acrobat for creating PDFs from images, combining PDF files generated from apps and producing booklet spreads for printing. It was this need that led me to create these scripts.


## Python on the Mac ##
These scripts are designed to work with the PyObjC Cocoa bridge and Python version currently bundled with MacOS. There are newer versions of python and PyObjC available, but the portability of the vanilla experience is preferred. 

If you're interested in python scripts, there are some python scripts written by Apple, in _/System/Library/Automator_, inside the bundles of PDF Automator actions for Combining PDF Pages, Extracting PDF pages, Watermarking PDFs, and adding gridlines to PDFs. There are also some open source python scripts on [Apple's open source pages](https://opensource.apple.com/source/pyobjc/pyobjc-49/pyobjc/pyobjc-framework-Quartz-2.5.1/Examples/), though some of these don't work on default installations.
