[中文版](README.zh.md)

# PNG to Grayscale Converter

## Overview
This Python script, "Convert.py," is designed to convert all PNG images in the current directory to grayscale images. It utilizes the OpenCV library to process the images, making it a simple and efficient tool for batch grayscale conversion.

## Features
- **Batch Conversion:** Automatically converts all PNG images in the current directory to grayscale.
- **Image Processing:** Uses OpenCV for image reading and conversion.
- **Ease of Use:** Simple execution without complex configurations.

## Requirements
- Python 3
- OpenCV Python library (`cv2`)

## Installation
1. Ensure Python 3 is installed on your system.
2. Install the OpenCV library: `pip install opencv-python`.

## Usage
1. Place the script in the directory containing the PNG images.
2. Run the script using Python: `python Convert.py`.
3. All PNG images in the directory will be converted to grayscale and saved with a `gray_` prefix.

```txt
# Selected Code Snippet from Script
import cv2
import os
import glob

# Get all png files in the current directory
png_files = glob.glob('*.png')

# Iterate through the found png files
for file in png_files:
    # Read the image file
    image = cv2.imread(file)
    # Convert to grayscale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Build the path for saving the grayscale image
    gray_image_path = 'gray_' + file
    # Save the grayscale image
    cv2.imwrite(gray_image_path, gray_image)

print("All PNG images have been converted to grayscale.")
```
