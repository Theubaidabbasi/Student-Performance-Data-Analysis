# Student Performance Data Analysis

## 1. Project Overview
This project analyzes student performance using Python data science libraries. The main objective is to explore student data, clean the dataset, calculate statistics, identify patterns, and visualize factors related to final grades.

## 2. Dataset
- **Dataset:** Student Performance (Math Course)
- **Source:** UCI Machine Learning Repository
- **Original dataset:** `student-mat.csv`
- **Source link:** https://archive.ics.uci.edu/dataset/320/student+performance
- **Rows:** 395
- **Columns:** 33

## 3. Technologies and Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- ReportLab

## 4. Project Structue
- `data sets/` — Original dataset folder
- `notebooks/` — Jupyter Notebook folder
- `notebooks/student_analysis.ipynb` — Jupyter Notebook for analysis
- `src/student_analysis.py` — Main Python analysis script
- `visualizations/` — Folder containing five saved graphs
- `cleaned_student_data.csv` — Cleaned dataset
- `make_report.py` — PDF report generation script
- `project_report.pdf` — Final PDF report
- `README.md` — Project documentation

## 5. Analysis Performed
- Displayed the first and last five rows
- Checked dataset shape, columns, data types, missing values, and duplicates
- Calculated mean, median, standard deviation, minimum, and maximum grades
- Compared grades by gender and study time
- Examined absences and final grades
- Calculated correlations between numerical variables
- Created five visualizations

## 6. Research Questions
1. What is the distribution of students' final grades?
2. How do average final grades differ by gender?
3. Is study time associated with final grades?
4. What relationship exists between absences and final grades?
5. Which numerical variables are correlated with final grades?

## 7. How to Run
1. Open the project folder in VS Code.
2. Activate the project's Python virtual environment.
3. Install the required libraries:
   `python -m pip install pandas numpy matplotlib seaborn reportlab`
4. Run the main analysis script:
   `python src/student_analysis.py`
5. Open `notebooks/student_analysis.ipynb` in VS Code to explore the notebook.
6. Run `python make_report.py` to regenerate the PDF report.
## 8. Limitations
This analysis identifies patterns and associations; it does not establish that one factor causes changes in student performance. The dataset represents a specific student population, so findings may not generalize to all schools.

## 9. Conclusion
The project demonstrates data exploration, cleaning, statistical analysis, object-oriented programming, and data visualization using Python. The findings should be interpreted in the context of the original dataset.
