# Text Vision: Text Detection and Extraction

A Python-based application that detects and extracts text from images using OpenCV and Tesseract OCR.

## Features
- **Text Detection**: Identifies text regions in images using image processing techniques.
- **Text Extraction**: Extracts text from detected regions using Tesseract OCR.
- **Custom Output**: Saves the extracted text to a file (`recognized.txt`).

## Requirements
- Python 3.8+
- Tesseract OCR
- OpenCV
- pytesseract

## Installation

### Install Tesseract OCR

Download and install [Tesseract OCR.](https://github.com/tesseract-ocr/tesseract)
Ensure the path to the tesseract.exe file is added to the script:

```
pytesseract.pytesseract.tesseract_cmd = r'path' 
# Usually it is located in C:\Program Files\Tesseract-OCR\tesseract.exe
```

## Example

Image:
![](/images/image2.jpg)

Output:
![](/images/output2.png)
