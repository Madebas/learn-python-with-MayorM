    

  #~~~~~What is Pandas?~~~~~~
#Pandas is a powerful and widely-used open-source data analysis and manipulation library for Python
#It provides easy-to-use data structures and functions designed to work with structured data, such as tables or time series.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
#Installation of Pandas
#pip install pandas
#Once Pandas is installed, import it in your applications by adding the import keyword:
import pandas


import pandas as pd

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

print(df)

#This would output:
#     Name  Age
#0    Alice   25
#1      Bob   30
#2  Charlie   35

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
#    cars  passings
#0    BMW         3
#1  Volvo         7
#2   Ford         2

#Checking Pandas Version
import pandas as pd
print(pd.__version__)

#Pandas Series
#A Pandas Series is a one-dimensional labeled array capable of holding any data type 
# (integers, strings, floats, Python objects, etc.). It’s like a single column in a spreadsheet or a database table.
#It has data and labels (called the index)
It’s built on top of NumPy arrays.
# Creating a Pandas Series

a = [1, 7, 2]
myseries = pd.Series(a)

print(myseries)
# Output:
# 0    1
# 1    7
# 2    2
# dtype: int64

# Accessing elements by index
print(myseries[0])  # Output: 1

# Custom index
myseries_custom = pd.Series(a, index=["x", "y", "z"])
print(myseries_custom)
# Output:
# x    1
# y    7
# z    2
# dtype: int64


import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])

print(series)
#a    10
#b    20
#c    30
#d    40
#dtype: int64

#DataFrames
#In Pandas, a DataFrame is a two-dimensional, size-mutable, 
# and heterogeneous tabular data structure with labeled axes (rows and columns). Think of it like an Excel spreadsheet
#Rows and columns: Each column can have a different data type (e.g., integers, strings, floats).
#Labeled axes: You can label both rows (index) and columns.
#Flexible: You can filter, sort, group, merge, reshape, and perform calculations easily

import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Nairobi', 'Kisumu', 'Mombasa']
}

df = pd.DataFrame(data)

print(df)

#      Name  Age     City
#0    Alice   25   Nairobi
#1      Bob   30    Kisumu
#2  Charlie   35   Mombasa

#df.head() – View the first few rows.
#df['Age'] – Access a column.
#df.loc[0] – Access a row by label.
#df.describe() – Get summary statistics.

#Named Indexes
#Add a list of names to give each row a name:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#output 

#        calories  duration
 # day1       420        50
 # day2       380        40
 # day3       390        45

 #Load Files Into a DataFrame
 #To load files into a Pandas DataFrame, you typically use functions like pd.read_csv(), pd.read_excel(), or pd.read_json() depending on the file format.
 #
import pandas as pd

df = pd.read_csv('filename.csv')


df = pd.read_excel('filename.xlsx')

#Pandas Read JSON
df = pd.read_json('filename.json')

import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM table_name", conn)

#Read JSON
#Big data sets are often stored, or extracted as JSON.
#JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

#Pandas - Analyzing DataFrames
#Analyzing DataFrames in Pandas means exploring, summarizing, 
# and manipulating the data to gain insights or prepare it for further processing (like visualization or modeling)
#Viewing the Data
#df.head(n) – View the first n rows.
#df.tail(n) – View the last n rows.
#df.shape – Get the number of rows and columns.
#df.columns – List all column names.
#df.info() – Summary of the DataFrame (data types, non-null counts).
#df.describe() – Statistical summary for numeric columns.

#Selecting Data
#df['column_name'] – Select a single column.
#df[['col1', 'col2']] – Select multiple columns.
#df.loc[row_label] – Select by row label.
#df.iloc[row_index] – Select by row index.

# Filtering Data
[df['Age'] > 30]  # Rows where Age is greater than 30
# Sorting Data

df.sort_values(by='Age', ascending=False)

#Grouping and Aggregating

df.groupby('City')['Age'].mean()  # Average age per city

#Handling Missing Data
#df.isnull() – Detect missing values.
#df.dropna() – Remove rows with missing values.
#df.fillna(value) – Fill missing values with a specific value.

#Basic Math and Stats
#df['Age'].mean() – Mean of the Age column.
#df['Age'].sum() – Sum of the Age column.
#df['Age'].value_counts() – Frequency of each unique value.

#~~~~Pandas - Cleaning Empty Cells~~~~
#Cleaning empty cells (also called missing data or null values) 
# is a crucial step in data preprocessing using Pandas. Empty cells can cause errors or skew analysis if not handled properly.

#Why Clean Empty Cells?
#They can affect statistical calculations.
#Some machine learning models can't handle missing values.
#They may indicate data entry errors or incomplete records.

#How to Detect Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

# Check for any missing values
print(df.isnull())

# Count missing values per column
print(df.isnull().sum())


#1. Remove Rows with Empty Cells
#Use case: When rows with missing data are few and not critical.
df_cleaned = df.dropna()

#Remove Columns with Empty Cells
#Use case: When entire columns are mostly empty or irrelevant.
df_cleaned = df.dropna(axis=1)

#Fill Empty Cells with a Specific Value
#Use case: When a default value makes sense (e.g., 0 for quantity, "Unknown" for names).
df_filled = df.fillna(0)  # Replace with 0
df_filled = df.fillna('Unknown')  # Replace with a string

#Fill with Mean, Median, or Mode
#Use case: For numerical columns where statistical imputation is appropriate.
df['Age'] = df['Age'].fillna(df['Age'].mean())     # Mean
df['Age'] = df['Age'].fillna(df['Age'].median())   # Median
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])  # Mode

#Forward Fill / Backward Fill
#Use case: Time series data where previous or next values can be used to fill gaps.
df.fillna(method='ffill', inplace=True)  # Forward fill
df.fillna(method='bfill', inplace=True)  # Backward fill

# Replace Only Specific Columns
#Use case: When only certain columns need cleaning.
df['Salary'] = df['Salary'].fillna(50000)

#Conditional Filling
#Use case: Fill based on conditions or group-specific logic.
df.loc[df['Age'].isnull() & (df['Gender'] == 'Male'), 'Age'] = 30

#Check for Empty Strings (not just NaN)
#Use case: When cells are empty strings but not technically NaN.
df.replace('', pd.NA, inplace=True)
df.dropna(inplace=True)



