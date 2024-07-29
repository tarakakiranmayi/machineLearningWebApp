# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:40:00 2024

@author: Sanjana
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetic_model=pickle.load(open('C:/Users/Sanjana/OneDrive/Desktop/Kiran_python/machineLearning/trained_model.sav','rb'))
heart_model=pickle.load(open('C:/Users/Sanjana/OneDrive/Desktop/Kiran_python/machineLearning/heart_disease.sav','rb'))
breast_model=pickle.load(open('C:/Users/Sanjana/OneDrive/Desktop/Kiran_python/machineLearning/breast_model.sav','rb'))

def diabeticPrediction(input_data):
    
    input_numpy_array=np.asarray(input_data,dtype='float')
    #reshape is done because our model knows 786 rows but we are giving 1 row
    input_reshape=input_numpy_array.reshape(1,-1)

    value=loaded_model.predict(input_reshape)
    print(value)
    if value[0]==0:
      return "IT is a diabetic person"
    else:
      return "It is not a diabetic person"


# Heart Disease Prediction
def heart_disease_prediction(input_data):
    input_numpy_array = np.asarray(input_data, dtype='float')
    # Reshape because the model expects a single row of data
    input_reshape = input_numpy_array.reshape(1, -1)

    value = heart_model.predict(input_reshape)
    if value[0] == 0:
        return "No Heart Disease"
    else:
        return "Heart Disease Positive"

# Breast Cancer Prediction
def breast_cancer_prediction(input_data):
    input_numpy_array = np.asarray(input_data, dtype='float')
    # Reshape because the model expects a single row of data
    input_reshape = input_numpy_array.reshape(1, -1)

    value = breast_model.predict(input_reshape)
    if value[0] == 0:
        return "No Breast Cancer"
    else:
        return "Breast Cancer Positive"


#side bar for navigateion
with st.sidebar:
    selected=option_menu('Mutliple Disease Prediction Ssytem',['Diabetic Predictic','Heart_Disease','Breast_Cancer'],icons=['activity','heart','parson'],default_index=0)
    


if(selected=='Diabetic Predictic'):
    st.title('Diapbetic Prediction ML')
    Pregnancies=st.text_input("Number of Pregnancies")
    Glucos=st.text_input("Number of Glucos")
    BloodPressure=st.text_input("BloodPressure")
    SkinThickness=st.text_input("Number of ,SkinThickness")
    Insulin=st.text_input("Insulin Level")
    BMI=st.text_input(" BMI")
    DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction")
    Age=st.text_input(" Age")
    
    #code for Prediction
    diagnosis=""#to store the result from prediction
    # button
    if st.button('diabeties test result'):
        diagnosis=diabeticPrediction([Pregnancies,Glucos,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
                                     
    st.success(diagnosis)
    
    
if(selected=='Heart_Disease'):
    st.title('Heart_Disease ML')
    age = st.text_input("Age")
    sex = st.text_input("Sex")
    cp = st.text_input("CP")
    trestbps = st.text_input("TrestBPS")
    chol = st.text_input("Chol")
    fbs = st.text_input("FBS")
    restecg = st.text_input("RestECG")
    thalach = st.text_input("Thalach")
    exang = st.text_input("Exang")
    oldpeak = st.text_input("OldPeak")
    slope = st.text_input("Slope")
    ca = st.text_input("CA")
    thal = st.text_input("Thal")
    
    
    # Button for Heart Disease Prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = ""  # Placeholder for actual prediction logic
        heart_inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        diagnosis = heart_disease_prediction(heart_inputs)
        st.success(diagnosis)
        mean_radius = st.text_input("Mean Radius")
    
    

if(selected=='Breast_Cancer'):
    st.title('Breast_Cancer ML')
    mean_texture = st.text_input("Mean Texture")
    mean_perimeter = st.text_input("Mean Perimeter")
    mean_area = st.text_input("Mean Area")
    mean_smoothness = st.text_input("Mean Smoothness")
    mean_compactness = st.text_input("Mean Compactness")
    mean_concavity = st.text_input("Mean Concavity")
    mean_concave_points = st.text_input("Mean Concave Points")
    mean_symmetry = st.text_input("Mean Symmetry")
    mean_fractal_dimension = st.text_input("Mean Fractal Dimension")
    radius_se = st.text_input("Radius SE")
    texture_se = st.text_input("Texture SE")
    perimeter_se = st.text_input("Perimeter SE")
    area_se = st.text_input("Area SE")
    smoothness_se = st.text_input("Smoothness SE")
    compactness_se = st.text_input("Compactness SE")
    concavity_se = st.text_input("Concavity SE")
    concave_points_se = st.text_input("Concave Points SE")
    symmetry_se = st.text_input("Symmetry SE")
    fractal_dimension_se = st.text_input("Fractal Dimension SE")
    radius_worst = st.text_input("Radius Worst")
    texture_worst = st.text_input("Texture Worst")
    perimeter_worst = st.text_input("Perimeter Worst")
    area_worst = st.text_input("Area Worst")
    smoothness_worst = st.text_input("Smoothness Worst")
    compactness_worst = st.text_input("Compactness Worst")
    concavity_worst = st.text_input("Concavity Worst")
    concave_points_worst = st.text_input("Concave Points Worst")
    symmetry_worst = st.text_input("Symmetry Worst")
    fractal_dimension_worst = st.text_input("Fractal Dimension Worst")
    
    # Button for Breast Cancer Prediction
    if st.button('Breast Cancer Test Result'):
        diagnosis = ""  # Placeholder for actual prediction logic
        breast_inputs = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, 
                     mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_se, 
                     texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, 
                     concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, 
                     perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, 
                     concave_points_worst, symmetry_worst, fractal_dimension_worst]
        diagnosis = breast_cancer_prediction(breast_inputs)
        st.success(diagnosis)
    
        
    


    