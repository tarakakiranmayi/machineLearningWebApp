# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:03:27 2024

@author: Sanjana
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/Sanjana/OneDrive/Desktop/Kiran_python/machineLearning/trained_model.sav','rb'))

#creating function for prediction

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
  
def main():
    
    
    #giving title for webpage
    st.title('Diabetics Prediction Web App')
    
    #getting the input data
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
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


#ruuning from anconda comand prompt name as main so main function will load we wriiten like this beacsue whne cmd start only this should load
if __name__ =='__main__':
    main()
    
    
    