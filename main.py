import PyPDF2

pdffileobj = open('resume_test.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)

x = pdfreader.numPages
pageobj = pdfreader.getPage(x - 1)
text = pageobj.extractText()

file1 = open(r'/Users/logan/Desktop/python/resume_scanner/txt/resume_test.txt', 'a')
file1.writelines(text)
file1.close()

keywords = ['Python', 'Java']

try:
    with open('resume_test.txt', 'r', encoding = 'utf-8') as file:
        for line in open('resume_test.txt'):
            for k in keywords:
                if k in line:
                    print(k)

finally:
    file.close()
