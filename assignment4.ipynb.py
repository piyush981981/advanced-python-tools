#Assignment 1 - NumPy (numpy_assignment.ipynb)
# Step 1: Import NumPy
import numpy as np
# Create 1D array from 1 to 20
arr1 = np.arange(1, 21)

# a. Basic statistics
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))

# b. Indices where elements > 10
print("Indices of elements > 10:", np.where(arr1 > 10)[0])
arr2 = np.arange(1, 17).reshape(4, 4)

# a. Print array
print("Original array:\n", arr2)

# b. Transpose
print("Transpose:\n", arr2.T)

# c. Row-wise and column-wise sums
print("Row-wise sum:", np.sum(arr2, axis=1))
print("Column-wise sum:", np.sum(arr2, axis=0))
a = np.random.randint(1, 21, (3, 3))
b = np.random.randint(1, 21, (3, 3))

# a. Element-wise operations
print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)

# b. Dot product
print("Dot product:\n", np.dot(a, b))
arr3 = np.arange(1, 13)
reshaped = arr3.reshape(3, 4)
print("Reshaped 3x4 array:\n", reshaped)

# Slice first 2 rows, last 2 columns
print("Sliced section:\n", reshaped[:2, -2:])


#Assignment 2 - Pandas (pandas_assignment.ipynb)
# Step 1: Import pandas
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)

# a. First five rows
print(df.head())

# b. Summary stats for 'Age' and 'Salary'
print(df[['Age', 'Salary']].describe())

# c. Average salary in HR
print("Average HR Salary:", df[df['Department'] == 'HR']['Salary'].mean())
df['Bonus'] = df['Salary'] * 0.10
print(df)
filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print(filtered_df)
dept_avg = df.groupby('Department')['Salary'].mean()
print(dept_avg)
sorted_df = df.sort_values(by='Salary')
print(sorted_df)

# Save to CSV
sorted_df.to_csv('sorted_salaries.csv', index=False)


#Assignment 3 - Matplotlib (matplotlib_assignment.ipynb)
# Step 1: Import matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]

plt.bar(students, marks, color='skyblue')
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]

explode = [0.1 if r == max(revenue) else 0 for r in revenue]  # highlight highest
plt.pie(revenue, labels=regions, autopct='%1.1f%%', explode=explode, startangle=140)
plt.title("Revenue Distribution by Region")
plt.axis('equal')  # Equal aspect ratio for a perfect circle
plt.show()
import numpy as np

data = np.random.randint(1, 101, size=1000)

plt.hist(data, bins=20, color='green', edgecolor='black')
plt.title("Frequency Distribution of Random Integers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


