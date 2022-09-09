import PyPDF2
import os

mergedFilesName = "combinedPDFs.pdf"
merger = PyPDF2.PdfFileMerger()  # alphabetically merging
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write(mergedFilesName)
