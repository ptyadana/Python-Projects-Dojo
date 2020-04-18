import PyPDF2

with open('./pdfs/dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getNumPages())

    page = reader.getPage(0)
    page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('./pdfs/processed/tilt.pdf','wb') as new_file:
        writer.write(new_file)