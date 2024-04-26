# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:27:12 2024

@author: hp
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/hp/Machine Learning/trained_model.sav', 'rb'))

def heartdiseaseprediction(input_data):
    input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease'
      
def main():
    # Add custom CSS to set background color
    st.markdown(
    """
    <style>
        .stApp {
            background-color:#FFC0CB;
        }
    </style>
    """,
    unsafe_allow_html=True
    )

    #giving a title
    st.title("Heart Disease Prediction")
    
    #getting the input data from the user
    
    Age = st.text_input('Age')
    Sex = st.text_input('Sex')
    ChestPain = st.text_input('Chest Pain')
    RestingBloodPressure = st.text_input('Resting Blood Pressure')
    Cholestrol = st.text_input('Cholestrol')
    FastingBloodSugar= st.text_input('Fasting Blood Sugar')
    RestingElectrocardiographicmeasurement= st.text_input('Resting Electrocardiographic measurement')
    MaximumHeartrate= st.text_input('Maximum Heart rate achieved')
    ExerciseInducedangina= st.text_input('Exercise Induced angina')
    STDepression= st.text_input('ST Depression induced by exercise relative to rest')
    SlopeofthepeakexerciseSTsegment = st.text_input('Slope of the peak exercise ST segment')
    majorvessels= st.text_input('The number of major vessels(0-3)')
    thalassemia = st.text_input('If the person has thalassemia')
    
    #code for prediction
    diagnosis=''
    # creating a button for Prediction
    
    if st.button('Heart Disease Prediction Test Result'):
        diagnosis = heartdiseaseprediction([Age,Sex,ChestPain,RestingBloodPressure,Cholestrol,FastingBloodSugar,RestingElectrocardiographicmeasurement,MaximumHeartrate,ExerciseInducedangina,STDepression,SlopeofthepeakexerciseSTsegment,majorvessels,thalassemia
])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
   
    
