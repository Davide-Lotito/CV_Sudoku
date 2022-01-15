import cv2 
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def image_to_digit(image):
    custom_config = r'--oem 3 --psm 6' # Adding custom options
    s = pytesseract.image_to_string(image, config=custom_config)
    try:
        return int(s)
    except:
        pass    




