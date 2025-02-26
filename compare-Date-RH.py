import pandas as pd
from google.colab import files

# Upload the Excel file from the local drive
uploaded = files.upload()

# Get the uploaded file name
file_name = list(uploaded.keys())[0]

# Initialize a list to store the results
different_values_list = []

# Load the Excel file using pandas
excel_file = pd.ExcelFile(file_name)

# Loop through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Loop through each row starting from the third row
    for index, row in df.iloc[2:].iterrows():
        # Get the values from the second column to the last column
        values = row[1:].dropna().tolist()

        # Check if all values are the same
        if len(set(values)) > 1:
            # If there are different values, add the sheet name and first column value to the list
            different_values_list.append((sheet_name, row[0]))

# Create a DataFrame from the list of different values
comparison_df = pd.DataFrame(different_values_list, columns=["Sheet", "Date"])

# Save the DataFrame to a new Excel file
comparison_df.to_excel("comparison.xlsx", index=False)

# Download the new Excel file
files.download("comparison.xlsx")
