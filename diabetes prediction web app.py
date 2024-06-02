# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:01:25 2024

@author: ijehn
"""

import numpy as np
import pickle
import streamlit as st #noqa: F401

# loading the saved model
loaded_model = pickle.load(open(r'C:/Users/ijehn/trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    

 
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
import streamlit as st #noqa: F401 
  
def main():
  #giving a title   
  st.title('Diabetes Prediction App')
  
  #getting input data from the user
  #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
  
  Pregnancies = st.text_input('number of pregnancies')   
  Glucose = st.text_input('number of glucose')  
  BloodPressure = st.text_input('number of bloodpressure value')
  SkinThickness = st.text_input('number of SkinThickness')  
  Insulin = st.text_input('number of Insulin')
  BMI = st.text_input('number of BMI')  
  DiabetesPedigreeFunction = st.text_input('number of DiabetesPedigreeFunction')  
  Age = st.text_input('number of Age')         

  #code for prediction
  diagnosis = ''      
  #creating a button for prediction
  
  if st.button('TEST RESULT'):
      diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
   
  st.success(diagnosis)





if __name__ == '__main__':
    main()      