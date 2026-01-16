# Pandas Feature Engineering for Customer Churn Prediction

## 📌 Project Overview
This project demonstrates how raw customer churn data can be cleaned, transformed, and prepared for machine learning using **Pandas**.

The focus is on **feature engineering**, which is a critical step before building any ML model.

---

## 📂 Dataset
- Source: Kaggle (Customer Churn Dataset)
- Rows: ~440,000
- Target Variable: `churn` (0 = No, 1 = Yes)

---

## ⚙️ Steps Performed
1. Loaded raw churn dataset
2. Cleaned column names
3. Handled missing values
4. Converted categorical data into numerical format
5. Created meaningful features such as:
   - Average spend per tenure
   - Support calls per tenure
   - Engagement score
6. Removed outliers using IQR method
7. Performed correlation analysis
8. Saved ML-ready processed dataset

---

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy

---

## 🎯 Outcome
The final output is a **clean, ML-ready dataset** that can be directly
used to train classification models such as Logistic Regression,
Random Forest, or XGBoost.

---

## 📌 Key Learning
- Real-world data cleaning
- Feature engineering for ML
- Professional data science workflow


## 📁 Project Structure
pandas_feature_engineering_ml/
├── data/
      |-processed_data.csv
      |-raw_data.csv
├── notebooks/
      |-feature_engineering.ipynb
├── src/
      |-feature_engineering.py
├── requirements.txt
└── README.md
