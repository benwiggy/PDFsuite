# PDFSuite Notes #

## Python on the Mac ##
Apple has announced that Catalina will be the last version of MacOS to ship with python 2.7. Furthermore, python 2 will be 'end-of-lifed' in 2020. This means that in MacOS 10.16 (to be released in September 2020), the user will have to install python3 and PyObjC to use the scripts. I plan to update the scripts to use python 3 and the latest version of PyObjC before then, rather than the versions that have shipped with MacOS before that date. The alternative might be to rewrite using Swift *(Hmmm)* or AppleScript-ObjC *(Eurghhh)*, in order to maintain the ease-of-use without dependencies.  
However, I enjoy writing with python, so will certainly continue using them myself!

Anyone wishing to use these scripts on python3: most should work if you remove all the utf-8 encode-decode functions, and make sure that print has brackets round everything.

## Future plans ##
Future plans for these scripts, which are also an indication of their current limitations, include (in no particular order):

1. When processing multiple files with scripts that create one new file for each input, _(e.g. Watermark, page numbers, etc)_, it might be beneficial to collate the output files into one folder. Otherwise, you get your input and output files all mixed up together. I find that I often want to select and further process the created files.)

2. It is assumed that all PDFs are not encrypted. Future versions should check for encryption and ask for passwords or exit gracefully. (A demonstration script that checks for encryption, ask for a password, unlocks the data and reports on its success is included here as password.py.)

3. The abilities of these scripts will be merged with CUPS backends, to create virtual printers that can automatically perform actions on PDFs as part of a print queue. (though CUPS backends are being phased out.)

4. The scripts should be a bit more python-y, and be more readily 'pluggable' into larger projects. 
 
5. If there's something you want these scripts to do, or something they're not doing that you think they should, please let me know. If anyone wants to help with improving the scripts in these ways, please jump in!

## Limitations ##

1. Other PDF-creating software, like Adobe Acrobat, can produce PDFs that contain features not supported by MacOS (3D objects, advanced encryption, compression and metadata, PDF-A specifications, embedded scripts and files). Re-saving these documents using the PDF routines built-in to MacOS _**may**_ cause the loss of these capabilities in the document.  While this should not affect the 'visible' aspects of the files, PDF files that need to include additional features may need further processing in other software in order to restore any such characteristics.

It is therefore worth mentioning that because many of the utilities in _PDFsuite_ create new PDF files, and some can over-write the original, you should check whether the created files contain all the characteristics that you require.

2. Some versions of OS X (Sierra 10.12 and High Sierra 10.13) have introduced a number of bugs into the PDFKit framework.  **Sierra should be avoided where possible for MacOS-based PDF workflows.** High Sierra seems to have made some improvements. However, the bugs are mainly in areas such as annotations and hidden text layers, which are not the focus of these scripts (yet). The only known issue that affects the scripts is that PDFs encrypted on Sierra will have their metadata (Title, Creator, Author, etc.) corrupted. The last two characters of each field will be lost. MacOS 10.14 Mojave has now fixed many of the bugs introduced in Sierra.

***I use these scripts on a daily basis, as part of a print workflow!*** I needed to find an alternative to Acrobat for creating PDFs from images, combining PDF files generated from apps and producing booklet spreads for printing. It was this need that led me to create these scripts.

