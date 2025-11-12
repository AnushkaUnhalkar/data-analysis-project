# My first data analysis project
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Display first 5 rows
print("📊 First 5 rows of the dataset:")
print(data.head())

# Display basic information
print("\n📋 Dataset Information:")
print(data.info())

# Display summary statistics
print("\n📈 Summary Statistics:")
print(data.describe())

# Plot a simple graph (example: first two numeric columns)
numeric_cols = data.select_dtypes(include=['number']).columns

if len(numeric_cols) >= 2:
    plt.figure(figsize=(8, 5))
    plt.scatter(data[numeric_cols[0]], data[numeric_cols[1]], color='blue')
    plt.title(f"{numeric_cols[0]} vs {numeric_cols[1]}")
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.show()
else:
    print("\nNot enough numeric columns to plot a scatter chart.")
