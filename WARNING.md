# Limitations of MacOS PDF routines

When generating PDF documents, MacOS creates the document to the lowest PDF version number that can completely describe the document's content. By default, it creates PDFs that conform to the PDF 1.3 specification. However, certain features, such as alpha channels, transparency, 16-bit images, encryption, etc, are implemented in later versions of the PDF format, resulting in a document with a higher PDF version number. MacOS generally creates documents in the range PDF 1.3 to 1.6.

Other PDF-creating software, like Adobe Acrobat, can produce PDFs that use features not supported by MacOS. Re-saving those documents using the PDF routines built-in to MacOS may cause the loss of those newer capabilities in the document. (The same issue is true for other apps that use the Quartz APIs, like Apple's own Preview.)

**For most purposes, this will not be a problem**, as MacOS's PDF capabilities are entirely sufficient to describe 2D graphical output from Mac applications -- graphics, text, etc -- as well as including document metadata and structure like annotations, links and bookmarks.

However, it is worth mentioning that many of the utilities in _PDFsuite_ create a new PDF file; some can over-write the original. Even editing the metadata (Title, Author, Creator, etc) can re-write the entire PDF. If you have complex workflows that rely on sophisticated features of PDFs, then you should check whether the created files will work for you.

Again, if your PDFs do NOT originate from any other PDF-creator, then there is no problem. I use these scripts on a daily basis!

A list of the features included in each PDF version can be found here:  

https://www.prepressure.com/pdf/basics/version

PDFs created to conform to standards like PDF/X or PDF/A, will similarly lose these characteristics when re-saved by MacOS. It is possible to re-save the PDFs with other software to restore conformity to the standard.

I hope to add python scripts that use third-party libraries to create and manipulate PDFs beyond the limitations of MacOS's routines in the near future.
