import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("xgboost_model.pkl")

# Define pages
st.sidebar.title("Bank Marketing Prediction")
page = st.sidebar.selectbox(
    "Navigation",
    ["About", "Prediction", "Visualization"]
)

# About Page
if page == "About":
    st.title("Bank Marketing Prediction App")
    # st.image("subfolder/logo.png", caption="Bank Marketing Prediction")
    st.subheader("About this App")
    st.write(
        "This app is designed to help banks predict whether a customer will subscribe to a term deposit based on their profile data. Simply input a customer's details, and the app provides a prediction along with key insights into factors influencing the decision."
    )
    
    st.subheader("Features")
    st.write("Enter the following details to get a prediction:")
    st.write(
        "1. **Age**: Customer's age (numeric).\n"
        "2. **Job**: Type of job (e.g., admin, management, technician).\n"
        "3. **Marital Status**: Customer's marital status (e.g., married, single).\n"
        "4. **Education**: Level of education (e.g., primary, secondary).\n"
        "5. **Default**: Does the customer have credit in default? (yes/no).\n"
        "6. **Balance**: Average yearly balance, in euros (numeric).\n"
        "7. **Housing Loan**: Does the customer have a housing loan? (yes/no).\n"
        "8. **Personal Loan**: Does the customer have a personal loan? (yes/no).\n"
        "9. **Contact Method**: Communication type (e.g., telephone, cellular).\n"
        "10. **Day**: Last contact day of the month (numeric).\n"
        "11. **Month**: Last contact month of the year (e.g., jan, feb).\n"
        "12. **Duration**: Duration of last contact in seconds (numeric).\n"
        "13. **Campaign**: Number of contacts during this campaign (numeric).\n"
        "14. **Pdays**: Days passed since last contact (numeric; -1 if not contacted).\n"
        "15. **Previous**: Number of previous contacts (numeric).\n"
        "16. **Poutcome**: Outcome of the previous campaign (e.g., success, failure)."
    )
    
    st.subheader("Visualization")
    st.write(
        "The app provides graphical insights including conversion rates, age group analysis, contact method efficiency, and education level performance."
    )
    
    st.subheader("How to Use")
    st.write(
        "1. Navigate to the **Prediction** page and fill in all the fields with the appropriate customer details.\n"
        "2. Click on the **Predict** button to see the prediction result.\n"
        "3. Navigate to the **Visualization** page to explore the interactive dashboard showing detailed insights."
    )

# Prediction Page
elif page == "Prediction":
    st.title("Customer Subscription Prediction")

    # Input fields
    st.subheader("Enter Customer Details")
    
    # Indexed Input Fields
    age = st.number_input("1. Age", min_value=18, max_value=100, step=1)
    balance = st.number_input("2. Balance", step=100)
    day = st.number_input("10. Last Contact Day", min_value=1, max_value=31)
    duration = st.number_input("12. Duration (in seconds)")
    campaign = st.number_input("13. Campaigns", step=1)
    pdays = st.number_input("14. Days Since Last Contact", step=1)
    previous = st.number_input("15. Previous Contacts", step=1)
    
    job = st.selectbox("2. Job", [
        "Student", "Retired", "Unemployed", "Admin", "Management", "Technician", 
        "Self-Employed", "Housemaid", "Entrepreneur", "Services", "Blue-Collar"
    ])
    marital = st.selectbox("3. Marital Status", ["Married", "Single", "Divorced"])
    education = st.selectbox("4. Education", [
        "Illiterate", "University", "Professional", "High School", 
        "Basic (4 Years)", "Basic (6 Years)", "Basic (9 Years)"
    ])
    default = st.selectbox("5. Default", ["Yes", "No"])
    housing = st.selectbox("7. Housing Loan", ["Yes", "No"])
    loan = st.selectbox("8. Personal Loan", ["Yes", "No"])
    contact = st.selectbox("9. Contact Method", ["Cellular", "Telephone", "Unknown"])
    month = st.selectbox("11. Month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    poutcome = st.selectbox("16. Previous Outcome", ["Success", "Failure", "Other", "Unknown"])
    
    # Prediction Button
    if st.button("Predict"):
        input_data = {
            'age': [age], 'job': [job], 'marital': [marital],
            'education': [education], 'default': [default], 'balance': [balance],
            'housing': [housing], 'loan': [loan], 'contact': [contact],
            'day': [day], 'month': [month], 'duration': [duration],
            'campaign': [campaign], 'pdays': [pdays], 'previous': [previous],
            'poutcome': [poutcome]
        }
        input_df = pd.DataFrame(input_data)
        
        # Prediction Logic
        categorical_columns = input_df.select_dtypes(include=['object']).columns
        input_encoded = pd.get_dummies(input_df, columns=categorical_columns)
        training_features = model.get_booster().feature_names
        for feature in set(training_features) - set(input_encoded.columns):
            input_encoded[feature] = 0
        input_encoded = input_encoded[training_features]
        prediction = model.predict(input_encoded)[0]
        result_text = "Likely to subscribe." if prediction == 1 else "Unlikely to subscribe."
        st.success(f"Prediction: {result_text}")

# Visualization Page
elif page == "Visualization":
    st.title("Bank Marketing Campaign Dashboard")
    st.markdown(
        """
        <iframe title="EDA Dashboard" width="100%" height="500" 
        src="https://app.powerbi.com/view?r=eyJrIjoiNGE2MzUxNTUtM2Q3ZC00NDdlLTg0MjYtOTdjNTU0YzBlNWNhIiwidCI6ImMyYWYwODk3LWYwNWYtNDZiMy04ODY1LTVjYTNkOTFlOTMyYyIsImMiOjl9" 
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True
    )
