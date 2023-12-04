# this code reads the text from an image(if the image has any text), we are using google colab and mounting google drive for storing the image url's locally the images are then stored in the image folder inside the Gen AI Internship.
from google.colab import drive
drive.mount('/content/drive')

!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install validators
!pip install tensorflow

from google.colab import files, drive
import requests
from PIL import Image
import pytesseract
import os
import validators

# Function to save image to Google Drive
def save_image(url, local_path):
    response = requests.get(url)
    with open(local_path, 'wb') as f:
        f.write(response.content)

import pandas as pd

# Load image URLs from Excel
excel_file_path = '/content/drive/MyDrive/Gen AI Intership/output.xlsx'
df = pd.read_excel(excel_file_path)

# Specify the column containing image URLs
url_column = 'img_url'

# Specify the base directory for saving images to Google Drive
save_directory_base = '/content/drive/MyDrive/Gen AI Intership/images/'

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    image_url = row[url_column]

    # Generate a unique filename based on the index
    filename = f"{index + 1}.jpg"

    # Create the full save path
    save_path = os.path.join(save_directory_base, filename)

    # Save the image to Google Drive
    save_image(image_url, save_path)

    # Perform OCR on the saved image
    extracted_text = pytesseract.image_to_string(Image.open(save_path))

    # Print the extracted text
    print(f"Image {index + 1} - {filename}:")
    print(extracted_text)
    print("------------------------")
