#%%
# Import necessary libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.impute import SimpleImputer

# Load your merged dataset
data = pd.read_excel('Full_DATA_NEW.xlsx')

# Filter the data where analytic_set = 1
data = data[data['analytic_set'] == 1]

# Label encode categorical variables
data['Gender'] = data['Gender'].astype('category').cat.codes
data['URM'] = data['URM'].astype('category').cat.codes
data['FIS_Nationality'] = data['FIS_Nationality'].astype('category').cat.codes

# Create a list of outcome variables
outcome_variables = [
    '# of Pubs from end of postdoc to 3-year check-in',
    'H-Index ever up to 3 year check-in',
    'Cat. Normal Citation Impact ever up to 3-year check-in',
    '# of 1st Author Pubs from end of postdoc to 3-year check-in',
    '% of 1st Author Pubs from end of postdoc to 3-year check-in',
    '# of last Author Pubs from end of postdoc to 3-year check-in',
    '% of last author pubs from end of postdoc to 3-year check-in',
    '# of corresponding author pubs from end of postdoc to 3-year check-in',
    '% of corresponding author pubs from end of postdoc to 3-year check-in',
    'Mean Relative Citation Ratio ever up to 3-year check-in',
    'Weighted Relative Citation Ratio ever up to 3-year check-in',
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in',
    'Network Size ever up to 3-year check-in',
]

# Define the constant baseline covariates
baseline_covariates = [
    '# of Pubs ever to end of postdoc',
    'H-Index ever to end of postdoc',
    'Cat. Normal Citation Impact ever to End of Postdoc',
    '# of 1st Author Pubs ever to end of postdoc',
    '% of 1st Author Pubs ever to end of postdoc',
    '# of last Author Pubs ever to end of postdoc',
    '% of last author pubs ever to end of postdoc',
    '# of corresponding author pubs ever to end of postdoc',
    '% of corresponding author pubs ever to end of postdoc',
    'Mean Relative Citation Ratio ever to end of postdoc',
    'Weighted Relative Citation Ratio ever to end of postdoc',
    '# of Pubs without Postdoc Mentor during the postdoc',
    'Network Size ever to end of postdoc'
]

# Define the columns with NaN values
columns_with_nan = [
    '# of Pubs ever to end of postdoc', 'H-Index ever to end of postdoc', 
    'Cat. Normal Citation Impact ever to End of Postdoc', 
    '# of 1st Author Pubs ever to end of postdoc', '% of 1st Author Pubs ever to end of postdoc', 
    '# of last Author Pubs ever to end of postdoc', '% of last author pubs ever to end of postdoc', 
    '# of corresponding author pubs ever to end of postdoc', 
    '% of corresponding author pubs ever to end of postdoc', 
    'Mean Relative Citation Ratio ever to end of postdoc', 
    'Weighted Relative Citation Ratio ever to end of postdoc', 
    '# of Pubs without Postdoc Mentor during the postdoc', 
    'Network Size ever to end of postdoc', 
    '# of grants ever to end of postdoc', 
    'Amount of grant funding ever to end of postdoc', 
    '# of Pubs from end of postdoc to 3-year check-in', 
    'H-Index ever up to 3 year check-in', 
    'Cat. Normal Citation Impact ever up to 3-year check-in', 
    '# of 1st Author Pubs from end of postdoc to 3-year check-in', 
    '% of 1st Author Pubs from end of postdoc to 3-year check-in', 
    '# of last Author Pubs from end of postdoc to 3-year check-in', 
    '% of last author pubs from end of postdoc to 3-year check-in', 
    '# of corresponding author pubs from end of postdoc to 3-year check-in', 
    '% of corresponding author pubs from end of postdoc to 3-year check-in', 
    'Mean Relative Citation Ratio ever up to 3-year check-in', 
    'Weighted Relative Citation Ratio ever up to 3-year check-in', 
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in', 
    'Network Size ever up to 3-year check-in', 
    '# of grants from end of postdoc to 3-year check-in', 
    'Amount of grant funding from end of postdoc to 3-year check-in', 
    'Months_Worked_in_appointment'
]

# Convert specific columns to numeric
numeric_columns = [
    '# of Pubs from end of postdoc to 3-year check-in',
    'H-Index ever up to 3 year check-in',
    'Cat. Normal Citation Impact ever up to 3-year check-in',
    '# of 1st Author Pubs from end of postdoc to 3-year check-in',
    '% of 1st Author Pubs from end of postdoc to 3-year check-in',
    '# of last Author Pubs from end of postdoc to 3-year check-in',
    '% of last author pubs from end of postdoc to 3-year check-in',
    '# of corresponding author pubs from end of postdoc to 3-year check-in',
    '% of corresponding author pubs from end of postdoc to 3-year check-in',
    'Mean Relative Citation Ratio ever up to 3-year check-in',
    'Weighted Relative Citation Ratio ever up to 3-year check-in',
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in',
    'Network Size ever up to 3-year check-in',     
    '# of Pubs ever to end of postdoc',
    'H-Index ever to end of postdoc',
    'Cat. Normal Citation Impact ever to End of Postdoc',
    '# of 1st Author Pubs ever to end of postdoc',
    '% of 1st Author Pubs ever to end of postdoc',
    '# of last Author Pubs ever to end of postdoc',
    '% of last author pubs ever to end of postdoc',
    '# of corresponding author pubs ever to end of postdoc',
    '% of corresponding author pubs ever to end of postdoc',
    'Mean Relative Citation Ratio ever to end of postdoc',
    'Weighted Relative Citation Ratio ever to end of postdoc',
    '# of Pubs without Postdoc Mentor during the postdoc',
    'Network Size ever to end of postdoc',
    'Years of Postdoc'  # Add the problematic column here
]

# Check for NaN values in each column
nan_columns = data.columns[data.isna().any()].tolist()

# Print the columns with NaN values
print("Columns with NaN values:")
print(nan_columns)

# Apply single hot deck imputation
imputer = SimpleImputer(strategy='most_frequent')
data[columns_with_nan] = imputer.fit_transform(data[columns_with_nan])

# Exclude non-numeric columns from imputation
numeric_columns = data[numeric_columns].select_dtypes(include=[np.number]).columns

# Convert specific numeric columns to numeric
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Fill NaN values with the median of each numeric column
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

# Check again for NaN values after final imputation
nan_columns_final = data.columns[data.isna().any()].tolist()
print("\nColumns with NaN values after final imputation:")
print(nan_columns_final)

# Handle missing values by removing rows with missing values
data.dropna(subset=['# of Pubs from end of postdoc to 3-year check-in',
                    '# of Pubs ever to end of postdoc',
                    'Gender',
                    'FIS_Nationality',
                    'URM'], inplace=True)

# Convert all columns to numeric to handle potential string values
data = data.apply(pd.to_numeric, errors='coerce')

# Impute missing values with column means
data.fillna(data.mean(), inplace=True)

# Impute missing values with column means
data.fillna(data.mean(), inplace=True)

# Create an empty list to store model results
model_results_list = []

# Create a list of models and their respective covariates
models = [
    {
        'name': 'Model 1',
        'additional_covariates': ['Pitt_Exit']
    },
    {
        'name': 'Model 2',
        'additional_covariates': ['Pitt_Exit', 'Gender', 'URM']
    },
    {
        'name': 'Model 3',
        'additional_covariates': ['Pitt_Exit', 'Gender', 'URM', 'FIS_Nationality', 'Months_Worked_in_appointment']
    }
]

# Loop through models
for model_info in models:
    model_name = model_info['name']
    additional_covariates = model_info['additional_covariates']

    # Loop through outcome variables
    for outcome_var in outcome_variables:
        # Combine baseline and additional covariates for the current model
        covariates = baseline_covariates + additional_covariates

        # Fit the linear regression model
        X = data[covariates]
        y = data[outcome_var]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()

        # Extract and format coefficients, confidence intervals, and p-values
        coef = model.params[covariates[0]]  # Coefficient for the primary predictor
        ci = model.conf_int().loc[covariates[0]].tolist()  # 95% confidence interval
        p_value = model.pvalues[covariates[0]]  # P-value

        # Append results to the model_results_list
        model_results_list.append({
            'Model': model_name,
            'Outcome': outcome_var,
            'Coefficient': coef,
            '95% Confidence Interval': ci,
            'P-value': p_value
        })

# Convert the list to a DataFrame
model_results = pd.DataFrame(model_results_list)

# Create an Excel writer for the results
with pd.ExcelWriter('Main_Results.xlsx') as writer:
    # Loop through models
    for model_info in models:
        model_name = model_info['name']
        additional_covariates = model_info['additional_covariates']

        # Create a DataFrame to store model results
        model_results_list = []

        # Loop through outcome variables
        for outcome_var in outcome_variables:
            # Combine baseline and additional covariates for the current model
            covariates = baseline_covariates + additional_covariates

            # Fit the linear regression model
            X = data[covariates]
            y = data[outcome_var]
            X = sm.add_constant(X)
            model = sm.OLS(y, X).fit()

            # Extract and format coefficients, confidence intervals, and p-values
            coef = model.params[covariates[0]]  # Coefficient for the primary predictor
            ci = model.conf_int().loc[covariates[0]].tolist()  # 95% confidence interval
            p_value = model.pvalues[covariates[0]]  # P-value

            # Append results to the model_results_list
            model_results_list.append({
                'Outcome': outcome_var,
                'Coefficient': coef,
                '95% Confidence Interval': ci,
                'P-value': p_value
            })

        # Convert the list to a DataFrame for the current model
        model_results = pd.DataFrame(model_results_list)

        # Save the model results to a separate sheet in the Excel file
        model_results.to_excel(writer, sheet_name=model_name, index=False)

        # Print results for the current model (optional)
        print(f"Model: {model_name}")
        print(model_results)
        print("\n")

print("Results saved to 'Main_Results.xlsx'")


