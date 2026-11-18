# Salary Prediction and Missing Data Imputation Using Machine Learning

## 1. Project Overview

This project focuses on predicting missing employee salary values using statistical and machine learning imputation techniques.

The main objective is to compare different imputation methods and identify which one provides the most accurate salary predictions.

The project uses the IBM HR Analytics Employee Attrition dataset.

## 2. Objectives

- Explore and understand the employee dataset.
- Analyze the distribution of monthly salaries.
- Create artificial missing values in the `MonthlyIncome` column.
- Apply statistical imputation methods.
- Build machine learning models to predict missing salaries.
- Evaluate and compare the performance of different methods.

## 3. Dataset Description

**Dataset:** IBM HR Analytics Employee Attrition & Performance

**Source:** [Kaggle – IBM HR Analytics](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

- Number of records: 1,470 employees
- Number of features: 35
- Target variable: `MonthlyIncome`

### Selected Features

| Feature | Description |
|---|---|
| Age | Employee age |
| TotalWorkingYears | Total professional experience |
| YearsAtCompany | Years spent at the company |
| YearsInCurrentRole | Years in the current role |
| YearsWithCurrManager | Years with current manager |
| JobLevel | Employee job level |
| JobRole | Employee job position |
| Department | Department |
| Education | Education level |
| BusinessTravel | Business travel frequency |
| MaritalStatus | Marital status |

## 4. Data Preparation

The original dataset does not contain missing values in `MonthlyIncome`.

To simulate a real-world missing data problem, 15% of salary values were randomly selected and replaced with missing values (`NaN`).

The original salary values were preserved to evaluate the quality of the imputation methods.

## 5. Imputation Methods

Four methods were implemented:

### Statistical Methods

- Mean Imputation
- Median Imputation

### Machine Learning Methods

- Linear Regression
- Random Forest Regressor

## 6. Model Evaluation

The models were evaluated using the original salary values that were artificially hidden.

The following metrics were used:

- **MAE:** Mean Absolute Error
- **MSE:** Mean Squared Error
- **RMSE:** Root Mean Squared Error
- **R²:** Coefficient of Determination

Lower MAE, MSE and RMSE values indicate better predictions. A higher R² indicates better explanatory performance.

## 7. Project Structure

```text
salary-imputation-regression/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── notebooks/
│   └── Salary_Imputation_Project.ipynb
│
├── src/
│   ├── imputation.py
│   └── evaluation.py
│
├── results/
│   ├── comparison_results.csv
│   ├── salary_predictions.csv
│   ├── data_imputed_linear_regression.csv
│   └── data_imputed_random_forest.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 8. Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 9. How to Run the Project

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook:

```bash
jupyter notebook
```

4. Run the notebook cells in order.

## 10. Results and Discussion

The performance of the four imputation methods is compared using MAE, MSE, RMSE and R².

The comparison helps identify the most suitable approach for estimating missing employee salaries.

*The numerical results and final interpretation are presented in the notebook and the results folder.*

## 11. Conclusion

This project demonstrates how statistical methods and machine learning algorithms can be used to handle missing salary data.

It also highlights the importance of evaluating imputation methods using known values before applying them to real missing data.

## Author

**Ahlam Aberrai**

Data Analytics and Artificial Intelligence Student

**Project:** Salary Prediction and Missing Data Imputation Using Machine Learning
