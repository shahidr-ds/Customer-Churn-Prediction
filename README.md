# Customer Churn Prediction

## 📌 Project Overview
This project focuses on predicting customer churn using machine learning techniques. By analyzing customer behavior and service usage patterns, the goal is to identify at-risk customers and suggest retention strategies.

## 📊 Dataset Overview
- **Source:** Kaggle / Telco Customer Churn Dataset
- **Total Entries:** 7042
- **Total Features:** 20
- **Target Variable:** `Churn` (Yes/No)

### 🔍 Key Features:
- **Customer Demographics:** Gender, Senior Citizen, Partner, Dependents
- **Service Usage:** Internet Service, Online Security, Tech Support
- **Billing Information:** Monthly Charges, Total Charges, Payment Method
- **Contract Details:** Tenure, Contract Type, Paperless Billing

## 🛠 Data Preprocessing & Feature Engineering
1. **Handling Missing Values:**
   - `Total Charges` converted to numeric, missing values imputed with median.
2. **Encoding Categorical Variables:**
   - One-hot encoding used for categorical features.
3. **Outlier Detection:**
   - Z-score method used to identify tenure outliers.
4. **Feature Scaling:**
   - StandardScaler applied to numerical variables.

## 📈 Exploratory Data Analysis (EDA)
### Key Insights:
- **High Monthly Charges → Higher Churn Rate** 📉
- **Longer Tenure → Lower Churn Rate** 🔄
- **Electronic Check Payments Linked to Higher Churn** 💳
- **Customers with Month-to-Month Contracts More Likely to Churn** 📆

## 🏆 Model Performance
We trained multiple machine learning models and evaluated their performance:

| Model                  | Accuracy | Precision (Churn) | Recall (Churn) | F1 Score |
|------------------------|----------|------------------|---------------|----------|
| Decision Tree         | 0.776    | 0.596            | 0.489         | 0.537    |
| SVM                   | 0.798    | 0.659            | 0.492         | 0.564    |
| Random Forest         | 0.786    | 0.621            | 0.495         | 0.551    |
| Logistic Regression   | 0.792    | 0.633            | 0.516         | 0.568    |
| XGBoost               | 0.752    | 0.523            | 0.727         | 0.609    |

**Best Model:** *Logistic Regression* - Balancing accuracy, precision and recall effectively.

## 📊 Visualizations
- Churn distribution analysis
- Tenure vs. Churn trends
- Monthly Charges impact on Churn
- Kaplan-Meier Survival Analysis

## 💡 Business Recommendations

✅ Offer incentives for long-term contracts to reduce churn.

✅ Implement loyalty programs for high-paying customers.

✅ Improve customer onboarding experience for new users.

✅ Identify high-risk customers and apply retention strategies.

## 🚀 How to Use This Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/churn-prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:
   ```bash
   jupyter notebook Project1.ipynb
   ```

## 📌 Conclusion
This project provides valuable insights into customer churn behavior and demonstrates how machine learning can help businesses retain customers effectively. Future improvements could include hyperparameter tuning, deep learning models, and additional feature engineering.

📜 License

This project is open-source and available under the MIT License. Feel free to use and improve upon it!

💡 Acknowledgments

Thanks to Kaggle for the dataset.

Inspired by various open-source churn prediction projects.

---
🚀 **Author:** [Shahid Rasheed]  
📅 **Date:** 17 February 2025  
📧 **Contact:** shahidr54gb@gamil.com


