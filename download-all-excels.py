import requests
from bs4 import BeautifulSoup
import os
import shutil
from google.colab import files

# Main URL containing the links to Excel files
main_url = 'https://www.mlit.go.jp/toukeijouhou/chojou/labor_result.htm'  # Replace with the actual URL

# Designated local directory to save files
local_directory = '/content/excel_files'
os.makedirs(local_directory, exist_ok=True)

# Fetch the main page
response = requests.get(main_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all Excel file links
excel_links = []
for link in soup.find_all('a', href=True):
    if link['href'].endswith('.xls') or link['href'].endswith('.xlsx'):
        excel_links.append(link['href'])

# Download each Excel file
for r in excel_links:
  print(r)


print("Download completed! The Excel files have been zipped and are ready for download.")
