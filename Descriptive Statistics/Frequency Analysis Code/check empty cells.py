#%%

import pandas as pd

def check_empty_cells(dataframe):
    # Check for empty cells in the DataFrame (excluding 'NA')
    empty_cells = dataframe.applymap(lambda x: x == '')

    # Display the count of empty cells in each column
    print("Empty Cell Count in Each Column:")
    print(empty_cells.sum())

    # Display the total count of empty cells in the DataFrame
    total_empty_cells = empty_cells.sum().sum()
    print(f"\nTotal Empty Cells in DataFrame: {total_empty_cells}")

    # Display rows with at least one empty cell
    rows_with_empty_cells = dataframe[empty_cells.any(axis=1)]
    print("\nRows with at Least One Empty Cell:")
    print(rows_with_empty_cells)

# Example usage:
# Load your dataset from the Excel file
df = pd.read_excel('Full_DATA_for_FQA.xlsx')

# Check for empty cells in the DataFrame (excluding 'NA')
check_empty_cells(df)

