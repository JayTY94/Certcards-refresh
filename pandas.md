1. Resampling Time-Series Data
Front:
What does resampling do in Pandas, and how do you perform downsampling?

Back:
Resampling changes the frequency of your time-series data.

Downsampling reduces the frequency (e.g., from daily to monthly).

    Example:
df.resample('M').sum()  # Downsample to monthly and sum values
2. Resampling Up-Sampling and Handling Missing Data
Front:
How do you perform upsampling and handle missing data in Pandas?

Back:
Upsampling increases the frequency (e.g., from monthly to daily).

You typically need to fill missing values, using methods like forward fill.

    Example:
df.resample('D').ffill()  # Up-sample to daily and forward fill missing values
3. Aggregation after Resampling
Front:
How can you apply multiple aggregation functions after resampling in Pandas?

Back:
You can apply functions like sum(), mean(), max(), etc., after resampling.

    Example:
df.resample('M').agg({'value': ['sum', 'mean']})
4. groupby() with Multiple Aggregations
Front:
How do you apply multiple aggregation functions (e.g., sum, mean) to different columns in a groupby operation?

Back:
Use .agg() with a dictionary to specify different aggregation functions for each column.

    Example:
df.groupby('category').agg({'value': ['sum', 'mean'], 'other_col': 'max'})
5. MultiIndex in Pandas
Front:
What is a MultiIndex, and how do you use it?

Back:
A MultiIndex allows for hierarchical indexing in rows and columns.

You can create it using set_index() with multiple columns or pd.MultiIndex.from_arrays().

    Example:
df.set_index(['category', 'sub_category'], inplace=True)
6. apply() with Lambda Functions
Front:
How do you use apply() with a lambda function to transform a DataFrame?

Back:
apply() allows you to apply a function (including a lambda) to each row or column.

    Example:
df['new_column'] = df.apply(lambda row: row['A'] * 2 if row['B'] > 10 else row['A'], axis=1)
7. pivot_table() vs pivot()
Front:
What is the difference between pivot() and pivot_table()?

Back:
pivot() reshapes data but requires unique combinations of index/columns.

pivot_table() allows for aggregation when there are duplicates and is more flexible.

Example for pivot_table():
df.pivot_table(index='category', columns='sub_category', values='value', aggfunc='sum')
8. Filtering with query()
Front:
How do you filter a DataFrame df using the query() method?

Back:
query() allows you to filter rows based on conditions written as a string.

    Example:
df.query('value > 10 and category == "A"')
9. unstack() Usage
Front:
What does the unstack() function do in Pandas?

Back:
unstack() "unpivots" a DataFrame by converting the index into columns.

    Example:
df.groupby(['category', 'sub_category']).sum().unstack()
10. Handling Missing Data with Interpolation
Front:
How can you fill missing values using interpolation in a time-series column?

Back:
Use .interpolate() to perform interpolation on missing values.

    Example:
df['value'] = df['value'].interpolate(method='linear')
11. Resampling Time-Series Data
Front:
What does resampling do in Pandas, and how do you perform downsampling?

Back:
Resampling changes the frequency of your time-series data.

Downsampling reduces the frequency (e.g., from daily to monthly).

    Example:
df.resample('M').sum()  # Downsample to monthly and sum values
12. Resampling Up-Sampling and Handling Missing Data
Front:
How do you perform upsampling and handle missing data in Pandas?

Back:
Upsampling increases the frequency (e.g., from monthly to daily).

You typically need to fill missing values, using methods like forward fill.

    Example:
df.resample('D').ffill()  # Up-sample to daily and forward fill missing values
13. Aggregation after Resampling
Front:
How can you apply multiple aggregation functions after resampling in Pandas?

Back:
You can apply functions like sum(), mean(), max(), etc., after resampling.

    Example:
df.resample('M').agg({'value': ['sum', 'mean']})
14. groupby() with Multiple Aggregations
Front:
How do you apply multiple aggregation functions (e.g., sum, mean) to different columns in a groupby operation?

Back:
Use .agg() with a dictionary to specify different aggregation functions for each column.

    Example:
df.groupby('category').agg({'value': ['sum', 'mean'], 'other_col': 'max'})
15. MultiIndex in Pandas
Front:
What is a MultiIndex, and how do you use it?

Back:
A MultiIndex allows for hierarchical indexing in rows and columns.

You can create it using set_index() with multiple columns or pd.MultiIndex.from_arrays().

    Example:
df.set_index(['category', 'sub_category'], inplace=True)
16. apply() with Lambda Functions
Front:
How do you use apply() with a lambda function to transform a DataFrame?

Back:
apply() allows you to apply a function (including a lambda) to each row or column.

    Example:
df['new_column'] = df.apply(lambda row: row['A'] * 2 if row['B'] > 10 else row['A'], axis=1)
17. pivot_table() vs pivot()
Front:
What is the difference between pivot() and pivot_table()?

Back:
pivot() reshapes data but requires unique combinations of index/columns.

pivot_table() allows for aggregation when there are duplicates and is more flexible.

Example for pivot_table():
df.pivot_table(index='category', columns='sub_category', values='value', aggfunc='sum')
18. Filtering with query()
Front:
How do you filter a DataFrame df using the query() method?

Back:
query() allows you to filter rows based on conditions written as a string.

    Example:
df.query('value > 10 and category == "A"')
19. unstack() Usage
Front:
What does the unstack() function do in Pandas?

Back:
unstack() "unpivots" a DataFrame by converting the index into columns.

    Example:
df.groupby(['category', 'sub_category']).sum().unstack()
20. Handling Missing Data with Interpolation
Front:
How can you fill missing values using interpolation in a time-series column?

Back:
Use .interpolate() to perform interpolation on missing values.

    Example:
df['value'] = df['value'].interpolate(method='linear')