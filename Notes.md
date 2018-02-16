# PDFSuite Road-map #

Future plans for these scripts, which are also an indication of their current limitations, include (in no particular order):

1. When using CGPDFDocument to process existing PDF files into new PDF documents, only the 'basic' Doc Info keys are passed: _Title, Author, Creator, etc._.  Other keywords and custom metadata are not passed to new files.

2. When processing multiple files with scripts that create one new file for each input, _(e.g. Watermark, page numbers, etc)_, it might be beneficial to collate the output files into one folder. Otherwise, you get your input and output files all mixed up together. I find that I often want to select and further process the created files.)

3. It is assumed that all PDFs are not encrypted. Future versions should check for encryption and ask for passwords or exit gracefully. (A demonstration script that checks for encryption, ask for a password, unlocks the data and reports on its success is included here as password.py.)

4. While a feature of these scripts is that they will work on any Mac (from Snow Leopard up) without additional software, some scripts using additional third-party python libraries are planned, in order to produce features beyond the scope of MacOS's native capabilities, and to redress concerns about bugs in the OS. This will include PyPDF2, a python PDF library.

5. The scripts should be a bit more python-y, and be more readily 'pluggable' into larger projects.

6. If there's something you want these scripts to do, or something they're not doing that you think they should, please let me know.
