# Excel Classifier
A PySide6-based desktop application to help you split large Excel files into smaller, more manageable files based on unique values in a specified column.

## Overview
Excel Classifier simplifies the task of organizing data within Excel files. By defining a column, users can break down a single large Excel file into multiple files, each containing rows that share the same value in the specified column.

### Example Use Case
Imagine you have an Excel file named `Excel_file_1.xlsx` with the following content:

| User   | Column1 | Column2 |
|--------|---------|---------|
| Wendel | inform. | inform. |
| Wendel | inform. | inform. |
| Barata | inform. | inform. |
| Barata | inform. | inform. |
| Sofia  | inform. | inform. |

If you select "User" as the column to split by, Excel Classifier will:
1. Create a new folder named `Excel_file_1`.
2. Generate three separate files within that folder:
   - `Excel_file_1_Wendel.xlsx`
  
     | User   | Column1 | Column2 |
     |--------|---------|---------|
     | Wendel | inform. | inform. |
     | Wendel | inform. | inform. |
   - `Excel_file_1_Barata.xlsx`

     | User   | Column1 | Column2 |
     |--------|---------|---------|
     | Barata | inform. | inform. |
     | Barata | inform. | inform. |
   - `Excel_file_1_Sofia.xlsx`

     | User   | Column1 | Column2 |
     |--------|---------|---------|
     | Sofia  | inform. | inform. |

## Getting Started
To use Excel Classifier effectively, follow these guidelines:

1. **Prepare Your Excel File**:
   - Use the template provided in this repository as a model for consistency.
   - Ensure the data is on a single sheet, starting from cell A1.
   - Any number of columns is supported.

2. **Choose the Output Folder**:
   - The application will store each processed file in a subfolder within your specified output folder.

3. **Select the Splitting Column**:
   - Define the column name you want to use to separate data.
   - Each unique value in this column will generate a new file.

## Requirements
- Just install the application.
