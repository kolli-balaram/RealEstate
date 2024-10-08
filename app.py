import streamlit as st
import numpy as np
import pickle
with open("estate_model.pkl",'rb') as file:
    model = pickle.load(file)
bedrooms = st.number_input("bed rooms ")
bathrooms = st.number_input("bath rooms ")
status = st.number_input("Status ")
size = st.number_input("size")
location = st.number_input("location")
face = st.number_input("face")
type = st.number_input("Type")
arr = np.array([[bedrooms,bathrooms,status,size,location,face,type]])
model.predict(arr)

