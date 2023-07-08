import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time
st.set_page_config(
    page_title="Multiple Disease Predictor",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="auto",
)

# Set the theme colors
st.markdown(
    """
    <style>
    :root {
        --primary-color: #B21F33;
        --background-color: #002b36;
        --secondary-background-color: #586e75;
        --text-color: #fafafa;
        --font: sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# loading the saved models

covid_model = pickle.load(open("covid.pkl", 'rb'))

heart_disease_model = pickle.load(open("heart.pkl",'rb'))

lungs_model = pickle.load(open("lung_cancer.pkl", 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Covid Prediction',
                           'Heart Disease Prediction',
                           'Lungs Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)


    
# CORONA Prediction Page
if (selected == 'Covid Prediction'):
    
    # page title
    st.title('Corona Prediction')
    
    
    # getting the input data from the user
    col1, col2= st.columns(2)
    
    with col1:
        cough = st.selectbox( 'Cough : 0 FOR NO, 1 FOR YES ',
          ('0', '1'))
    
    with col2:
        fever = st.selectbox( 'Fever: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col1:
       sore_throat =st.selectbox( 'Sore throat: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col2:
        shortness_of_breath = st.selectbox( 'Shortness of breath: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col1:
        head_ache = st.selectbox( 'Head ache: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col2:
        age_60_and_above = st.selectbox( 'Age 60 and above: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col1:
        gender = st.selectbox( 'Gender: 0 FOR M, 1 FOR F',
          ('0', '1'))
    
    with col2:
        test_indication = st.selectbox( 'Test indication: 0 FOR ABROAD, 1 FOR CONTACT, 2 FOR OTHER',
          ('0', '1','2'))
    
    
    # code for Prediction
    covid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Corona Test Result'):
        Covid_Prediction = covid_model.predict([[cough,fever,sore_throat,shortness_of_breath,head_ache,age_60_and_above,gender,test_indication]])
        
        if (Covid_Prediction[0] == 1):
          covid_diagnosis = 'The person has covid'
        else:
          covid_diagnosis = 'The person does not have covid'
        
    st.success(covid_diagnosis)




# # Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
#     # page title
     st.title('Heart Disease Prediction')
    
     col1, col2, col3 = st.columns(3)
    
     with col1:
        Age = st.slider("Choose your age: ", min_value=10,  max_value=99, value=35, step=1)
        
     with col2:
         Sex = st.selectbox( 'Sex : 0 FOR M, 1 FOR F',
          ('0', '1',))
        
     with col3:
         ChestPainType = st.selectbox( 'ChestPainType : ATA:0, NAP:1, ASY:2, TA:3',
          ('0', '1','2','3'))
        
     with col1:
         RestingBP = st.text_input('Resting Blood Pressure')
        
     with col2:
         Cholesterol = st.text_input('Serum Cholestoral in mg/dl')
        
     with col3:
         FastingBS =  st.text_input('FASTINGBS')
        
     with col1:
         RestingECG =st.selectbox( 'RestingECG Normal:0, ST:1, LVH:2',
          ('0', '1','2'))
        
     with col2:
         MaxHR = st.text_input('Maximum Heart Rate achieved')
        
     with col3:
         ExerciseAngina = st.selectbox( 'ExcerciseAngina N:0, Y:1',
          ('0', '1','2'))
        
     with col1:
         Oldpeak = st.text_input('Old peak')
        
     with col2:
         ST_Slope = st.selectbox( 'ST_Slope  Up:0, Down:1, Flat:2,',
          ('0', '1','2'))
        
        
     
     
#     # code for Prediction
     heart_diagnosis = ''
    
     # creating a button for Prediction
    
     if st.button('Heart Disease Test Result'):
         heart_prediction = heart_disease_model.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])                          
        
         if (heart_prediction[0] == 1):
           heart_diagnosis = 'The person is having heart disease'
         else:
           heart_diagnosis = 'The person does not have any heart disease'
        
     st.success(heart_diagnosis)
        
    
    

# # Parkinson's Prediction Page
if (selected == "Lungs Disease Prediction"):
    
#     # page title
     st.title("Lungs Disease Prediction")
    
     col1, col2, col3, col4, col5 = st.columns(5)  
    
     with col1:
         AGE = st.slider("Choose your age: ", min_value=10,  max_value=99, value=35, step=1)
        
     with col2:
         SMOKING = st.selectbox( 'Smoking :1 FOR NO, 2 FOR YES',
          ('1', '2'))
        
     with col3:
         YELLOW_FINGERS = st.selectbox( 'Yellow Fingers :1 FOR NO, 2 FOR YES',
          ('1', '2'))
        
     with col4:
         ANXIETY = st.selectbox( 'Anxiety :1 FOR NO, 2 FOR YES',
          ('1', '2'))
     with col5:
         PEER_PRESSURE = st.selectbox( 'Peer pressure :1 FOR NO, 2 FOR YES',
          ('1', '2'))
        
     with col1:
         CHRONICDISEASE= st.selectbox('Chronic disease :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col2:
         FATIGUE = st.selectbox('Fatigue :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col3:
         ALLERGY= st.selectbox('Allergy :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col4:
         WHEEZING= st.selectbox('Wheezing :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col5:
         ALCOHOLCONSUMING= st.selectbox('Alcohol consuming :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col1:
         COUGHING = st.selectbox('Coughing :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col2:
         SHORTNESSOFBREATH = st.selectbox('Shortness of breath :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col3:
         SWALLOWINGDIFFICULTY = st.selectbox('Swallow difficulty :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col4:
         CHESTPAIN= st.selectbox('Chest pain :1 FOR NO, 2 FOR YES',('1', '2'))
        
     with col5:
         M = st.selectbox( 'Sex :0 FOR F, 1 FOR M',
          ('0', '1',))
        

        
    
    
#     # code for Prediction
     lungs_diagnosis = ''
    
#     # creating a button for Prediction    
     if st.button("Lung Disease Test Result"):
         lungs_prediction = lungs_model.predict([[AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONICDISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOLCONSUMING,COUGHING,	SHORTNESSOFBREATH,	SWALLOWINGDIFFICULTY	,CHESTPAIN,	M]])
        
         if (lungs_prediction [0] == 1):
           lungs_diagnosis = "The person has Lungs disease"
         else:
           lungs_diagnosis = "The person does not have Lungs disease"
        
     st.success(lungs_diagnosis)
