

# University of Pittsburgh - PostDoc Researchers Success Impact Analysis based on Diffrent Metrics

Brief description of your project.

## Table of Contents
1. [Data Preparation and Exploration](#1-data-preparation-and-exploration)
2. [Missing Data Analysis](#2-missing-data-analysis)
3. [Frequency Analysis](#3-frequency-analysis)
4. [Linear Regression Models](#4-linear-regression-models)
5. [Imputation Strategies](#5-imputation-strategies)
6. [Sensitivity Analysis](#6-sensitivity-analysis)
7. [GitHub Repository Organization](#7-github-repository-organization)

## 1. Data Preparation and Exploration

- **Code Title:** `Data_Preparation_and_Exploration.py`
- **Functionality:**
  - Load and merge datasets.
  - Handle categorical variables.
  - Filter data based on specific criteria.
  - Conduct exploratory data analysis (EDA).
  - Identify missing data patterns.

## 2. Missing Data Analysis

- **Code Title:** `descriptive_analysis.py`
- **Functionality:**
  - Perform a descriptive analysis of missing data.
  - Calculate missing data percentages.
  - Explore missing data patterns across variables.
  - Visualize missing data.

## 3. Frequency Analysis

- **Code Title:** `frequency_analysis.py`
- **Functionality:**
  - Generate frequency tables for categorical variables.
  - Include percentages and cumulative frequencies.
  - Handle missing values in frequency tables.
  - Save results to Excel.

## 4. Linear Regression Models

- **Code Title:** `Linear_Regression_Models.py`
- **Functionality:**
  - Fit linear regression models for multiple outcomes.
  - Handle categorical variables using label encoding.
  - Evaluate model coefficients, confidence intervals, and p-values.
  - Save results to Excel.

## 5. Imputation Strategies

- **Code Title:** `data_preprocessing_and_regression.py`
- **Functionality:**
  - Implement imputation strategies for missing values.
  - Use column means for simple imputation.
  - Apply multiple imputation for more complex missing data patterns.
  - Save imputed datasets.

## 6. Sensitivity Analysis

- **Code Title:** `Sensitivity_Analysis.py`
- **Functionality:**
  - Conduct sensitivity analysis on imputed data.
  - Assess robustness of results under different missing data assumptions.
  - Compare results from multiple imputation and sensitivity analysis.

## 7. GitHub Repository Organization

- **Data-Driven-Postdoctoral-Insights:** `README.md`
- **Functionality:**

## 8. Functionality:

Descriptive Analysis Code:
File: descriptive_analysis.py

- Description:
Calculates descriptive statistics and frequencies.
Generates a summary report with missing percentages, means, medians, and more.

- Instructions:
Ensure you have the dataset in the specified format.
Run the script to obtain descriptive statistics.
Review the generated summary report in 'Result_Data_Summary.xlsx'.

- Frequency Analysis Code:
File: frequency_analysis.py

- Description:
Performs frequency analysis on categorical variables.
Produces frequency tables for different groups of columns.

- Instructions:
Load the dataset required for frequency analysis.
Run the script to generate frequency tables.
Explore the results in 'Result_Frequency_tables.xlsx'.
Data Preprocessing and Linear Regression Models:
File: data_preprocessing_and_regression.py

- Description:
Handles missing data through imputation strategies.
Applies label encoding to categorical variables.
Executes linear regression models with various covariates.

- Instructions:
Load the merged dataset for postdoc data.
Run the script to preprocess and model the data.
Explore the results in 'Main_Results.xlsx'.

### How to Run:

1. **Descriptive Analysis:**
    ```bash
    python descriptive_analysis.py
    ```

2. **Frequency Analysis:**
    ```bash
    python frequency_analysis.py
    ```

3. **Data Preprocessing and Regression:**
    ```bash
    python data_preprocessing_and_regression.py
    ```

Feel free to clone the repository and explore each code file for detailed information.

