import PyPDF2 

pdfFileobj = open('sample.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileobj)

#print(pdfReader.numPages)
for i in range(pdfReader.numPages):
    pageobj = pdfReader.getPage(i)


    with open('text.txt','a')as file:
        content  = pageobj.extractText()
        file.write(content)
    
    
    
    print(pageobj.extractText())

pdfFileobj.close()

