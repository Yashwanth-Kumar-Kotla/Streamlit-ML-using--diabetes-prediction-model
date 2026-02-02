import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("/Users/yashwanthkumar/Desktop/ML project/Streamlit ML using  diabetes prediction model/trained_model.sav", "rb"))

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



def main():
    st.title("Diabetes Prediction Web App")

    #getting input values from the user

    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure of the Patient")
    SkinThickness = st.text_input("SkinThickness Value")
    Insulin = st.text_input("Insulin Percentage")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    Age = st.text_input("Age of the patient")

    diagnosis = ""

    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__ ==  "__main__":
    main()
 
