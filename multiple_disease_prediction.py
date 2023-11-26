import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
# don't forget to change '\' to '/'
diabetes_model = pickle.load(
    open('F:/Jupyter files/Projects/Multi Disease Prediction/Saved models/Diabetes prediction model.sav', 'rb'))

heart_disease_model = pickle.load(
    open('F:/Jupyter files/Projects/Multi Disease Prediction/Saved models/Heart disease model.sav', 'rb'))

parkinsons_disease_model = pickle.load(
    open('F:/Jupyter files/Projects/Multi Disease Prediction/New saved models/parkinsons_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes disease prediction', 'Heart disease prediction', 'Parkinsons disease prediction'],
                           icons=['capsule', 'activity', 'person'],
                           default_index=0)

#     test comment

# Diabetes Prediction page
if (selected == 'Diabetes disease prediction'):

    # page title
    st.title('Diabetes disease prediction Using ML')

    # taking inputs
    # creating columns
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input('Please enter the number of pregnancies you have had?')
    with col2:
        Glucose = st.text_input('Please enter your fasting blood glucose level in mg/dL?')
    with col1:
        BloodPressure = st.text_input('Please enter your blood pressure in mm Hg. (e.g., 120/80?')
    with col2:
        SkinThickness = st.text_input('Please enter the thickness of your skinfold in millimeters?')
    with col1:
        Insulin = st.text_input('Please enter your insulin level in mU/mL?')
    with col2:
        BMI = st.text_input('Please enter your Body Mass Index (BMI)?')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Please enter the diabetes pedigree function score?')
    with col2:
        Age = st.text_input('Please enter your age in years?')

    # code for prediction
    diab_detection = ''

    # creating a button for prediction
    if st.button('Diabetes Test Results'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_detection = 'The person is Diabetic'
        else:
            diab_detection = 'The person is not Diabetic'
    st.success(diab_detection)

# Heart disease prediction page
if (selected == 'Heart disease prediction'):
    # page title
    st.title('Heart disease prediction Using ML')

    # taking inputs from user
    # creating columns
    colh1, colh2 = st.columns(2)
    with colh1:
        age = st.text_input('Please enter your age in years?')
    with colh2:
        sex = st.text_input('Please enter your gender. (Use numerical codes, e.g., 1 for male, 0 for female)?')
    with colh1:
        chest_pain_type = st.text_input('Please enter the type of chest pain you experience. (Use numerical codes, e.g., 1 for typical angina, 2 for atypical angina, 3 for non-anginal pain, 4 for asymptomatic)?')
    with colh2:
        resting_blood_pressure = st.text_input('Please enter your resting blood pressure in mm Hg?')
    with colh1:
        cholestoral = st.text_input('Please enter your cholesterol level in mg/dL?')
    with colh2:
        fasting_blood_sugar = st.text_input('Please enter your fasting blood sugar level. (Use numerical codes, e.g., 1 for >120 mg/dL, 0 for <=120 mg/dL)?')
    with colh1:
        rest_ecg = st.text_input('Please enter the result of your resting electrocardiogram. (Use numerical codes, e.g., 0 for normal, 1 for having ST-T wave abnormality, 2 for showing probable or definite left ventricular hypertrophy)?')
    with colh2:
        Max_heart_rate = st.text_input('Please enter your maximum heart rate during exercise?')
    with colh1:
        exercise_induced_angina = st.text_input('Please enter whether you experience exercise-induced angina. (Use numerical codes, e.g., 1 for yes, 0 for no)?')
    with colh2:
        oldpeak = st.text_input('Please enter the depression induced by exercise relative to rest?')
    with colh1:
        slope = st.text_input('Please enter the slope of the peak exercise ST segment. (Use numerical codes, e.g., 1 for upsloping, 2 for flat, 3 for downsloping)?')
    with colh2:
        vessels_colored_by_flourosopy = st.text_input('Please enter the number of major vessels colored by fluoroscopy?')
    with colh1:
        thalassemia = st.text_input('Please enter your thalassemia type. (Use numerical codes, e.g., 3 for normal, 6 for fixed defect, 7 for reversible defect)?')

    # prediction variable
    heart_detection = ''

    # creating a button for prediction
    if st.button('Detect Heart Disease'):
        heart_prediction = heart_disease_model.predict([[age, sex, chest_pain_type, resting_blood_pressure, cholestoral, fasting_blood_sugar, rest_ecg, Max_heart_rate, exercise_induced_angina, oldpeak, slope, vessels_colored_by_flourosopy, thalassemia]])

        if(heart_prediction[0]==1):
            heart_detection = 'The person is suffering a Heart Disease'
        else:
            heart_detection = 'The person is not suffering from any Heart Disease'
    st.success(heart_detection)

# Parkinsons disease prediction page
if (selected == 'Parkinsons disease prediction'):
    # page title
    st.title('Parkinsons disease prediction Using ML')

    # taking inputs from users
    # creating columns
    colp1, colp2 = st.columns(2)
    with colp1:
        MDVP_Fo_Hz = st.text_input('MDVP_Fo_Hz: Please enter the fundamental frequency of your voice in Hertz?')
    with colp2:
        MDVP_Fhi_Hz = st.text_input('MDVP_Fhi_Hz: Please enter the highest fundamental frequency of your voice in Hertz?')
    with colp1:
        MDVP_Flo_Hz = st.text_input('MDVP_Flo_Hz: Please enter the lowest fundamental frequency of your voice in Hertz?')
    with colp2:
        MDVP_Jitter_percent = st.text_input('Please enter the percentage of jitter in your voice?')
    with colp1:
        MDVP_Jitter_Abs = st.text_input('Please enter the absolute jitter value in your voice?')
    with colp2:
        MDVP_RAP = st.text_input('MDVP_RAP: Please enter the relative average perturbation in your voice?')
    with colp1:
        MDVP_PPQ = st.text_input('MDVP_PPQ: Please enter the five-point period perturbation quotient of your voice?')
    with colp2:
        Jitter_DDP = st.text_input('Please enter the average absolute difference of differences in consecutive jitter cycles?')
    with colp1:
        MDVP_Shimmer = st.text_input('Please enter the amplitude variation in your voice?')
    with colp2:
        MDVP_Shimmer_dB = st.text_input('MDVP_Shimmer_dB: Please enter the amplitude variation in decibels of your voice?')
    with colp1:
        Shimmer_APQ3 = st.text_input('Shimmer_APQ3: Please enter the amplitude variation in decibels of your voice?')
    with colp2:
        Shimmer_APQ5 = st.text_input('Shimmer_APQ5: Please enter the five-point amplitude perturbation quotient of your voice?')
    with colp1:
        MDVP_APQ = st.text_input('MDVP_APQ: Please enter the amplitude perturbation quotient of your voice?')
    with colp2:
        Shimmer_DDA = st.text_input('Shimmer_DDA: Please enter the average absolute differences between consecutive cycles of amplitude perturbation?')
    with colp1:
        NHR = st.text_input('NHR: Please enter the ratio of noise to harmonic components in your voice?')
    with colp2:
        HNR = st.text_input('HNR: Please enter the harmonic-to-noise ratio of your voice?')
    with colp1:
        RPDE = st.text_input('RPDE: Please enter the recurrence period density entropy of your voice?')
    with colp2:
        DFA = st.text_input('DFA: Please enter the detrended fluctuation analysis of your voice?')
    with colp1:
        spread1 = st.text_input('Please enter the first spreading of your voice data?')
    with colp2:
        spread2 = st.text_input('Please enter the second spreading of your voice data?')
    with colp1:
        D2 = st.text_input('D2: Please enter the nonlinear measure of fundamental frequency variation in your voice?')
    with colp2:
        PPE = st.text_input('PPE: Please enter the pitch period entropy of your voice?')

    # variable for prediction
    parkinsons_prediction = ''

    # creating button for detection
    if st.button('Detect Parkinsons Disease'):
        parkinsons_detection = parkinsons_disease_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if(parkinsons_detection[0]==1):
            parkinsons_prediction = 'Person is suffering from Parkinsons Disease'
        else:
            parkinsons_prediction = 'Person is not suffering from Parkinsons Disease'
    st.success(parkinsons_prediction)