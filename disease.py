import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the ML models
diabetes_model = pickle.load(open('C:/Users/PREODATOR HELIOS 300/Desktop/disease/sav files/diabetes_model.sav', 'rb'))
heartdisease_model = pickle.load(open('C:/Users/PREODATOR HELIOS 300/Desktop/disease/sav files/heartdisease_model.sav', 'rb'))
parkinson_model = pickle.load(open('C:/Users/PREODATOR HELIOS 300/Desktop/disease/sav files/parkinson_model.sav', 'rb'))

# Sidebar with disease selection
with st.sidebar:
    selected = option_menu('Disease Predictor', ['Diabetes', 'Heart Disease', 'Parkinsons'],
                           icons=['activity','heart','person'], default_index=0)

# Disease boxes with brief descriptions and accuracy input
if selected == 'Diabetes':
    st.title('Diabetes Prediction')
    st.write('Diabetes is a chronic condition that affects the way your body metabolizes glucose.')
    st.write('the accuracy score for Diabetes prediction:76.62%')
    st.session_state.selected = selected

elif selected == 'Heart Disease':
    st.title('Heart Disease Prediction')
    st.write('Heart disease refers to several conditions that affect the heart.')
    st.write('the accuracy score for Heart Disease prediction:78.5%')
    st.session_state.selected = selected

elif selected == 'Parkinsons':
    st.title('Parkinsons Disease Prediction')
    st.write('Parkinsons disease is a progressive nervous system disorder that affects movement.')
    st.write('the accuracy score for Parkinsons prediction:89.74%')
    st.session_state.selected = selected

# Prediction phase based on selected disease
if 'selected' in st.session_state:
    selected = st.session_state.selected
    
    if selected == 'Diabetes':
        # Clear input fields of other predictions
        st.session_state.pop('heart_input', None)
        st.session_state.pop('parkinson_input', None)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            Pregnancies=st.text_input('Number of Pregnancies')
        with col1:
            Glucose=st.text_input('Glucose Level')
        with col2:
            BloodPressure=st.text_input('Blood Pressure')
        with col2:
            SkinThickness=st.text_input('Skin Thickness')
        with col3:
            Insulin=st.text_input('Insulin Level')
        with col3:
            BMI=st.text_input('BMI')
        with col4:
            DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
        with col4:
            Age=st.text_input('Age')
        
        diab_diagnosis = ''
        
        if st.button('Diabetes Prediction'):
            # Convert input values to float
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), 
                            float(SkinThickness), float(Insulin), float(BMI), 
                            float(DiabetesPedigreeFunction), float(Age)]
            
            # Make prediction
            diab_prediction = diabetes_model.predict([input_data])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = 'Diabetic'
            else:
                diab_diagnosis = 'Non-Diabetic'
                
        st.success(diab_diagnosis)
        
    elif selected == 'Heart Disease':
        # Clear input fields of other predictions
        st.session_state.pop('diabetes_input', None)
        st.session_state.pop('parkinson_input', None)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            age = st.text_input('Age')
            sex = st.text_input('sex(1->Male and 0->Female)')
        with col2:
            cp = st.text_input('chest pain')
            trestbps = st.text_input('resting blood pressure')
        with col3:
            chol = st.text_input('serum cholestrol')
            fbs = st.text_input('fasting blood sugar')
        with col4:
            restecg = st.text_input('resting ecg level')
            thalach = st.text_input('Max heart rate')
        with col1:
            exang = st.text_input('Exercise induced angina')
        with col3:
            oldpeak = st.text_input('ST depression')
            slope = st.text_input('Slope of peak exercise value')
        with col2:
            ca = st.text_input('vessels colored')
            thal = st.text_input('Thal')
            
        heart_diagnosis = ''
        
        if st.button('Heart Disease Prediction'):
            # Convert input values to float
            input_data = [float(age), float(sex), float(cp), 
                            float(trestbps),float(chol),float(fbs), float(restecg), float(thalach), 
                            float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            
            # Make prediction
            heart_prediction = heartdisease_model.predict([input_data])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'Patient has heart disease'
            else:
                heart_diagnosis = 'Patient has no heart disease'
                
        st.success(heart_diagnosis)

    elif selected == 'Parkinsons':
        # Clear input fields of other predictions
        st.session_state.pop('diabetes_input', None)
        st.session_state.pop('heart_input', None)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            MDVPFo = st.text_input('Avg vocal frequency')
            MDVPFhi = st.text_input('Max vocal frequency')
        with col2:
            MDVPF = st.text_input('Min vocal frequency')
            MDVPJ= st.text_input('Variation in frequency')
        with  col3:
            MDVPS = st.text_input('Variation in amplitude')
            HNR = st.text_input('Noise to tonal ratio')
        with col4:
            RPDE = st.text_input('Non linear complexity1')
            DFA = st.text_input('Signal fractal scale')
        with col1:
            spread1 = st.text_input('Non linear measure1')
            spread2 = st.text_input('Non linear measure2')
        with col3:
            D = st.text_input('Non linear complexity2')
            
        Parkinsons_diagnosis = ''
    
        if st.button('Parkinsons Prediction'):
            # Convert input values to float
            input_data = [float(MDVPFo), float(MDVPFhi), float(MDVPF), 
                          float(MDVPJ),float(MDVPS),float(HNR), float(RPDE), float(DFA), 
                          float(spread1), float(spread2),float(D)]
            
            # Make prediction
            Parkinsons_prediction = parkinson_model.predict([input_data])
            
            if Parkinsons_prediction[0] == 1:
                Parkinsons_diagnosis = 'Patient has Parkinsons'
            else:
                Parkinsons_diagnosis = 'Patient has no Parkinsons'
                
        st.success(Parkinsons_diagnosis)

