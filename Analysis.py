import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Show first 5 rows
print(df.head())

# Basic info
print(df.info())

# Average scores
print("\nAverage Scores:")
print(df[['math score', 'reading score', 'writing score']].mean())

# Gender comparison
gender_avg = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
print("\nAverage Scores by Gender:")
print(gender_avg)

print("\nKey Insights:")

if gender_avg.loc['female', 'reading score'] > gender_avg.loc['male', 'reading score']:
    print("- Female students perform better in reading on average.")

if gender_avg.loc['female', 'writing score'] > gender_avg.loc['male', 'writing score']:
    print("- Female students perform better in writing on average.")

if gender_avg.loc['male', 'math score'] > gender_avg.loc['female', 'math score']:
    print("- Male students perform slightly better in math on average.")

    
# Plot average scores by gender
gender_avg.plot(kind='bar')
plt.title("Average Scores by Gender")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.show()

