# Install the xlsxwriter package
!pip install xlsxwriter

from google.colab import files
import pandas as pd
import io

# Step 1: Upload the Excel file
uploaded = files.upload()

# Step 2: Read the Excel file
file_name = list(uploaded.keys())[0]
excel_file = pd.ExcelFile(io.BytesIO(uploaded[file_name]))

# Step 3: Delete multiple specific tabs (sheets)
# Specify the sheet names you want to delete
sheets_to_delete = ['cntran0394','cntran0399','cntran0763','cntran0945','cntran1309','cntran1491','cntran1855','cntran0758','cntran1310','cntran0940','cntran1304','cntran1486','cntran0408','cntran0772','cntran0954','cntran1318','cntran1500','cntran1864','cntran0411','cntran0957','cntran0387','cntran0751','cntran0933','cntran1321','cntran1297','cntran1479','cntran1503','cntran1843','cntran1867','cntran0775','cntran0427','cntran0791','cntran0973','cntran1519','cntran1883','cntran1702','cntran1884','cntran1337','cntran0418','cntran0964','cntran0782','cntran1328','cntran1510','cntran1874','cntran1886','cntran0442','cntran0806','cntran0988','cntran1352','cntran1534','cntran1898','cntran0447','cntran1363','cntran0811','cntran0993','cntran1357','cntran0821','cntran1539','cntran1903','cntran1735','cntran1024','cntran1388','cntran1207','cntran1736','cntran1936','cntran1575','cntran1757','cntran1939','cntran1777','cntran1592','cntran1956','cntran0508','cntran0872','cntran1054','cntran1418','cntran1600','cntran1964','cntran0494','cntran0858','cntran1040','cntran1404','cntran1586','cntran1950','cntran1940','cntran1604','cntran0513','cntran0877','cntran1605','cntran1787','cntran1969','cntran0527','cntran0891','cntran1073','cntran1437','cntran1619','cntran1983','cntran0514','cntran1060','cntran1424','cntran1606','cntran1970','cntran1609','cntran0878','cntran1088','cntran1647','cntran0557','cntran0921','cntran1103','cntran1467','cntran1649','cntran2013','cntran0561','cntran0743','cntran0564','cntran0928','cntran0925','cntran2018','cntran0563','cntran0927','cntran1828']  # Replace with the actual sheet names

# Read all sheets except the ones to delete
sheets = excel_file.sheet_names
sheets_to_keep = [sheet for sheet in sheets if sheet not in sheets_to_delete]

# Read the sheets into a dictionary of DataFrames
data_frames = {sheet: excel_file.parse(sheet) for sheet in sheets_to_keep}

# Step 4: Save the modified Excel file
output_path = 'modified_file.xlsx'
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    for sheet_name, df in data_frames.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Provide a download link
files.download(output_path)
