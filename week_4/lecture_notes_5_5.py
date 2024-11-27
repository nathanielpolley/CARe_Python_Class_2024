'''
Working with Pandas Dataframes for Spreadsheet Analysis
'''

import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'San Francisco', 'London', 'Paris'],
    'Salary': [50000, 75000, 80000, 65000]
})

# Save the DataFrame to a CSV file
df.to_csv('example.csv', index=False)

# Read the CSV file
df_read = pd.read_csv('example.csv')
print(df_read)

# Creating a DataFrame with Specified Data Types
df = pd.DataFrame({
    'A': [1, 2, 3,4,5],
    'B': pd.Timestamp('20230101'),
    'C': pd.Series(1, index=list(range(5)), dtype='float32'),
    'D': np.array([3] * 5, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test","train","test"])
})

print(df)

# Viewing partial data
print(df.head())
print(df.tail(2))

# Generate a larger dataset
np.random.seed(0)
n_rows = 100000

df_large = pd.DataFrame({
    'ID': range(1, n_rows + 1),
    'Name': [f'Person_{i}' for i in range(1, n_rows + 1)],
    'Age': np.random.randint(18, 80, n_rows),
    'Salary': np.random.randint(20000, 200000, n_rows),
    'Department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing', 'Finance'], n_rows),
    'Years_of_Experience': np.random.randint(0, 40, n_rows)
})

# Save the large DataFrame to a CSV file
df_large.to_csv('large_file.csv', index=False)

# Read the large CSV file in chunks
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    print(f"Processing chunk of size {len(chunk)}")
    # Process each chunk here
    # For example, you can perform some calculations or transformations
    print(chunk.head())
    print("\n")

#Data cleaning and preprocessing
# Handling missing data
df.dropna()  # Drop rows with missing values
df.fillna(value=5)  # Fill missing values with 5

# Removing duplicates
df.drop_duplicates()

# Data type conversion
df['column_name'] = df['column_name'].astype('int64')

#Merging and Joining Data
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Sales', 'Marketing']
})

# DataFrame df2
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Name': ['Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [70000, 80000, 90000, 60000]
})

print("DataFrame df1:")
print(df1)
print("\nDataFrame df2:")
print(df2)

#Concatenation
df = pd.concat([df1, df2])
print("\nConcatenation result:")
print(df)

#Merging (by "ID" column)
merged_df = pd.merge(df1, df2, on='ID')
print("\nMerging result:")
print(merged_df)

#Joining (left-join)
joined_df = df1.set_index('ID').join(df2.set_index('ID'), lsuffix='_df1', rsuffix='_df2')
print("\nJoining result:")
print(joined_df)

#Data manipulation
df = pd.DataFrame({
    'column_name': [1, 3, 5, 7, 9, 11],
    'category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [10, 20, 30, 40, 50, 60]
})

print("Input DataFrame:")
print(df)
#Filtering
filtered_df = df[df['column_name'] > 5]
print("\nFiltered DataFrame (column_name > 5):")
print(filtered_df)

#Sorting
sorted_df = df.sort_values('column_name')
print("\nSorted DataFrame (by column_name):")
print(sorted_df)

#Grouping and Aggregation
grouped = df.groupby('category').agg({'value': 'mean'})
print("\nGrouped DataFrame (mean value by category):")
print(grouped)

#Describe
df = pd.DataFrame({
    'column_name': [1, 3, 5, 7, 9, 11],
    'category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [10, 20, 30, 40, 50, 60]
})

print("Input DataFrame:")
print(df)

#Applying functions
df['new_column'] = df['column_name'].apply(lambda x: x * 2)
print(df)

#Timeseries
ts = pd.date_range('2023-01-01', periods=100, freq='D')
ts_df = pd.DataFrame({'date': ts, 'value': np.random.randn(len(ts))})
print(ts_df.head())

#Graphing and Plotting
# Creating a sample DataFrame with random data
df = pd.DataFrame({
    'column1': [52, 93, 15, 72, 61, 21, 83, 87, 75, 75],
    'column2': [88, 24, 3, 22, 53, 2, 88, 30, 38, 2],
    'category': ['A', 'A', 'B', 'B', 'A', 'A', 'A', 'C', 'C', 'C'],
    'value': [51, 69, 89, 24, 71, 71, 56, 71, 60, 64]
})

print(df)

plt.figure(figsize=(10, 8))

# Basic Plot
plt.subplot(2, 2, 1)
df.plot(title='Basic Plot', ax=plt.gca())

# Bar Plot
plt.subplot(2, 2, 2)
df.plot.bar(title='Bar Plot', x='category', y='value', ax=plt.gca())

# Histogram
plt.subplot(2, 2, 3)
df['value'].plot.hist(title='Histogram', ax=plt.gca(), bins=5)

# Scatter Plot
plt.subplot(2, 2, 4)
df.plot.scatter(x='column1', y='column2', title='Scatter Plot', ax=plt.gca())

plt.tight_layout()
plt.show()






