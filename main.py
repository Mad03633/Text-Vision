import cv2 
import pytesseract

# The path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img: cv2.Mat = cv2.imread("images\image2.jpg")

# Convert the image to grayscale for better thresholding 
gray: cv2.Mat = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding and binary inversion to the grayscale image 
ret: float
thresh1: cv2.Mat
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Define a rectangular structuring element for dilation
rect_kernel: cv2.Mat = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Apply dilation to the thresholding image to join text regions
dilation: cv2.Mat = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Find contours from the dilated image
contours: list
hierarchy: cv2.Mat
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create a copy of the original image to draw rectangles on detected text
im2: cv2.Mat = img.copy()

# Clear the content of the output file
file: object = open("recognized.txt", "w+")
file.write("")
file.close

# Loop through each detected contour
for cnt in contours:
    # Get the bounding box for each contour
    x: int # X-coordinate of the top-left corner of the bounding box
    y: int # Y-coordinate of the top-left corner of the bounding box
    w: int # Width of the bounding box 
    h: int # Height of the bounding box
    x, y, w, h = cv2.boundingRect(cnt)

    # Draw a rectangle around the detected text region 
    rect: cv2.Mat = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Crop the detected text region from the image
    cropped: cv2.Mat = im2[y:y + h, x:x + w]

    # Appent mode
    file = open("recognized.txt", "a")

    # Extract text from the cropped region using Tesseract OCR
    text: str = pytesseract.image_to_string(cropped)

    file.write(text)
    file.write("\n")
    file.close()