# Import required packages
import cv2
import sys
import pytesseract
from PIL import Image
  
# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "/home/berkay/anaconda3/envs/dev/bin/tesseract"
  
def ittMain(fn):
    text = pytesseract.image_to_string(Image.open(fn), lang="eng")
    print(text)

 
