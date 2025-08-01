________________________________________
Student Performance Analysis & Prediction
Project Overview
This project analyzes student performance using the StudentsPerformance dataset and applies data cleaning, exploratory data analysis (EDA), and machine learning to derive insights.
It also includes a Power BI dashboard to present interactive visualizations for better understanding.
Sector: Education
Problem Statement:
Can we analyze and predict student performance based on socio-economic and academic factors?
________________________________________
Dataset
•	Source: Provided as part of the project (StudentsPerformance.csv)
•	Rows: 1000+
•	Columns:
o	Gender
o	Race/Ethnicity
o	Parental Level of Education
o	Lunch Type
o	Test Preparation Course
o	Math, Reading, and Writing Scores
Additional Features Created:
•	Average Score (mean of math, reading, and writing scores)
•	Pass/Fail classification (based on average score ≥ 50)
•	StudentID (unique identifier for each record)
________________________________________
Project Workflow
1. Data Cleaning (Python)
•	Handled missing values (categorical → mode, numerical → median)
•	Removed outliers using IQR method
•	Encoded categorical variables for modeling
•	Added Pass/Fail and StudentID columns
2. Exploratory Data Analysis
•	Visualized score distributions
•	Compared performance by gender and parental education
•	Correlation analysis between subjects
3. Machine Learning
•	Applied Random Forest Regressor to predict math scores
•	Evaluated using Root Mean Squared Error (RMSE)
________________________________________

Correlation Heat map
This is a correlation heatmap of your dataset, showing how strongly different variables are related to each other:
•	Dark red areas (close to 1.0) → Strong positive correlation (as one increases, the other also increases).
•	Dark blue areas (close to -1.0) → Strong negative correlation (as one increases, the other decreases).
•	Light areas (near 0) → Little to no correlation.
Key Observations:
1.	Math, Reading, Writing, and Average Score
o	These are highly correlated (dark red) → makes sense since average is derived from these scores.
2.	Pass/Fail vs Scores
o	Positive correlation with all scores (students with higher scores are more likely to pass).
3.	Lunch Type & Test Prep
o	Slight correlation with performance → students with standard lunch and completed test prep tend to perform a bit better.
4.	Parental Education
o	Mild positive correlation with scores → higher education levels are linked to better performance.
5.	Gender & Ethnicity
o	Low correlation with scores (light colors) → indicates gender and ethnicity don’t strongly affect the scores in this dataset.
This heatmap helps quickly see which variables are most relevant when predicting student performance.


 


     
Distribution of Math Scores
The distribution of math scores shows how students performed in mathematics:
•	Shape: The scores are roughly bell-shaped, meaning most students cluster around the middle range.
•	Center: The majority of students scored between 60–80.
•	Spread: A few students scored very low or very high, but extreme outliers are rare.
•	Insight: Performance in math is fairly balanced, with no strong skew toward very low or very high scores.

 

      Math  Scores by Gender
This boxplot of math scores by gender shows:
•	Median: Males have a slightly higher median math score than females.
•	Spread: Both genders have a similar range of scores, though males show slightly more variation.
•	Outliers: A few outliers exist for males at the lower end (very low scores).
•	Insight: While both genders perform similarly overall, males tend to score slightly higher in math on average.

 






________________________________________
Power BI Dashboard
The Power BI dashboard presents:
•	Key KPIs: Average Math, Reading, and Writing scores
•	Donut Chart: Pass vs Fail rate
•	Clustered Bar Chart: Average scores by gender
•	Column Chart: Average score by parental education level
•	Scatter Plot: Correlation between reading & writing scores
•	Slicers: Gender, Parental Education, Test Preparation


 ________________________________________
Files in This Repository
•	/data/
o	StudentsPerformance.csv – Original dataset
o	cleaned_StudentsPerformance.csv – Processed dataset for analysis & Power BI
•	/code/
o	python.py – Python script for cleaning, EDA, and ML
•	/dashboard/
o	Student_Performance.pbix – Power BI dashboard
•	README.md – Project documentation
________________________________________
How to Run
1.	Clone this repository:
2.	git clone https://github.com/Manzii13/Student-Performance-Analysis
3.	Install dependencies:
4.	pip install pandas numpy matplotlib seaborn scikit-learn
5.	Run the Python script:
6.	python code/python.py
7.	Open Student_Performance.pbix in Power BI Desktop to view the dashboard.
________________________________________
Key Insights
•	Students who completed test preparation scored higher across all subjects.
•	Parental education level positively correlates with student performance.
•	Gender differences are small but noticeable in certain subjects.
________________________________________
Future Work
•	Build a classification model to predict Pass/Fail with high accuracy.
•	Integrate additional socio-economic datasets for deeper insights.
________________________________________
Author
Your Name: Manzi Arsene
Link:https://github.com/Manzii13/Student-Performance-Analysis
Faculty of Information Technology – AUCA
Final Exam – Capstone Project (INSY 8413: Introduction to Big Data Analytics)
________________________________________

