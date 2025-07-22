# 💼 Employee Salary Prediction App

An interactive and smart web application that predicts an employee’s **annual salary** based on demographic, education, and work-related features. Built using **Streamlit**, **XGBoost**, and a **custom pipeline**, the app provides a clean UI with **avatar generation**, **theme toggle**, **CSV upload/download**, and **visual prediction insights**.

---

## 🚀 Features

✅ Predict salary from a single employee's input  
✅ CSV upload for batch salary predictions  
✅ Animated emojis based on prediction result  
✅ Gender-based Avatar Generator  
✅ Company Logo (top-right aligned)  
✅ Dark/Light mode toggle  
✅ Download prediction results as CSV  

---

## 🧠 Tech Stack

| Tool           | Purpose                           |
|----------------|-----------------------------------|
| **Python**     | Core programming language         |
| **Streamlit**  | Web app framework                 |
| **Pandas**     | Data handling                     |
| **XGBoost**    | Salary prediction model           |
| **Scikit-learn** | Data preprocessing pipeline     |
| **Joblib**     | Model serialization               |
| **Plotly**     | Gauge chart visualization         |
| **HTML/CSS**   | UI customization via markdown     |

---

## 📂 Folder Structure

📁 salary-prediction-app/
├── app.py                        # Main Streamlit app
├── salary_pipeline_model.pkl    # Trained XGBoost model
├── sample_input.csv             # Example CSV for testing
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies (optional)
└── images/
    ├── logo.png                 # Top-right company logo
    └── avatars/
        ├── male_1st.png
        └── female_1st.png

---

## 📈 Input Features

| Feature           | Description                         |
|-------------------|-------------------------------------|
| `age`             | Age of the employee                 |
| `fnlwgt`          | Final weight (sampling factor)      |
| `educational-num` | Education level (1–16)              |
| `capital-gain`    | Capital gain from investment        |
| `capital-loss`    | Capital loss                       |
| `hours-per-week`  | Weekly working hours                |
| `workclass`       | Type of employment (Private, etc.)  |
| `marital-status`  | Marital status                      |
| `occupation`      | Job role                            |
| `relationship`    | Relationship type                   |
| `race`            | Race                                |
| `gender`          | Male / Female                       |
| `native-country`  | Country of origin                   |

---

## 🖼 Sample Input (UI Prediction)

```python
{
    'age': 35,
    'fnlwgt': 200000,
    'educational-num': 13,
    'capital-gain': 0,
    'capital-loss': 0,
    'hours-per-week': 40,
    'workclass': 'Private',
    'marital-status': 'Married-civ-spouse',
    'occupation': 'Exec-managerial',
    'relationship': 'Husband',
    'race': 'White',
    'gender': 'Male',
    'native-country': 'United-States'
}
