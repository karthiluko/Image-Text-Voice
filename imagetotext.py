import pytesseract
import cv2
from texttovoice import voice
import os
from capture import capimage

capimage()


img1=cv2.imread(r"C:\Users\Karthi\opencv_frame_0.png")
cv2.imshow("image",img1)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
    textfile = pytesseract.image_to_string(img1, lang='eng')
    print(textfile)
    path="newtext.txt"
    f=open(path,'w')
    f.write(textfile)
    f.close()
    voice(path)

    if os.path.exists("newtext.txt"):
        os.remove("newtext.txt")
except:
    grayimg=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grayimg,(3,3),0)
    thresh=cv2.threshold(blur,0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    noisereduced=cv2.fastNlMeansDenoising(thresh,None,10,7,21)
    invert=255-noisereduced
    textfile = pytesseract.image_to_string(invert, lang='eng')

    print(textfile)
    path="newtext.txt"
    f=open(path,'w')
    f.write(textfile)
    f.close()
    voice(path)

    if os.path.exists("newtext.txt"):
        os.remove("newtext.txt")


