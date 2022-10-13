# import required libraries
from gtts import gTTS
import PyPDF2
import os

# open PDF file
pdf_file=open("name.pdf",'rb')

# create PDF reader object
pdf_reader=PyPDF2.PdfFileReader(pdf_file)

# count number of pages
pages=pdf_reader.numPages
text=[]

# extract text data from each page 
for i in range(pages):
    try:
        page=pdf_reader.getPage(i)
        text.append(page.extractText())
    except:
        pass

# join all data of all pages
textstring=" ".join(text)

print(textstring)

# set language to english
l='en'

# call gtts
audio=gTTS(text=textstring,lang=l,slow=False)

#save file
audio.save("Audio.mp3")