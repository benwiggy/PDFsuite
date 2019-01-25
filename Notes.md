# PDFSuite Notes #

PDF Suite was last updated January 2019. If you have downloaded before then, please update.

Future plans for these scripts, which are also an indication of their current limitations, include (in no particular order):

1. When processing multiple files with scripts that create one new file for each input, _(e.g. Watermark, page numbers, etc)_, it might be beneficial to collate the output files into one folder. Otherwise, you get your input and output files all mixed up together. I find that I often want to select and further process the created files.)

2. It is assumed that all PDFs are not encrypted. Future versions should check for encryption and ask for passwords or exit gracefully. (A demonstration script that checks for encryption, ask for a password, unlocks the data and reports on its success is included here as password.py.)

3. The abilities of these scripts will be merged with CUPS backeds, to create virtual print queues that can automatically perform these actions on PDFs.

4. The scripts should be a bit more python-y, and be more readily 'pluggable' into larger projects.
 
5. If there's something you want these scripts to do, or something they're not doing that you think they should, please let me know.

## Limitations ##

1. Other PDF-creating software, like Adobe Acrobat, can produce PDFs that contain features not supported by MacOS (3D objects, advanced encryption, compression and metadata, PDF-A specifications, embedded scripts and files). Re-saving these documents using the PDF routines built-in to MacOS _**may**_ cause the loss of these capabilities in the document.  While this should not affect the 'visible' aspects of the files, PDF files that need to include additional features may need further processing in other software in order to restore any such characteristics.

It is therefore worth mentioning that because many of the utilities in _PDFsuite_ create new PDF files, and some can over-write the original, you should check whether the created files contain all the characteristics that you require.

2. Some versions of OS X (Sierra 10.12 and High Sierra 10.13) have introduced a number of bugs into the PDFKit framework.  **Sierra should be avoided where possible for MacOS-based PDF workflows.** High Sierra seems to have made some improvements. However, the bugs are mainly in areas such as annotations and hidden text layers, which are not the focus of these scripts (yet). The only known issue that affects the scripts is that PDFs encrypted on Sierra will have their metadata (Title, Creator, Author, etc.) corrupted. The last two characters of each field will be lost. MacOS 10.14 Mojave has now fixed many of the bugs introduced in Sierra.

***I use these scripts on a daily basis, as part of a print workflow!*** I needed to find an alternative to Acrobat for creating PDFs from images, combining PDF files generated from apps and producing booklet spreads for printing. It was this need that led me to create these scripts.


## Python on the Mac ##
These scripts are designed to work with the PyObjC Cocoa bridge and Python version currently bundled with MacOS. There are newer versions of python and PyObjC available, but the portability of the vanilla experience is preferred. 

If you're interested in python scripts, there are some python scripts written by Apple, in _/System/Library/Automator_, inside the bundles of PDF Automator actions for Combining PDF Pages, Extracting PDF pages, Watermarking PDFs, and adding gridlines to PDFs. (Though they're not as good as PDFSuite!) There are also some open source python scripts on [Apple's open source pages](https://opensource.apple.com/source/pyobjc/pyobjc-49/pyobjc/pyobjc-framework-Quartz-2.5.1/Examples/), though some of these no longer work on newer OS versions.
