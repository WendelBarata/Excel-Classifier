from pathlib import Path
from PySide6.QtCore import Signal
import pandas as pd


def split_excel_by_column(input_folder: Path, output_folder: Path,
                          column: str,
                          sender: Signal = None):
    '''
    Function to split excel files by a column and save them in separate
    folders.

    Parameters:
        input_folder (Path): The folder containing the excel files.
        output_folder (Path): The folder to save the split excel files.
        column (str): The column to split the excel files by.
        sender (Signal): The signal to emit messages to the UI.

    Returns:
        bool: True if the excel files were split successfully, False otherwise.
    '''
    try:
        # Read the excel files
        for file in input_folder.glob('*.xlsx'):
            # # Create a folder in the output folder with the same name as
            # # the input excel file

            # New folder for each excel file
            folder_each_excel = output_folder / file.stem
            # Create the folder if it does not exist
            folder_each_excel.mkdir(exist_ok=True)

            # Read all sheets in the Excel file
            sheets = pd.read_excel(file, sheet_name=None)

            # Get unique values for the specified column across all sheets
            unique_values = set()
            for df in sheets.values():
                unique_values.update(df[column].unique())

            # Create a new Excel file for each unique value
            for value in unique_values:
                new_file = folder_each_excel / f'{file.stem}_{value}.xlsx'
                with pd.ExcelWriter(new_file, engine='openpyxl') as writer:
                    for sheet_name, df in sheets.items():
                        # Filter the DataFrame by the current unique value
                        group = df[df[column] == value]
                        # Write the filtered DataFrame to the new Excel file
                        group.to_excel(writer, index=False,
                                       sheet_name=sheet_name)

        # Emit a signal informing the user that the excel files have been split
        if sender is not None:
            sender.emit('Excel files have been split successfully')
            return True

    except FileNotFoundError:
        if sender is not None:
            sender.emit('Error: Input folder or specified file not found. '
                        'Please check the path and try again.')
        return False
    except PermissionError:
        if sender is not None:
            sender.emit('Error: Permission denied. Check access rights '
                        'for the files or output folder.')
        return False
    except KeyError:
        if sender is not None:
            sender.emit(f'Error: Column "{column}" not found in one of '
                        'the files. Please check the column name.')
        return False
    except pd.errors.EmptyDataError:
        if sender is not None:
            sender.emit('Error: One of the files is empty and cannot be '
                        'processed.')
        return False
    except pd.errors.ParserError:
        if sender is not None:
            sender.emit('Error: Failed to parse one of the Excel files. '
                        'Check if files are corrupted or in a different '
                        'format.')
        return False
    except OSError as e:
        if sender is not None:
            sender.emit(f'Error: OS-related error occurred: {str(e)}')
        return False
    except Exception as e:
        if sender is not None:
            sender.emit(f'Error: An unexpected error occurred: {str(e)}')
        return False


def common_columns(input_folder: Path, sender: Signal = None) -> list:
    '''
    Method that retrieves all the titles in the column and returns a list of
    only the titles present in all the files.

    Parameters:
        input_folder (Path): The folder containing the excel files.

    Returns:
        list: A list of the common titles in the column.
    '''
    try:
        # Get the excel files
        excel_files = list(input_folder.glob('*.xlsx'))

        # Initialize common_columns as None
        common_columns = None

        for file in excel_files:
            # Read all sheets in the Excel file
            sheets = pd.read_excel(file, sheet_name=None)

            # Collect columns from all sheets
            file_columns = set()
            for df in sheets.values():
                file_columns.update(df.columns)

            # Determine the common columns
            if common_columns is None:
                common_columns = file_columns
            else:
                common_columns.intersection_update(file_columns)

            # If no common columns are found, return an empty list
            if not common_columns:
                return []

        return list(common_columns) if common_columns else []

    except FileNotFoundError:
        if sender is not None:
            sender.emit('Error: Input folder or specified file not found. '
                        'Please check the path and try again.')
        return []
    except PermissionError:
        if sender is not None:
            sender.emit('Error: Permission denied. Check access rights '
                        'for the files or output folder.')
        return []
    except KeyError:
        if sender is not None:
            sender.emit('Error: Column not found in one of the files. '
                        'Please check the column name.')
        return []
    except pd.errors.EmptyDataError:
        if sender is not None:
            sender.emit('Error: One of the files is empty and cannot be '
                        'processed.')
        return []
    except pd.errors.ParserError:
        if sender is not None:
            sender.emit('Error: Failed to parse one of the Excel files. '
                        'Check if files are corrupted or in a different '
                        'format.')
        return []
    except OSError as e:
        if sender is not None:
            sender.emit(f'Error: OS-related error occurred: {str(e)}')
        return []
    except Exception as e:
        if sender is not None:
            sender.emit(f'Error: An unexpected error occurred: {str(e)}')
        return []


if __name__ == '__main__':
    input_folder = Path('Test/Excel_input')
    output_folder = Path('Test/Excel_output')
    column = 'Coluna1'
    split_excel_by_column(input_folder, output_folder, column)

    # print(common_columns(Path('Test/Excel_input')))
