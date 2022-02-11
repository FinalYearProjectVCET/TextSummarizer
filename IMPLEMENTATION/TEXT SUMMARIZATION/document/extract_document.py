import PyPDF2 

class Document:
    
    def extractPDF(self, inputFileName):
        
        input_text = ""
        
        pdfFileobj = open(inputFileName,'rb')

        pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
        
        for i in range(pdfReader.numPages):
            pageobj = pdfReader.getPage(i)

            with open('text.txt','a')as file:
                content  = pageobj.extractText()
                file.write(content)
                        
            input_text += pageobj.extractText()            

        pdfFileobj.close()

        return input_text