import cv2
import pytesseract
from PIL import Image
import numpy as np
import argparse
import os

def ocr_credits(video_path, output_file):
    pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"  # Set the path to your tesseract executable if needed

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0

    unique_lines = set()

    with open(output_file, "w") as f:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            if frame_count % (fps * 2) == 0:  # Process every 2 seconds
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

                pil_img = Image.fromarray(thresh)
                text = pytesseract.image_to_string(pil_img, lang="eng", config="--psm 6")
                text = text.strip()

                if text and text not in unique_lines:
                    unique_lines.add(text)
                    f.write(text + "\n")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()
    
def get_output_file(video_path):
    video_dir, video_file = os.path.split(video_path)
    video_name, _ = os.path.splitext(video_file)
    output_file = os.path.join(video_dir, f"{video_name}.txt")
    return output_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from rolling credits")
    parser.add_argument("video_path", help="Path to the video file containing the credits")
    args = parser.parse_args()
    output_file = get_output_file(args.video_path)
    ocr_credits(args.video_path, output_file)