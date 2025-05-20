# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import zipfile

# Set Seaborn style
sns.set(style="whitegrid")

# === Task 1: Load and Explore the Dataset ===

# Step 1: Define the file path (update this path to match your file and username)
#file_path = r'C:\Users\USER\Downloads\iris.zip'  # Replace with actual path
# File path to your ZIP file
zip_path = r'C:\Users\USER\Downloads\iris.zip'

# Iris dataset column names from UCI repository
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Step 2: Load dataset with error handling
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Show files
        file_list = zip_ref.namelist()
        print(" Files in ZIP:", file_list)

        # Find and load the .data file
        if 'iris.data' in file_list:
            with zip_ref.open('iris.data') as file:
                df = pd.read_csv(file, header=None, names=column_names)
                print(" Dataset loaded successfully.\n")
        else:
            print(" 'iris.data' not found in the ZIP.")
            exit()
except Exception as e:
    print(f" An error occurred: {e}")
    exit()

# Display first few rows
print(df.head())

# Clean missing rows (some may be empty at the end)
df.dropna(inplace=True)

# Dataset info
print("\n Dataset Info:")
print(df.info())

# === Basic Statistics ===
print("\n Basic Statistics:")
print(df.describe())

# Group by species
print("\n Average Petal Length by Species:")
print(df.groupby('species')['petal_length'].mean())

# === Visualizations ===

sns.set(style="whitegrid")

# Line chart - sepal length trend
plt.figure(figsize=(10, 5))
plt.plot(df['sepal_length'])
plt.title(" Sepal Length Trend (simulated)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length")
plt.grid(True)
plt.show()

# Bar chart - avg petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='species', y='petal_length', estimator=np.mean)
plt.title(" Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length")
plt.show()

# Histogram - sepal width
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_width'], bins=20, kde=True)
plt.title(" Sepal Width Distribution")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.show()

# Scatter plot - petal length vs sepal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
plt.title(" Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend(title='Species')
plt.show()

print(" All tasks completed successfully.")