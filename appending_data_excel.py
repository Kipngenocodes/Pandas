import pandas as pd
import os

# Reading the JSON file
json_file_path = r'C:\Users\p1\OneDrive\Desktop\Pandas\employee_data.json'

# Converting the JSON file to a DataFrame
df = pd.read_json(json_file_path)
print("DataFrame:")
print(df)

# Path for the Excel file
output_excel_path = r'C:\Users\p1\OneDrive\Desktop\Pandas\employee_data.xlsx'

# Check if the file exists
if not os.path.exists(output_excel_path):
    print(f"File not found: {output_excel_path}. Creating a new Excel file.")
    # Create a new Excel file and write the DataFrame to it
    with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='New_Employee_Data', index=False)
else:
    # If the file exists, append the DataFrame to a new sheet
    print(f"File found: {output_excel_path}. Appending data to it.")
    with pd.ExcelWriter(output_excel_path, mode='a', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='New_Employee_Data', index=False)

print(f"Data written to: {output_excel_path}")
