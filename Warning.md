# Limitations of MacOS PDF routines

Since the inception of MacOS (OS X) back in 2001, it has integrated PDF into its core graphics frameworks. This allows users to save any document as a PDF, and it also lets developers produce routines to convert, edit and manipulate PDFs with just a few lines of code (as you can see!). These scripts use the same framework as Apple's own Preview app.

However, there are a few notes of caution that need to be remembered when using the Quartz/Core Graphics APIs for PDFs in MacOS.

1. Other PDF-creating software, like Adobe Acrobat, can produce PDFs that contain features not supported by MacOS (3D objects, advanced encryption, compression and metadata, PDF-X and PDF-A specifications, embedded scripts and files). Re-saving these documents using the PDF routines built-in to MacOS may cause the loss of these capabilities in the document.  While this should not affect the 'visible' aspects of the files, PDF files that need to include additional features may need further processing in other software in order to restore any such characteristics.

It is therefore worth mentioning that because many of the utilities in _PDFsuite_ create new PDF files, and some can over-write the original, you should check whether the created files will work for you, if you need these additional features.

2. Recent versions of OS X (Sierra 10.12 and High Sierra 10.13) have introduced a number of bugs into the PDFKit framework.  **Sierra should be avoided where possible for MacOS-based PDF workflows.** High Sierra seems to have made some improvements. However, the bugs are mainly in areas such as annotations and hidden text layers, which are not the focus of these scripts (yet). The only known issue that affects the scripts is that PDFs encrypted on Sierra will have their metadata (Title, Creator, Author, etc.) corrupted. The last two characters of each field will be lost.

***I use these scripts on a daily basis, as part of a print workflow!*** I needed to find an alternative to Acrobat for creating PDFs from images, combining PDF files generated from apps and producing booklet spreads for printing. It was this need that led me to create these scripts.


I hope to add python scripts that use third-party libraries to create and manipulate PDFs beyond the limitations of MacOS's routines in the near future.
