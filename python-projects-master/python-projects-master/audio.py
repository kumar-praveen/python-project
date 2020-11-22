import pyttsx3
import PyPDF2
book=open("D:/Audio/romantic1.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
