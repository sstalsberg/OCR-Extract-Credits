# OCR-Extract-Credits
Python script that uses OCR (Optical Character Recognition) to extract text and end roll credits from a movie or video and save it to a text file.
The script process a frame every 2 seconds. This can be changed in the code if needed for more or less accuracy. See frame_count in the script.

The code also recognizes similar lines and only wirte new lines to the output file.

To accomplish this task you need OpenCV, pytesseract, and PIL libraries. 

Install these libraries using pip:
```
pip install opencv-python
pip install pytesseract
pip install pillow
```
Then install Tesseract on your machine.

For Windows, you can download the installer from the following link: https://github.com/UB-Mannheim/tesseract/wiki

For Linux, you can install it using the package manager. For example, on Ubuntu or Debian:
```
sudo apt-get install tesseract-ocr
```
For macOS, you can use Homebrew:
```
brew install tesseract
```

Download the python script and edit extract_credits.py so the path to tesseract is correct.

Example
```py
    pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"  # Set the path to your tesseract executable if needed
```
Finally run with:
```
python extract_credits.py path/to/video.mp4
```
