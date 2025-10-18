# 📊 Customer Churn Data Analysis

This project analyzes customer churn data to identify key factors influencing why customers leave a telecom service.  
The analysis includes data cleaning, visualization, and a basic logistic regression model to interpret feature importance.

---

## 🚀 Features
- Cleaned and preprocessed raw dataset
- Visualized churn distribution and patterns across demographics
- Explored correlations among key numeric features
- Built a logistic regression model to determine feature importance

---

## Output

(7043, 21)
<class 'pandas.core.frame.DataFrame'>
Index: 7032 entries, 0 to 7042
Data columns (total 21 columns):
    Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   customerID        7032 non-null   object 
 1   gender            7032 non-null   object 
 2   SeniorCitizen     7032 non-null   int64  
 3   Partner           7032 non-null   object 
 4   Dependents        7032 non-null   object 
 5   tenure            7032 non-null   int64  
 6   PhoneService      7032 non-null   object 
 7   MultipleLines     7032 non-null   object 
 8   InternetService   7032 non-null   object 
 9   OnlineSecurity    7032 non-null   object 
 10  OnlineBackup      7032 non-null   object 
 11  DeviceProtection  7032 non-null   object 
 12  TechSupport       7032 non-null   object 
 13  StreamingTV       7032 non-null   object 
 14  StreamingMovies   7032 non-null   object 
 15  Contract          7032 non-null   object 
 16  PaperlessBilling  7032 non-null   object 
 17  PaymentMethod     7032 non-null   object 
 18  MonthlyCharges    7032 non-null   float64
 19  TotalCharges      7032 non-null   float64
 20  Churn             7032 non-null   object 
dtypes: float64(2), int64(2), object(17)
memory usage: 1.2+ MB
None
       SeniorCitizen       tenure  MonthlyCharges  TotalCharges
count    7032.000000  7032.000000     7032.000000   7032.000000
mean        0.162400    32.421786       64.798208   2283.300441
std         0.368844    24.545260       30.085974   2266.771362
min         0.000000     1.000000       18.250000     18.800000
25%         0.000000     9.000000       35.587500    401.450000
50%         0.000000    29.000000       70.350000   1397.475000
75%         0.000000    55.000000       89.862500   3794.737500
max         1.000000    72.000000      118.750000   8684.800000
/tmp/ipython-input-2889277115.py:21: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

  sns.countplot(x='Churn', data=df, palette='coolwarm')
<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/e2fb9fc8-616d-4ab6-bd53-454ad709db6e" />
<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/965774af-7f2d-4966-ba8e-25d5820d7238" />
<img width="515" height="435" alt="image" src="https://github.com/user-attachments/assets/e290275a-470b-4a5b-ae01-00a852ce2176" />
<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/f75889c6-8648-4f48-be62-d520c5afa986" />
<img width="645" height="435" alt="image" src="https://github.com/user-attachments/assets/d5cbb0a5-f7c1-4569-9822-5bd51af34961" />


## 🧠 Technologies Used
- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Plotly  
- Scikit-learn  

---

## 📂 Dataset
Dataset used: `Telco Customer Churn`  
Source: [Kaggle – Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)

---

## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/<your-username>/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis
