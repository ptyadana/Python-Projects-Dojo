import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('./pdfs/processed/super.pdf')

if __name__ == "__main__":
    pdf_combiner(inputs)

#how to run
#python pdf_dynamic_merger <file_arg1> <file_arg2> ..etc
#python pdf_dynamic_merger.py pdfs/dummy.pdf pdfs/twopage.pdf
