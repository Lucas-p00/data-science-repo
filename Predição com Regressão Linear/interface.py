import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib  

st.set_page_config(page_title="Previsão de Salário", layout="centered")

st.title("Previsão de salário com base no tempo de estudo mensal 📚💼")
st.write("""
Este projeto utiliza Regressão Linear para prever o salário mensal de uma pessoa com base no total de horas que ela dedica aos estudos por mês baseado em um dataset fictício. 
Ajuste o número de horas estudadas abaixo e veja automaticamente a previsão do salário!
""")

model = joblib.load("regression_model.pkl")  

st.header("Insira os Dados")
study_time = st.slider("Tempo de estudo mensal (em horas):", min_value=0, max_value=300, step=5)

predicted_salary = model.predict([[study_time]])[0]

st.subheader(f"O salário estimado é: R$ {predicted_salary:,.2f}")