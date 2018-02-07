# PDFSuite Road-map #

Future plans for these scripts, which are also an indication of their current limitations, include (in no particular order):

1. When using CGPDFDocument to process existing PDF files into new PDF documents, only the 'basic' Doc Info keys are passed: _Title, Author, Creator, etc._.  
Other keywords and custom metadata are not passed to new files. Scripts using PDFKit's PDFDocument pass all such metadata by default.

2. When processing multiple files with scripts that create one new file for each input, _(e.g. Watermark, page numbers, etc)_, it might be beneficial to collate the output files into one folder. Otherwise, you get your input and output files all mixed up together. I find that I often want to select and further process the created files.)

3. Currently, scripts that create folders _(pdf2tiff, splitPDF)_ will fail if the folder already exists. They should create a folder with a unique name.

4. Because of (current) concerns about bugs in the PDF frameworks of MacOS, and in order to produce features beyond the scope of MacOS's capabilities, alternative scripts using third-party software libraries are planned. This will include PyPDF2, a python PDF library.

5. It is assumed that all PDFs are not encrypted. Future versions should check for encryption and ask for passwords or exit gracefully.
