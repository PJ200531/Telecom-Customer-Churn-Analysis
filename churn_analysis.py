
import pandas as pd
df = pd.read_csv("Telco-Customer-Churn.csv")
print(df.shape)
df.head()

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Basic cleaning
df = df.dropna()
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

# Basic info
print(df.info())
print(df.describe())

# Churn distribution
sns.countplot(x='Churn', data=df, palette='coolwarm')
plt.title("Customer Churn Distribution")
plt.show()

# Gender vs Churn
sns.countplot(x='gender', hue='Churn', data=df, palette='viridis')
plt.title("Churn by Gender")
plt.show()

# Correlation heatmap
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Key Numeric Features")
plt.show()

# Monthly Charges vs Tenure
px.scatter(df, x='tenure', y='MonthlyCharges', color='Churn',
           title='Monthly Charges vs Tenure (Churn Highlighted)')

# Contract type vs Churn
sns.countplot(x='Contract', hue='Churn', data=df, palette='magma')
plt.title("Churn Rate by Contract Type")
plt.show()

# Internet Service vs Churn
sns.countplot(x='InternetService', hue='Churn', data=df, palette='cubehelix')
plt.title("Churn by Internet Service Type")
plt.show()

# Feature importance (basic logistic regression)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Encode categorical
df_encoded = df.copy()
for col in df_encoded.select_dtypes('object').columns:
    df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)
importance = pd.Series(model.coef_[0], index=X.columns).sort_values(ascending=False)

# Top 10 features
importance.head(10).plot(kind='barh', color='teal')
plt.title("Top Features Influencing Customer Churn")
plt.show()
