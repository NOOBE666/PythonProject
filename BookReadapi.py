import PyPDF2
import pyttsx3

book=open('Subhash Bose.pdf','rb')
read=PyPDF2.PdfReader(book)
pages=len(read.pages)

speaker=pyttsx3.init()
for i in range(pages):
    choose_page=read.pages[i]
    text=choose_page.extract_text()
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice',voices[0].id)
    speaker.say(text)

speaker.runAndWait()
