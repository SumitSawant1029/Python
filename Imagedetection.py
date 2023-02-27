import cv2
import pytesseract
import hand
# Modifying the image
img = cv2.imread('test3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilate = cv2.dilate(thresh, kernel, iterations=1)

# Detecting the text in the image
text = pytesseract.image_to_string('test2.jpg')
print(text)

# For Comaparision with the Dataset
dataset = ['Nigel Silveria','Abhay Singh','Sumit Sawant','Afzal siddhiquie']

word = text.split('\n')
print(len(word))


print(word[0])

