# -*- coding: utf-8 -*-
import PyPDF2
import os

pdfPath='./pdfs'

def getSentences(pdfPath,fileName):
    with open(os.path.join(pdfPath,fileName),"rb") as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
        if not read_pdf.isEncrypted:
            #read_pdf.decrypt("")
            number_of_pages =read_pdf.getNumPages()
            #print(number_of_pages)

            page = read_pdf.getPage(0)
            page_content = page.extractText()
            enitireText = page_content.encode('ascii', 'ignore').decode('ascii')


            text=enitireText.split('.')


            return text

if __name__ == '__main__':
    #x = getSentences('15.pdf')
    #l = getSentences('17.pdf')

    #r = x + l
    r = getSentences(pdfPath,'24.pdf')
    print(r)
