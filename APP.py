import streamlit as st
import pickle
import numpy as np

model=pickle.load(open('Model.pkl','rb'))

pclass = st.number_input("Enter Pclass(1, 2, or 3) :: ", min_value=1, max_value=3, step=1)
sex = st.selectbox("Select Gender(0 for Male or 1 for Female) :: ", options=[0,1])
age = st.number_input("Enter the Age :: ", min_value=0, max_value=100)
sibsp = st.number_input("Enter the SibSp :: ", min_value=0)
parch = st.number_input("Enter the Parch :: ", min_value=0)
fare = st.number_input("Enter the Fare :: ", min_value=0.0)
embarked = st.selectbox("Select Embarked(0 for S, 1 for C or 2 for Q) :: ", options=[0,1,2])

x=np.array([pclass,sex,age,sibsp,parch,fare,embarked]).reshape(1,-1)

if(st.button('Predict')):
    result=model.predict(x)

    if(result==1):
        st.header("Survived")
    else:
        st.header("Not Survived")
