# 🛒 BigMart Sales Prediction using Gradient Boosting

## 📌 Project Overview
This project predicts **Item_Outlet_Sales** for BigMart products using **Machine Learning**. A **Gradient Boosting Regressor** model is trained to learn sales patterns from historical data and evaluate performance using regression metrics.

## 📂 Dataset
- **Name:** BigMart Sales Data  
- **Target Variable:** `Item_Outlet_Sales`  
- **Dropped Columns:**
  - `Item_Outlet_Sales` (target)
  - `Outlet_Establishment_Year` (removed during preprocessing)

## ⚙️ Data Preparation
```python
X = df.drop(['Item_Outlet_Sales','Outlet_Establishment_Year'], axis=1)
y = df['Item_Outlet_Sales']
```

## 🔀 Train–Test Split
- **Training Data:** 70%
- **Testing Data:** 30%
- **Random State:** 42

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
```

## 🤖 Model Used
**Gradient Boosting Regressor**

**Why Gradient Boosting?**
- Handles non-linear relationships
- Reduces bias and variance
- Performs well on structured/tabular data

### Model Configuration
```python
GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3
)
```

## 📊 Model Evaluation
| Metric | Value |
|------|------|
| **R² Score** | 0.58 |
| **MSE** | 961,982.48 |
| **RMSE** | 980.80 |

```python
r2_score(y_test, y_pred)
mean_squared_error(y_test, y_pred)
```

### 🔎 Interpretation
- **R² = 0.58** → Model explains ~58% of the variance in sales
- **RMSE ≈ 981** → Average prediction error in sales units

## 💾 Model Saving & Loading
```python
# Save model
pickle.dump(GR, open('model.pkl', 'wb'))

# Load model
model = pickle.load(open('model.pkl', 'rb'))
```

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Pickle

## 🚀 Future Improvements
- Feature engineering (log transformation, encoding optimization)
- Hyperparameter tuning
- Try advanced models (XGBoost, LightGBM)
- Model deployment using Flask / Streamlit

## 📌 Conclusion
This project demonstrates an **end-to-end machine learning pipeline**:
- Data preprocessing
- Model training
- Evaluation
- Model persistence

It is suitable for **ML beginners to intermediate learners** and can be extended into a **production-ready application**.

