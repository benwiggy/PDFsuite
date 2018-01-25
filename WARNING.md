# Limitations of MacOS PDF routines

MacOS creates PDFs that are compatible with the PDF 1.3 specification. Other PDF-creating software, like Adobe Acrobat, can produce PDFs with higher version numbers. Higher version numbers provide newer capabilities like 3D objects, enhanced metadata, better compression and improved encryption. Re-saving those documents using the PDF routines built-in to MacOS may cause the loss of those newer capabilities in the document.

**For most purposes, this will not be a problem,** as the 1.3 version is entirely sufficient to describe 2D graphical output from Mac applications -- graphics, text, etc -- as well as including document structure like annotations and bookmarks.

Many of the utilities here create a new PDF file, or over-write the original. Even editing the metadata (Title, Author, Creator, etc) writes the entire PDF. These new PDFs will be written to PDF 1.3 spec.

The same issue is true for other apps that use the Quartz APIs, like Apple's own Preview. Of course, if your PDFs do NOT originate from any other PDF-creator, then again there is no problem. I use these scripts on a daily basis!

A list of the features included in each PDF version can be found here:  

https://www.prepressure.com/pdf/basics/version

PDFs created to conform to standards like PDF/X or PDF/A, will similarly lose these characteristics when re-saved by MacOS. It is of course entirely possible to re-save the PDFs to restore conformity to the standard.

I hope to add python scripts that use third-party libraries to create and manipulate PDFs beyond the limitations of MacOS's routines in the near future.
