# Limitations of MacOS PDF routines

Since the inception of MacOS (OS X) back in 2001, it has integrated PDF into its core graphics frameworks. This allows users to save any document as a PDF, and it also lets developers produce routines to convert, edit and manipulate PDFs with just a few lines of code (as you can see!). 

However, there are a few notes of caution that need to be remembered when using the Quartz/Core Graphics APIs for PDFs in MacOS.

1. Other PDF-creating software, like Adobe Acrobat, can produce PDFs that contain features not supported by MacOS (3D objects, advanced encryption and metadata, embedded scripts and files). Re-saving these documents using the PDF routines built-in to MacOS may cause the loss of those newer capabilities in the document. (The same is true when saving from Apple's Preview, or other apps that use the Quartz APIs.)  
 
Similarly, PDFs created to conform to standards like PDF/X or PDF/A, will similarly lose these characteristics when re-saved by MacOS. It is possible to re-save the PDFs with other software to restore conformity to the standard.

It is therefore worth mentioning that because many of the utilities in _PDFsuite_ create new PDF files, and some can over-write the original, you should check whether the created files will work for you without issue. 

2. Recent versions of OS X (Sierra 10.12 and High Sierra 10.13) have introduced a number of bugs into the PDFKit framework.  **Sierra should be avoided where possible for MacOS-based PDF workflows.** High Sierra seems to have made some improvements. However, the bugs are mainly in areas such as annotations, hidden text layers and outlines, which are not the focus of these scripts (yet). The only known issue that affects the scripts is that PDFs encrypted on Sierra will have their metadata (Title, Creator, Author, etc.) corrupted. The last two characters of each field will be lost.

***I use these scripts on a daily basis, as part of print workflow!***


I hope to add python scripts that use third-party libraries to create and manipulate PDFs beyond the limitations of MacOS's routines in the near future.
