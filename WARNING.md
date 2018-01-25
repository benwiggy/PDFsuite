# WARNING!

MacOS creates PDFs compatible with the PDF 1.3 specification. This is sufficient for graphical output from Mac applications -- graphics, text, etc. Higher version numbers provide extensions for newer capabilities. For example, if you encrypt a PDF using MacOS, the PDF version number increases to 1.4, because the OS uses 128-bit encryption, which was added to PDF in the 1.4 spec.

Many of the utilities here create an entirely new PDF file, or over-write the original. Even editing the metadata (Title, Author, Creator, etc) writes the entire PDF. Such PDFs will be written to PDF 1.3 spec. If your PDF originated from another PDF-creator, such as Adobe Acrobat, and was created with newer features found in later versions, these features will be lost in the rewrite.

A list of the features included in each PDF version can be found here:  

https://www.prepressure.com/pdf/basics/version

PDFs created to other standards, like PDF/X or PDF/A, will similarly lose these characteristics when saved by MacOS.

Python scripts that use alternative PDF engines, such as PyPDF2, will be added here, which may be of use to overcome this limitation.
