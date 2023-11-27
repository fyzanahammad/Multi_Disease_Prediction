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
    open('F:/Jupyter files/Projects/Multi Disease Prediction/Saved models/Parkinsons disease model.sav', 'rb'))

breast_cancer_model = pickle.load(
    open('F:/Jupyter files/Projects/Multi Disease Prediction/Saved models/Breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes disease prediction', 'Heart disease prediction', 'Parkinsons disease prediction' , 'Breast Cancer Classifier'],
                           icons=['capsule', 'activity', 'person','chat-square-heart'],
                           default_index=0)


# Diabetes Prediction page
if (selected == 'Diabetes disease prediction'):

    # page title
    st.title('Diabetes disease prediction Using ML')

    # taking inputs
    # creating columns
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input('Number of pregnancies?')
    with col2:
        Glucose = st.text_input('Fasting blood glucose level in mg/dL?')
    with col1:
        BloodPressure = st.text_input('Blood pressure in mm Hg?')
    with col2:
        SkinThickness = st.text_input('Thickness of your skinfold in millimeters?')
    with col1:
        Insulin = st.text_input('Insulin level in mU/mL?')
    with col2:
        BMI = st.text_input('Body Mass Index (BMI)?')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function score?')
    with col2:
        Age = st.text_input('Your age in years?')

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
    colb1, colb2 = st.columns(2)
    with colb1:
        age = st.text_input('Your age in years?')
    with colb2:
        sex = st.text_input('Your gender. (Use numerical codes, e.g., 1 for male, 0 for female)?')
    with colb1:
        chest_pain_type = st.text_input(
            'Type of chest pain. (Use numerical codes, e.g., 1 for typical angina, 2 for atypical angina, 3 for non-anginal pain, 4 for asymptomatic)?')
    with colb2:
        resting_blood_pressure = st.text_input('Resting blood pressure in mm Hg?')
    with colb1:
        cholestoral = st.text_input('Cholesterol level in mg/dL?')
    with colb2:
        fasting_blood_sugar = st.text_input(
            'Fasting blood sugar level. (Use numerical codes, e.g., 1 for >120 mg/dL, 0 for <=120 mg/dL)?')
    with colb1:
        rest_ecg = st.text_input(
            'Result of your resting electrocardiogram. (Use numerical codes, e.g., 0 for normal, 1 for ST-T wave abnormality, 2 for probable or definite left ventricular hypertrophy)?')
    with colb2:
        Max_heart_rate = st.text_input('Maximum heart rate during exercise?')
    with colb1:
        exercise_induced_angina = st.text_input(
            'Experience exercise-induced angina. (Use numerical codes, e.g., 1 for yes, 0 for no)?')
    with colb2:
        oldpeak = st.text_input('Depression induced by exercise relative to rest?')
    with colb1:
        slope = st.text_input(
            'Slope of the peak exercise ST segment. (Use numerical codes, e.g., 1 for upsloping, 2 for flat, 3 for downsloping)?')
    with colb2:
        vessels_colored_by_flourosopy = st.text_input('Number of major vessels colored by fluoroscopy?')
    with colb1:
        thalassemia = st.text_input(
            'Your thalassemia type. (Use numerical codes, e.g., 3 for normal, 6 for fixed defect, 7 for reversible defect)?')

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
        MDVP_Fo_Hz = st.text_input('MDVP_Fo_Hz: Fundamental frequency (MDVP_Fo) of your voice in Hertz?')
    with colp2:
        MDVP_Fhi_Hz = st.text_input('MDVP_Fhi_Hz: Highest fundamental frequency (MDVP_Fhi) of your voice in Hertz?')
    with colp1:
        MDVP_Flo_Hz = st.text_input('MDVP_Flo_Hz: Lowest fundamental frequency (MDVP_Flo) of your voice in Hertz?')
    with colp2:
        MDVP_Jitter_percent = st.text_input('MDVP_Jitter_percent: Percentage of jitter in your voice?')
    with colp1:
        MDVP_Jitter_Abs = st.text_input('MDVP_Jitter_Abs: Absolute jitter value in your voice?')
    with colp2:
        MDVP_RAP = st.text_input('MDVP_RAP: Relative average perturbation (MDVP_RAP) in your voice?')
    with colp1:
        MDVP_PPQ = st.text_input('MDVP_PPQ: Five-point period perturbation quotient (MDVP_PPQ) of your voice?')
    with colp2:
        Jitter_DDP = st.text_input(
            'Jitter_DDP: Average absolute difference of differences in consecutive jitter cycles (Jitter_DDP)?')
    with colp1:
        MDVP_Shimmer = st.text_input('MDVP_Shimmer: Amplitude variation (MDVP_Shimmer) in your voice?')
    with colp2:
        MDVP_Shimmer_dB = st.text_input(
            'MDVP_Shimmer_dB: Amplitude variation in decibels (MDVP_Shimmer_dB) of your voice?')
    with colp1:
        Shimmer_APQ3 = st.text_input(
            'Shimmer_APQ3: Three-point amplitude perturbation quotient (Shimmer_APQ3) of your voice?')
    with colp2:
        Shimmer_APQ5 = st.text_input(
            'Shimmer_APQ5: Five-point amplitude perturbation quotient (Shimmer_APQ5) of your voice?')
    with colp1:
        MDVP_APQ = st.text_input('MDVP_APQ: Amplitude perturbation quotient (MDVP_APQ) of your voice?')
    with colp2:
        Shimmer_DDA = st.text_input(
            'Shimmer_DDA: Average absolute differences between consecutive cycles of amplitude perturbation (Shimmer_DDA)?')
    with colp1:
        NHR = st.text_input('NHR: Ratio of noise to harmonic components (NHR) in your voice?')
    with colp2:
        HNR = st.text_input('HNR: Harmonic-to-noise ratio (HNR) of your voice?')
    with colp1:
        RPDE = st.text_input('RPDE: Recurrence period density entropy (RPDE) of your voice?')
    with colp2:
        DFA = st.text_input('DFA: Detrended fluctuation analysis (DFA) of your voice?')
    with colp1:
        spread1 = st.text_input('Spread1: First spreading (spread1) of your voice data?')
    with colp2:
        spread2 = st.text_input('Spread2: Second spreading (spread2) of your voice data?')
    with colp1:
        D2 = st.text_input('D2: Nonlinear measure (D2) of fundamental frequency variation in your voice?')
    with colp2:
        PPE = st.text_input('PPE: Pitch period entropy (PPE) of your voice?')

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

# Breast Cancer classifier page
if (selected == 'Breast Cancer Classifier'):
    # page title
    st.title('Breast Cancer Classifier Using ML')

    # taking inputs from user
    # creating columns
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('Mean radius:')
        mean_texture = st.text_input('Mean texture:')
        mean_perimeter = st.text_input('Mean perimeter:')
        mean_smoothness = st.text_input('Mean smoothness:')
        mean_concavity = st.text_input('Mean concavity:')
        mean_symmetry = st.text_input('Mean symmetry:')
        radius_error = st.text_input('Radius error:')
        texture_error = st.text_input('Texture error:')
        perimeter_error = st.text_input('Perimeter error:')
        smoothness_error = st.text_input('Smoothness error:')


    with col2:
        concavity_error = st.text_input('Concavity error:')
        symmetry_error = st.text_input('Symmetry error:')
        worst_radius = st.text_input('Worst radius:')
        worst_texture = st.text_input('Worst texture:')
        worst_perimeter = st.text_input('Worst perimeter:')
        mean_area = st.text_input('Mean area:')
        mean_compactness = st.text_input('Mean compactness:')
        mean_concave_points = st.text_input('Mean concave points:')
        mean_fractal_dimension = st.text_input('Mean fractal dimension:')
        area_error = st.text_input('Area error:')

    with col3:
        compactness_error = st.text_input('Compactness error:')
        concave_points_error = st.text_input('Concave points error:')
        fractal_dimension_error = st.text_input('Fractal dimension error:')
        worst_area = st.text_input('Worst area:')
        worst_smoothness = st.text_input('Worst smoothness:')
        worst_compactness = st.text_input('Worst compactness:')
        worst_concavity = st.text_input('Worst concavity:')
        worst_concave_points = st.text_input('Worst concave points:')
        worst_symmetry = st.text_input('Worst symmetry:')
        worst_fractal_dimension = st.text_input('Worst fractal dimension:')

    # prediction variable
    breast_cancer_classifier = ''

    # creating a button for prediction
    if st.button('Classify Breast Cancer'):
        breast_cancer_prediction = breast_cancer_model.predict([[
    'mean_radius', 'mean_texture', 'mean_perimeter', 'mean_smoothness',
    'mean_concavity', 'mean_symmetry', 'radius_error', 'texture_error',
    'perimeter_error', 'smoothness_error', 'concavity_error', 'symmetry_error',
    'worst_radius', 'worst_texture', 'worst_perimeter', 'mean_area',
    'mean_compactness', 'mean_concave_points', 'mean_fractal_dimension',
    'area_error', 'compactness_error', 'concave_points_error',
    'fractal_dimension_error', 'worst_area', 'worst_smoothness',
    'worst_compactness', 'worst_concavity', 'worst_concave_points',
    'worst_symmetry', 'worst_fractal_dimension']])

        if(breast_cancer_prediction[0]==1):
            breast_cancer_classifier = 'The Breast cancer identified is Benign'
        else:
            breast_cancer_classifier = 'The Breast cancer identified is Malignant'
    st.success(breast_cancer_classifier)