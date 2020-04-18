import PyPDF2

with open('pdfs/dummy.pdf','rb') as file1, open('pdfs/twopage.pdf','rb') as file2:
    merger = PyPDF2.PdfFileMerger()
    merger.merge(0,file1)
    merger.merge(1,file2)

    with open('pdfs/processed/merged.pdf','wb') as merged_file:
        merger.write(merged_file)