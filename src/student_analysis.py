import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Find the main project folder automatically
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset path
file_path = PROJECT_DIR / "data sets" / "student-mat.csv"

print("Dataset path:", file_path)
print("File exists:", file_path.exists())

# Load dataset
df = pd.read_csv(file_path, sep=";")

print("FIRST FIVE ROWS")
print(df.head())

print("LAST FIVE ROWS")
print(df.tail())

print("DATASET SHAPE")
print(df.shape)

print("COLUMN NAMES")
print(df.columns.tolist())

print("DATA TYPES")
print(df.dtypes)

print("STATISTICAL SUMMARY")
print(df.describe())

print("MISSING VALUES")
print(df.isnull().sum())

print("DUPLICATE RECORDS")
print(df.duplicated().sum())

# Project folder
project_dir = Path(__file__).resolve().parent.parent

# Load original dataset
file_path = project_dir / "data sets" / "student-mat.csv"
df = pd.read_csv(file_path, sep=";")

print("Original dataset shape:", df.shape)

# Step 1: Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Step 2: Handle missing values
# Fill missing numerical values with their column median
for column in df.select_dtypes(include="number").columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with their most frequent value
for column in df.select_dtypes(include="object").columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

# Step 3: Remove duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDuplicate rows removed:", duplicates_before)

# Step 4: Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 5: Save cleaned dataset
output_path = project_dir / "data sets" / "cleaned_data.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved at:", output_path)
print("Cleaned dataset shape:", df.shape)

# ==========================================
# STEP 3: NUMPY ANALYSIS
# ==========================================

import numpy as np

# Student marks ko NumPy array mein convert karna
marks = df["G3"].to_numpy()

print("\n========== NUMPY ANALYSIS ==========")

print("Mean marks:", np.mean(marks))
print("Median marks:", np.median(marks))
print("Minimum marks:", np.min(marks))
print("Maximum marks:", np.max(marks))
print("Standard deviation:", np.std(marks))

# Students who passed (G3 >= 10)
passed = np.sum(marks >= 10)

# Students who failed (G3 < 10)
failed = np.sum(marks < 10)

print("Students passed:", passed)
print("Students failed:", failed)

# ==========================================
# STEP 4: PANDAS ANALYSIS
# ==========================================

print("\n========== PANDAS ANALYSIS ==========")

# 1. Average final grade by gender
print("\nAverage final grade by gender:")
print(df.groupby("sex")["G3"].mean().round(2))

# 2. Average final grade by study time
print("\nAverage final grade by study time:")
print(df.groupby("studytime")["G3"].mean().round(2))

# 3. Average final grade by school
print("\nAverage final grade by school:")
print(df.groupby("school")["G3"].mean().round(2))

# 4. Students with the highest absences
print("\nTop 10 students by absences:")
print(df.nlargest(10, "absences")[["absences", "G3"]])

# 5. Correlation between absences and final grade
print("\nCorrelation between absences and final grade:")
print(df["absences"].corr(df["G3"]))

# 6. Overall grade statistics
print("\nFinal grade statistics:")
print(df["G3"].describe())

# ==========================================
# STEP 5: DATA VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

# Create visualizations folder if it does not exist
visual_dir = project_dir / "visualizations"
visual_dir.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")
# Graph 1: Distribution of final grades
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="G3", bins=15, kde=True)
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(visual_dir / "01_grade_distribution.png")
plt.show()
plt.close()

# Graph 2: Average grade by gender
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="sex", y="G3", errorbar=None)
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Final Grade")
plt.tight_layout()
plt.savefig(visual_dir / "02_grade_by_gender.png")
plt.show()
plt.close()

# Graph 3: Study time vs final grade
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="studytime", y="G3")
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time Category")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig(visual_dir / "03_studytime_vs_grade.png")
plt.show()
plt.close()

# Graph 4: Absences vs final grade
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="absences", y="G3")
plt.title("Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig(visual_dir / "04_absences_vs_grade.png")
plt.show()
plt.close()

# Graph 5: Correlation heatmap
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(12, 8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap of Student Data")
plt.tight_layout()
plt.savefig(visual_dir / "05_correlation_heatmap.png")
plt.show()
plt.close()

print("\n========== VISUALIZATION COMPLETE ==========")
print("All five graphs saved in:", visual_dir)   
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
class StudentAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, sep=";")

    def show_data(self):
        print("First five rows:")
        print(self.df.head())

        print("\nDataset shape:")
        print(self.df.shape)

    def calculate_average(self, column):
        return self.df[column].mean()

    def show_statistics(self, column):
        print("Mean:", self.df[column].mean())
        print("Median:", self.df[column].median())
        print("Standard deviation:", self.df[column].std())
        
class StudentVisualizer:

    def __init__(self, dataframe):
        self.df = dataframe

    def plot_histogram(self, column):
        plt.figure(figsize=(8, 5))
        sns.histplot(data=self.df, x=column, kde=True)

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Number of Students")

        plt.tight_layout()
        plt.show()
        
def answer_research_questions(df):

    print("\n" + "=" * 55)
    print("STEP 8: DATA ANALYSIS AND INSIGHTS")
    print("=" * 55)

    # Question 1: Average final grade
    print("\nQ1. What is the average final grade?")

    average_grade = df["G3"].mean()
    median_grade = df["G3"].median()

    print("Average final grade:", round(average_grade, 2))
    print("Median final grade:", round(median_grade, 2))


    # Question 2: Grade difference by gender
    print("\nQ2. Do average grades differ by gender?")

    gender_grades = df.groupby("sex")["G3"].mean()

    print(gender_grades.round(2))

    if "F" in gender_grades.index and "M" in gender_grades.index:
        difference = gender_grades["F"] - gender_grades["M"]

        print("Female minus male average:", round(difference, 2))


    # Question 3: Study time and grades
    print("\nQ3. How does study time relate to final grades?")

    study_results = df.groupby("studytime")["G3"].agg(
        ["mean", "median", "count"]
    )
    print(study_results.round(2))
    # Question 4: Absences and grades
    print("\nQ4. What is the relationship between absences and grades?")
    absence_correlation = df["absences"].corr(df["G3"])
    print(
        "Correlation between absences and G3:",
        round(absence_correlation, 3)
    )
    print("Average grade by absence level:")
    absence_groups = pd.cut(
        df["absences"],
        bins=[-1, 0, 5, 10, float("inf")],
        labels=["0 absences", "1-5", "6-10", "More than 10"]
    )
    print(df.groupby(absence_groups, observed=False)["G3"].mean().round(2))
    # Question 5: Variables correlated with final grade
    print("\nQ5. Which numerical variable is most correlated with G3?")
    correlations = (
        df.select_dtypes(include="number")
        .corr()["G3"]
        .drop("G3")
    )
    correlations = correlations.sort_values(
        key=lambda values: values.abs(),
        ascending=False
    )
    print(correlations.round(3))
    strongest_variable = correlations.index[0]
    print(
        "Strongest correlation:",
        strongest_variable,
        "=",
        round(correlations.iloc[0], 3)
    )
    print("\n========== ANALYSIS COMPLETE ==========")
if __name__ == "__main__":

    analyzer = StudentAnalyzer(
    r"C:\Users\PMLS\Desktop\student dataa analysis\data sets\student-mat.csv"
)

    analyzer.show_data()
    analyzer.show_statistics("G3")

visualizer = StudentVisualizer(analyzer.df)

visualizer.plot_histogram("G3")
answer_research_questions(analyzer.df)