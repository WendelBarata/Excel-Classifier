from pathlib import Path
from PySide6.QtCore import Signal
import pandas as pd


def split_excel_by_column(input_folder: Path, output_folder,
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

            # Read the excel file
            df = pd.read_excel(file)

            # Split the excel file by the column
            for name, group in df.groupby(column):
                # Create a new excel file
                new_file = folder_each_excel / f'{file.stem}_{name}.xlsx'
                # Create the excel file
                with pd.ExcelWriter(new_file, engine='openpyxl') as writer:
                    group.to_excel(writer, index=False)

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


def common_columns(input_folder: Path, sender: Signal) -> list:
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

        # Get the common columns
        common_columns = []
        for file in excel_files:
            # Read the excel file
            df = pd.read_excel(file)

            # Get the column titles
            columns = df.columns

            # Get the common column titles
            if not common_columns:
                common_columns = set(columns)
            else:
                # Remove the columns that are not common
                for column in common_columns.copy():
                    if column not in columns:
                        common_columns.remove(column)
                    if not common_columns:
                        return []

        return list(common_columns)

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
    # input_folder = Path('Test/Excel_input')
    # output_folder = Path('Test/Excel_output')
    # column = 'Usuario'
    # split_excel_by_column(input_folder, output_folder, column)

    print(common_columns(Path('Test/Excel_input')))
