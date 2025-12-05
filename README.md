# Bank Marketing Campaign Analysis and Prediction

## Overview

This project aims to predict whether a bank customer will subscribe to a term deposit based on their profile and historical data. It leverages machine learning to assist banks in optimizing their marketing strategies and making data-driven decisions.


---
---
## Features

- *Data Cleaning *: Uses Pandas and Nupmy for the data Manipulation and cleaning.
- *Explatory Data Analysis*: Perform detailed EDA to ask questions from data to idenfity trends and patterns.
- *Prediction Model*: Uses machine learning (XGBoost) to classify customer subscription likelihood.
- *Data Visualization*: Insights into trends such as conversion rates, age-group analysis, and feature importance.
- *Offline Capability*: Predicts outcomes for a single customer at a time by taking input for all features

---

## Tech Stack

- *Programming Language*: Python
- *Machine Learning Libraries*: Scikit-learn, XGBoost
- *Data Visualization*: Matplotlib, Seaborn
- *Model Serialization*: Joblib

---

## Steps to Run the Project

## 1. Clone the Repository:
      git clone https://github.com/yourusername/bank-marketing-prediction.git
      cd bank-marketing-prediction


## 2. Install Dependencies:
      pip install -r requirements.txt


## 3. Optional: Single Customer Prediction:
- Input all required features for a single customer to generate a prediction.

---

# Data Pipeline

### 1. Data Preparation
- Load and explore the dataset using Pandas.
- Perform EDA to identify distribution, trends, and correlations.
- Clean data by handling missing values and encoding categorical variables.

### 2. Feature Engineering
- Scale and normalize numerical features.
- Create interaction terms and select relevant features.

### 3. Model Training
- Train models using Scikit-learn and XGBoost.
- Evaluate models with metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

### 4. Fine-Tuning
- Perform hyperparameter optimization using Grid Search and Random Search.
- Experiment with advanced algorithms like LightGBM or Neural Networks (optional).

---

## Expected Outcomes
- **Accurate Predictions**: Identify customers likely to subscribe to term deposits.
- **Insights for Decision-Making**: Visualization of campaign performance and feature importance.


---

## Requirements
- **Python Version**: 3.8+
- **Libraries**:
  - Pandas
  - XGBoost
  - Seaborn
  - Matplotlib
- **Dataset**: Bank Marketing Dataset (from Kaggle)

---

## Visualizations
The project includes visual insights such as:
- Subscription rates by job type and age group.
- Duration analysis of successful campaigns.
- Feature importance graphs from the trained model.

---

## License

This project is licensed under the MIT License.  
Feel free to use, modify, and share this project.

---
## Acknowledgements

- **Dataset**: Bank Marketing Dataset.
- **Libraries**: Scikit-learn, XGBoost, Pandas, Matplotlib, Seaborn.
- **Tools**: Jupyter Notebook, VS Code.
For further questions or feedback, please contact sheryarlodhi789@gmail.com.


