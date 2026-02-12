import pandas as pd
import matplotlib.pyplot as plt

# create student marks dataset
data = {
    'Subject' : ['Maths', 'Science', 'English', 'ICT', 'History'],
    'Marks' : [85, 78, 90, 88, 75]

}

df = pd.DataFrame(data)

# display data
print("Student Marks Data:")
print(df)

# calculate statistics
mean_marks = df['Marks'].mean()
median_marks = df['Marks'].median()

# plot bar chart
plt.bar(df['Subject'], df['Marks'])
plt.title("Student Marks Analysis")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()