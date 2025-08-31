import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open('text.png'))
print(text)