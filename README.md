#  Titanic Survival Prediction (ML + Streamlit App)

##  Project Overview
This project predicts whether a passenger survived the Titanic disaster using machine learning classification techniques. It also includes an interactive web application built using Streamlit, where users can input passenger details and get real-time predictions.

---

##  Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit

---

##  Dataset Information
The dataset contains passenger details such as:
- Pclass (Passenger Class)
- PassengerId
- Name
- Cabin
- Sex
- Age
- Fare
- SibSp (Siblings/Spouses aboard)
- Parch (Parents/Children aboard)
- Embarked

---

##  Workflow

### 1. Data Preprocessing
- Handled missing values (Age, Embarked)
- Encoded categorical variables
- Feature scaling

### 2. Exploratory Data Analysis (EDA)
- Visualized survival distribution
- Identified key patterns affecting survival

### 3. Model Building
- Logistic Regression
- Random Forest Classifier

### 4. Model Evaluation
- Accuracy Score
- Precision
- Recall
- F1 Score

---

##  Streamlit App
- Built an interactive web app using Streamlit  
- Users can input passenger details  
- Model predicts survival in real-time  


---

##  How to Run the Project

###  Run ML Model (Notebook)
1. Clone the repository  
2. Install dependencies:
   pip install pandas numpy scikit-learn matplotlib seaborn
3. Run the app:
   streamlit run app.py

---

##  Project Structure

titanic-classification/
│── dataset
│── titanic_survival_prediction.ipynb
│── app.py
│── README.md

---

##  Key Insights
- Female passengers had higher survival rates  
- First-class passengers were more likely to survive    

---

##  Future Improvements
- Hyperparameter tuning  
- Use advanced models (XGBoost)  
- Deploy app on cloud (Streamlit Cloud / Heroku)  
