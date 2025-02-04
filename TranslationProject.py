import os
import xml.etree.ElementTree as ET
from google.colab import files

# Step 1: Upload XML files
print("Please upload your XML files:")
uploaded_files = files.upload()

def replace_in_xml_files(uploaded_files):
    modified_files = {}
    for filename in uploaded_files.keys():
        if filename.endswith('.xml'):
            # Parse the XML file
            tree = ET.ElementTree(ET.fromstring(uploaded_files[filename].decode('utf-8')))
            root = tree.getroot()

            # Replace occurrences of "体重" with "权重"
            for elem in root.iter():
                if elem.text:
                    elem.text = elem.text.replace("体重", "权重")
                if elem.tail:
                    elem.tail = elem.tail.replace("体重", "权重")

            # Save the modified XML file
            modified_file_path = f'modified_{filename}'
            tree.write(modified_file_path, encoding='utf-8', xml_declaration=True)
            modified_files[modified_file_path] = modified_file_path

    return modified_files

# Step 2: Process the uploaded files
modified_files = replace_in_xml_files(uploaded_files)

# Step 3: Download the modified files
for modified_file in modified_files.keys():
    files.download(modified_file)
