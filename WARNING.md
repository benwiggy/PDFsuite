# WARNING!

MacOS creates PDFs that are compatible with the PDF 1.3 specification. Other PDF-creating software, like Adobe Acrobat, can produce PDFs with features beyond the 1.3 spec, and these documents will have higher version numbers. Re-saving those documents using the PDF routines built-in to MacOS may cause the loss of those newer features in the document.

For most purposes, this will not be a problem, as the 1.3 version is entirely sufficient to describe 2D graphical output from Mac applications -- graphics, text, etc -- as well as to include document structure like annotations and bookmarks. There is no danger of any visual elements being lost!  
Higher version numbers provide extensions for newer capabilities (e.g. 3D objects, enhanced metadata, better encryption.) For example, if you encrypt a PDF using MacOS, the PDF version number increases to 1.4, because the OS uses 128-bit encryption, which was only added to PDF in the 1.4 specification.

Many of the utilities here create a new PDF file, or over-write the original. Even editing the metadata (Title, Author, Creator, etc) writes the entire PDF. These new PDFs will be written to PDF 1.3 spec.

The same issue is true for other apps that use the Quartz APIs, like Apple's own Preview. Of course, if your PDFs do NOT originate from any other PDF-creator, then there is nothing to worry about.

A list of the features included in each PDF version can be found here:  

https://www.prepressure.com/pdf/basics/version

PDFs created to other standards, like PDF/X or PDF/A, will similarly lose these characteristics when re-saved by MacOS.

I hope to add python scripts that use other libraries to harness increased power and precision over PDFs in the near future.
