import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# ----------------- Load Dataset -----------------
df = pd.read_csv("StudentsPerformance.csv")

# ----------------- Data Cleaning -----------------
# 1. Handle missing values safely
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# 2. Remove outliers using IQR (for numeric columns)
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# 3. Add a StudentID column
df.reset_index(drop=True, inplace=True)
df['StudentID'] = df.index + 1

# 4. Add a Pass/Fail column (average of scores)
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
df['pass_fail'] = np.where(df['average_score'] >= 50, 'Pass', 'Fail')

# 5. Keep original Gender column for Power BI
gender_column = df['gender']

# 6. Encode categorical variables
df_encoded = pd.get_dummies(df, drop_first=True)

# 7. Add back non-encoded gender for Power BI
df_encoded['Gender'] = gender_column

# 8. Save the cleaned dataset
df_encoded.to_csv("cleaned_StudentsPerformance.csv", index=False)
print("Cleaned dataset saved as 'cleaned_StudentsPerformance.csv'")

# ----------------- Exploratory Data Analysis -----------------
# Distribution of math scores
sns.histplot(df['math score'], kde=True)
plt.title("Distribution of Math Scores")
plt.show()

# Compare scores by gender
sns.boxplot(x='gender', y='math score', data=df)
plt.title("Math Scores by Gender")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df_encoded.corr(), annot=False, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ----------------- Machine Learning Model (Regression) -----------------
X = df_encoded.drop(['math score'], axis=1)
y = df_encoded['math score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
