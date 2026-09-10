
# Food Demand Forecasting & Surplus Estimation

## Project Overview

This project develops a machine learning-based food demand forecasting system for food-service environments such as campuses, hostels, canteens, and hospitality settings.

The system predicts expected food demand using historical demand data and relevant operational factors. The predicted demand is then compared with the planned food quantity to estimate potential surplus or shortage.

A Streamlit dashboard is developed to provide an interactive interface for making predictions and supporting food preparation decisions.

---

## Objectives

- Analyze historical food demand data.
- Identify important factors affecting food demand.
- Perform exploratory data analysis and feature engineering.
- Develop machine learning models for demand prediction.
- Compare multiple regression models.
- Select the best-performing model.
- Estimate potential food surplus or shortage.
- Provide preparation recommendations.
- Develop an interactive Streamlit dashboard.

---

## Dataset

The dataset contains food demand records with the following features:

- `id`
- `week`
- `center_id`
- `meal_id`
- `checkout_price`
- `base_price`
- `emailer_for_promotion`
- `homepage_featured`
- `num_orders`

The target variable is:

`num_orders`

The dataset contains 1,999 records and 9 original features.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook / VS Code

---

## Machine Learning Workflow

The project follows these major steps:

1. Data loading
2. Data understanding
3. Data quality checking
4. Exploratory Data Analysis
5. Feature engineering
6. Time-based train-test splitting
7. Categorical feature encoding
8. Model training
9. Model evaluation
10. Model comparison
11. Surplus/shortage estimation
12. Model saving
13. Streamlit dashboard integration

## Feature Engineering

Cyclical features were created from the week variable:

- `week_sin`
- `week_cos`

These features help represent the cyclical nature of weekly patterns.

The original `id` column was removed because it does not provide meaningful predictive information for the demand model.

---

## Models Evaluated

Three regression models were evaluated:

1. Random Forest Regressor
2. Extra Trees Regressor
3. Gradient Boosting Regressor

### Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest | 129.57 | 216.50 | 0.4974 |
| Extra Trees | 113.72 | 202.30 | 0.5612 |
| Gradient Boosting | 113.96 | 191.36 | 0.6074 |

Gradient Boosting was selected as the best-performing model among the evaluated models because it achieved the highest R² score and the lowest RMSE.

---

## Final Model Verification

The saved Gradient Boosting model was independently verified using the test dataset.

Final verification results:

```text
MAE  : 113.96
RMSE : 191.36
R²   : 0.6074
````

The trained model and preprocessing pipeline are saved for use by the Streamlit application.

---

## Surplus and Shortage Estimation

The system compares predicted demand with planned food quantity.

### Formula

`Potential Surplus = Planned Quantity - Predicted Demand`

If the result is positive, the system reports potential surplus.

If the result is negative, the system reports potential shortage.

The estimated surplus represents a decision-support estimate and does not represent actual measured food waste.

---

## Streamlit Dashboard

The dashboard provides:

* Center selection
* Meal selection
* Week input
* Checkout price input
* Base price input
* Email promotion selection
* Homepage featured selection
* Planned food quantity
* Predicted demand
* Potential surplus or shortage
* Preparation recommendations
* Demand vs planned quantity visualization
* Historical demand trend
* Model performance information

---

## Dashboard Workflow

```text
User Input
    ↓
Feature Preparation
    ↓
Data Preprocessing
    ↓
Gradient Boosting Model
    ↓
Predicted Food Demand
    ↓
Compare with Planned Quantity
    ↓
Surplus / Shortage Estimation
    ↓
Recommendation
```

---

## Project Structure

```text
Food_Demand_Forecasting/
│
├── app/
│   └── app.py
│
├── data/
│   └── Food demand.csv
│
├── models/
│   ├── food_demand_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

From the project root directory:

```bash
streamlit run app/app.py
```

The application will open in the browser.

---

## Business Interpretation

The predicted demand can help food-service operators estimate how much food may be required for a selected center, meal, week, price, and promotion configuration.

The surplus/shortage calculation provides a simple decision-support mechanism for comparing expected demand with the planned preparation quantity.

---

## Limitations

* The model is trained using the available historical dataset.
* The current dataset contains a limited number of operational features.
* Actual food waste is not directly measured.
* Surplus is an estimate based on planned quantity and predicted demand.
* Factors such as weather, special events, holidays, attendance, and sudden changes in demand are not included.

---

## Future Enhancements

Possible future improvements include:

* Incorporating weather information.
* Including holidays and special events.
* Using attendance or meal-registration data.
* Adding more advanced forecasting techniques.
* Improving model performance through hyperparameter tuning.
* Adding automated surplus alerts.
* Integrating the system with food redistribution workflows.
* Supporting real-time demand updates.

---

## Conclusion

This project demonstrates an end-to-end machine learning solution for food demand forecasting and potential surplus/shortage estimation.

It combines exploratory data analysis, feature engineering, machine learning model comparison, prediction, business-oriented surplus estimation, and an interactive Streamlit dashboard into a single decision-support application.

