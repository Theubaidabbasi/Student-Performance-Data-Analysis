
import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "cleaned_student_data.csv")
GRAPH_DIR = os.path.join(BASE_DIR, "visualizations")
PDF_PATH = os.path.join(BASE_DIR, "project_report.pdf")

df = pd.read_csv(DATA_PATH)
styles = getSampleStyleSheet()

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)

story = []

def add_heading(text):
    story.append(Paragraph(text, styles["Heading1"]))
    story.append(Spacer(1, 10))

def add_text(text):
    story.append(Paragraph(text, styles["BodyText"]))
    story.append(Spacer(1, 8))

# Page 1: Introduction
story.append(Spacer(1, 1.2 * inch))
story.append(Paragraph(
    "STUDENT PERFORMANCE DATA ANALYSIS",
    styles["Title"]
))
story.append(Spacer(1, 25))
add_text("Python Data Science Final Project")
add_text("Dataset: Student Performance (Mathematics)")
add_text("Tools: Python, Pandas, NumPy, Matplotlib, Seaborn and OOP")
add_text("Student Name: __________________________")
add_text("Department / Institute: __________________")
story.append(PageBreak())

# Page 2: Dataset and exploration
add_heading("1. Dataset Overview")
add_text(
    "This project analyzes student performance data using Python. "
    "The dataset contains student characteristics and academic results."
)
add_text(f"Number of rows: {df.shape[0]}")
add_text(f"Number of columns: {df.shape[1]}")
add_text(
    "The target variable is G3, representing the final mathematics grade."
)
add_text(
    "Original dataset source: UCI Machine Learning Repository, "
    "Student Performance Data Set."
)
add_text(
    "Source URL: https://archive.ics.uci.edu/dataset/320/student+performance"
)
add_heading("Data Quality")
add_text(f"Missing values in cleaned dataset: {df.isnull().sum().sum()}")
add_text(f"Duplicate rows in cleaned dataset: {df.duplicated().sum()}")
add_text("The dataset was explored using head, tail, info and describe.")
story.append(PageBreak())

# Page 3: Methods and statistics
add_heading("2. Methodology and Statistical Analysis")
add_text(
    "Pandas was used to load, inspect, group and summarize the dataset. "
    "NumPy was used to calculate numerical statistics and filter grades."
)
add_text(f"Mean final grade (G3): {df['G3'].mean():.2f}")
add_text(f"Median final grade (G3): {df['G3'].median():.2f}")
add_text(f"Standard deviation: {df['G3'].std():.2f}")
add_text(f"Minimum final grade: {df['G3'].min()}")
add_text(f"Maximum final grade: {df['G3'].max()}")
add_text(
    "Two classes were implemented: StudentAnalyzer for data summaries "
    "and StudentVisualizer for plotting."
)
story.append(PageBreak())

# Page 4: Findings
add_heading("3. Research Questions and Findings")

female_mean = df.loc[df["sex"] == "F", "G3"].mean()
male_mean = df.loc[df["sex"] == "M", "G3"].mean()
study_means = df.groupby("studytime")["G3"].mean()
absence_corr = df["absences"].corr(df["G3"])
corr = df.select_dtypes(include="number").corr()["G3"].drop("G3")
strongest = corr.abs().idxmax()

add_text(
    f"Q1. What is the average final grade? The mean is {df['G3'].mean():.2f} "
    f"and the median is {df['G3'].median():.2f}."
)
add_text(
    f"Q2. Do grades differ by gender? Female mean: {female_mean:.2f}; "
    f"male mean: {male_mean:.2f}. This is a descriptive comparison."
)
add_text(
    f"Q3. How does study time relate to grades? The average G3 by study-time "
    f"category is: {study_means.round(2).to_dict()}."
)
add_text(
    f"Q4. How are absences related to grades? The correlation between "
    f"absences and G3 is {absence_corr:.3f}."
)
add_text(
    f"Q5. Which numerical variable has the strongest absolute correlation "
    f"with G3 among the other numeric columns? {strongest} "
    f"(correlation {corr[strongest]:.3f})."
)
add_text(
    "These results describe associations and do not establish causation."
)
story.append(PageBreak())

# Page 5: Visualizations
add_heading("4. Visualizations")

graph_files = [
    "01_grade_distribution.png",
    "02_grade_by_gender.png",
    "03_studytime_vs_grade.png",
    "04_absences_vs_grade.png",
    "05_correlation_heatmap.png",
]

for graph in graph_files:
    graph_path = os.path.join(GRAPH_DIR, graph)
    if os.path.exists(graph_path):
        story.append(Paragraph(graph.replace("_", " "), styles["Heading3"]))
        story.append(Spacer(1, 5))
        story.append(Image(graph_path, width=6.0 * inch, height=3.2 * inch))
        story.append(Spacer(1, 12))

# Page 6: Limitations and conclusion
story.append(PageBreak())
add_heading("5. Limitations")
add_text(
    "The analysis is based on one dataset and may not represent all students "
    "or schools. Correlation does not prove causation. Some important factors "
    "may not be included in the dataset."
)
add_heading("6. Conclusion")
add_text(
    "This project demonstrated data loading, exploration, cleaning, "
    "numerical analysis, grouping, object-oriented programming and "
    "visualization. The findings can help describe patterns in student "
    "performance, but should not be treated as proof of cause and effect."
)
add_heading("References")
add_text(
    "Cortez, P. and Silva, A. (2008). Using Data Mining to Predict "
    "Secondary School Student Performance."
)
add_text(
    "UCI Machine Learning Repository: "
    "https://archive.ics.uci.edu/dataset/320/student+performance"
)

doc.build(story)
print("PDF report created:", PDF_PATH)

