# import streamlit as st
# import pandas as pd
# import joblib 
# import numpy as np
# from sklearn.preprocessing import StandardScaler

# scaler = joblib.load(r'models/scaler')
# model = joblib.load(r'models/best_model')

# st.header('Placement Prediction App') # App name

# # CGPA,Internships,Projects,Workshops/Certifications,AptitudeTestScore,SoftSkillsRating,SSC_Marks,HSC_Marks,ExtracurricularActivities_Yes,PlacementTraining_Yes
# # PlacementStatus_Placed

# cgpa = st.number_input("CGPA")
# internships = st.number_input("Internships")
# projects = st.number_input("Projects")
# workshops = st.number_input("Workshops/Certifications")
# aptitude = st.number_input("Aptitude Test Score")
# softskills = st.number_input("Soft Skills Rating")
# extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
# training = st.selectbox("Placement Training", ["Yes", "No"])
# ssc = st.number_input("SSC Marks")
# hsc = st.number_input("HSC Marks")

# df = pd.DataFrame([{'CGPA':cgpa,
#     'Internships':internships,
#     'Projects':projects,
#     'Workshops/Certifications':workshops,
#     'AptitudeTestScore':aptitude,
#     'SoftSkillsRating':softskills,
#     'SSC_Marks':ssc,
#     'HSC_Marks':hsc,
#     'ExtracurricularActivities_Yes':extracurricular,
#     'PlacementTraining_Yes':training
#     }])

# st.write(df)

# # cat_col = df.select_dtypes(include='object').columns.to_list()

# #         # One-hot encoding
# # df = pd.get_dummies(df, columns=cat_col, drop_first=True, dtype='int')


# scaler = StandardScaler()
# x = scaler.fit_transform(df)






# def preprocess_input(cgpa, internships, projects, workshops, aptitude, softskills, extracurricular, training, ssc, hsc):
#     extracurricular = 1 if extracurricular == "Yes" else 0
#     training = 1 if training == "Yes" else 0
#     # Ensure input is in the same format as training data
#     input_data = np.array([[cgpa, internships, projects, workshops, aptitude, softskills, extracurricular, training, ssc, hsc]])
#     return input_data

# if st.button("Predict Placement"):
#     input_data = preprocess_input(cgpa, internships, projects, workshops, aptitude, softskills, extracurricular, training, ssc, hsc)
#     prediction = model.predict(input_data)
#     result = "Placed" if prediction[0] == 1 else "Not Placed"
#     st.write(f"### Prediction: {result}")


import joblib
import streamlit as st
import pandas as pd
import numpy as np

# Load the trained scaler and model
scaler = joblib.load('models\scaler')
model = joblib.load('models\best_model')

st.header('Placement Prediction App')  # App name

# Input fields
cgpa = st.number_input("CGPA")
internships = st.number_input("Internships")
projects = st.number_input("Projects")
workshops = st.number_input("Workshops/Certifications")
aptitude = st.number_input("Aptitude Test Score")
softskills = st.number_input("Soft Skills Rating")
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
training = st.selectbox("Placement Training", ["Yes", "No"])
ssc = st.number_input("SSC Marks")
hsc = st.number_input("HSC Marks")

# Convert categorical inputs to numerical values
extracurricular = 1 if extracurricular == "Yes" else 0
training = 1 if training == "Yes" else 0

# Create DataFrame with user input
df = pd.DataFrame([{
    'CGPA': cgpa,
    'Internships': internships,
    'Projects': projects,
    'Workshops/Certifications': workshops,
    'AptitudeTestScore': aptitude,
    'SoftSkillsRating': softskills,
    'SSC_Marks': ssc,
    'HSC_Marks': hsc,
    'ExtracurricularActivities_Yes': extracurricular, 
    'PlacementTraining_Yes': training 
}])

# Display user input
st.write("### User Input Data:")
st.write(df)

# Scale input data using the preloaded scaler
scaled_input = scaler.transform(df)

if st.button("Predict Placement"):
    pred = model.predict(scaled_input)
    result = "🎉 Placed" if pred[0] == 1 else "❌ Not Placed"
    st.write(f"### Prediction: {result}")
