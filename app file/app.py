import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Titanic Predictor", page_icon="🚢")
st.title("🚢 Titanic Survival Predictor")

@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    return model, scaler

model, scaler = load_model()

# Inputs
pclass = st.selectbox("Pclass", [1,2,3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Siblings/Spouses", 0, 8, 0)
parch = st.number_input("Parents/Children", 0, 6, 0)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)
embarked = st.selectbox("Embarked", ["Q", "S"])  # सिर्फ 2 options

if st.button("🚀 Predict"):
    sex_enc = 1 if sex == "Female" else 0
    emb_Q = 1 if embarked == "Q" else 0
    emb_S = 1 if embarked == "S" else 0
    
    # ✅ 8 FEATURES (तुम्हारे scaler के according)
    data = np.array([[pclass, sex_enc, age, sibsp, parch, fare, emb_Q, emb_S]])
    
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)[0]
    
    st.balloons()
    if pred == 1:
        st.success("✅ SURVIVED!")
    else:
        st.error("❌ Did Not Survive")