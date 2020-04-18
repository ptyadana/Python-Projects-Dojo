import PyPDF2

reader_pdf = PyPDF2.PdfFileReader(open('pdfs/processed/super.pdf','rb'))
reader_wm  = PyPDF2.PdfFileReader(open('pdfs/wtr.pdf','rb'))
    
writer = PyPDF2.PdfFileWriter()

total_pages = reader_pdf.numPages
for page_number in range(total_pages):
    page = reader_pdf.getPage(page_number)
    page.mergePage(reader_wm.getPage(0))
    writer.addPage(page)

with open('./pdfs/processed/watermarked_super.pdf','wb') as wm_file:
    writer.write(wm_file)
