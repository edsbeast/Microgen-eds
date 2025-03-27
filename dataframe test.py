import pandas as pd

# Example data frames with different indexes
df1 = pd.DataFrame({'Values': [1.0, 2.0, 3.0, 4.0, 5.0]}, index=range(0, 5))
df2 = pd.DataFrame({'Values': [2.0, 3.0, 4.0, 5.0, 6.0]}, index=range(5, 10))
df3 = pd.DataFrame({'Values': [3.0, 4.0, 5.0, 6.0, 7.0]}, index=range(10, 15))

# Reset indexes and concatenate the data frames
concatenated_df = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True), df3.reset_index(drop=True)], axis=1)

# Calculate the average of the concatenated data frame
average_df = concatenated_df.mean(axis=1)

print(average_df)