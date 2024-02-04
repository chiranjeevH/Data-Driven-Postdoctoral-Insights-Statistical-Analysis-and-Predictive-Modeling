#%%
# import pandas as pd

# # Load your dataset from the CSV file
# data = pd.read_csv('Full_DATA.xlsx')

# # Descriptive statistics for the entire dataset
# descriptive_stats = data.describe()

# # Percentage of missing values for each column
# missing_percent = (data.isnull().mean() * 100).round(2)

# # Categorical columns for which you want frequency tables
# categorical_columns = [
#     'Found link to CV (saved in Master)',
#     'Found link to Public Profile (saved in Master)',
#     'Y/N Found Postdoc Mentor (saved in Master)',
#     'FIS_Nationality',
#     'URM',
#     'Gender'
# ]

# # Generate frequency tables for categorical columns
# frequency_tables = {}
# for column in categorical_columns:
#     frequency_tables[column] = data[column].value_counts()

# # Save descriptive statistics to a CSV file
# descriptive_stats.to_csv('descriptive_statistics.csv')

# # Save missing percentage to a CSV file
# missing_percent.to_frame('Missing Percentage').to_csv('missing_percentage.csv')

# # Save frequency tables to separate CSV files
# for column, table in frequency_tables.items():
#     table.to_frame('Frequency').to_csv(f'{column}_frequency.csv')




#%%
import pandas as pd

# Load your dataset from the Excel file
data = pd.read_excel('Full_DATA_for_DA.xlsx')

# Calculate the missing percentage in the whole dataset
missing_percentage = (data.isna().mean() * 100).round(2)

# Initialize empty lists to store statistics
std = []
mean = []
median = []
percentile_25 = []
percentile_75 = []
iqr = []

# Iterate over columns
for column in data.columns:
    # Convert the column to numeric, ignoring non-numeric values
    numeric_data = pd.to_numeric(data[column], errors='coerce')
    
    # Check if there are any numeric values
    if not numeric_data.dropna().empty:
        std.append(numeric_data.std())
        mean.append(numeric_data.mean())
        median.append(numeric_data.median())
        percentile_25.append(numeric_data.quantile(0.25))
        percentile_75.append(numeric_data.quantile(0.75))
        iqr.append(numeric_data.quantile(0.75) - numeric_data.quantile(0.25))
    else:
        std.append(None)
        mean.append(None)
        median.append(None)
        percentile_25.append(None)
        percentile_75.append(None)
        iqr.append(None)

# Calculate the number of missing values
missing_count = data.isna().sum()

# Create a summary DataFrame
summary_df = pd.DataFrame({
    'Number of Missing': missing_count,
    'Missing %': missing_percentage,
    'Std': std,
    'Mean': mean,
    'Median': median,
    '25%': percentile_25,
    '75%': percentile_75,
    'IQR': iqr,
})

# Save the summary to a CSV file
summary_df.to_excel('Result_Data_Summary.xlsx')
print("Complete")
# %%
