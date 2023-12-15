import streamlit as st
import joblib
import pandas as pd


# Chargez le modèle
meilleur_modele = joblib.load('/home/chanez/documents/cloud/meilleur_modele_churn_prediction(1).joblib')
# compress the model
#ml = joblib.dump(meilleur_modele, '/home/chanez/documents/cloud/meilleur_modele_churn_prediction(1).joblib', compress=True)

# Function for churn prediction
def predict_churn(features):
    # Make sure the features are in the correct format
    features = pd.DataFrame([features])
    prediction = meilleur_modele.predict(features)
    return prediction[0]  # Extract the single prediction value from the array

# Interface utilisateur Streamlit
st.title('Application de prédiction du churn')

# Add Streamlit components for user inputs
CustomerID = st.number_input('CustomerID', min_value=0.0, max_value=100000.0, step=1.0)
tenure = st.number_input('Tenure', min_value=0.0, max_value=100.0, step=1.0)
CityTier = st.number_input('CityTier', min_value=1.0, max_value=3.0, step=1.0)
warehouse_to_home = st.number_input('WarehouseToHome', min_value=0.0, max_value=100.0, step=1.0)
hour_spend_on_app = st.number_input('HourSpendOnApp', min_value=0.0, max_value=24.0, step=0.5)

# Add input fields for other numerical features
number_of_devices_registered = st.number_input('NumberOfDeviceRegistered', min_value=0, step=1)
satisfaction_score = st.number_input('SatisfactionScore', min_value=1, max_value=5, step=1)
number_of_address = st.number_input('NumberOfAddress', min_value=0, step=1)
# Add other checkboxes for categorical features
Complain = st.checkbox('Complain') 
OrderAmountHikeFromlastYear =   st.number_input('OrderAmountHikeFromlastYear')
# Add input fields for categorical features (assuming they are encoded as binary)
CouponUsed =  st.checkbox('CouponUsed')
OrderCount = st.number_input('OrderCount')
DaySinceLastOrder = st.number_input('DaySinceLastOrder')
CashbackAmount = st.number_input('CashbackAmount')
PreferredPaymentMode_CC = st.checkbox('PreferredPaymentMode_CC')
PreferredPaymentMode_COD = st.checkbox('PreferredPaymentMode_COD')
PreferredPaymentMode_Cash_d = st.checkbox('PreferredPaymentMode_Cash on Delivery') 
PreferredPaymentMode_Credit_crd  = st.checkbox('PreferredPaymentMode_Credit Card') 
PreferredPaymentMode_E_wallet  = st.checkbox('PreferredPaymentMode_E wallet')         
PreferredPaymentMode_UPI =  st.checkbox('PreferredPaymentMode_UPI')
Gender_Female  = st.checkbox('Gender_Female')
Gender_Male  = st.checkbox('Gender_Male')
MaritalStatus_Divorced = st.checkbox('MaritalStatus_Divorced')
MaritalStatus_Married = st.checkbox('MaritalStatus_Married')
MaritalStatus_Single =   st.checkbox('MaritalStatus_Single')         
PreferedOrderCat_Fashion =  st.checkbox('PreferedOrderCat_Fashion')           
PreferedOrderCat_Grocery =  st.checkbox('PreferedOrderCat_Grocery')        
PreferedOrderCat_Laptop = st.checkbox('PreferedOrderCat_Laptop')
PreferedOrderCat_Mobile =    st.checkbox('PreferedOrderCat_Mobile') 
PreferedOrderCat_Mobile_ph =  st.checkbox('PreferedOrderCat_Mobile Phone ')       
PreferedOrderCat_Others =    st.checkbox('PreferedOrderCat_Others')
PreferredLoginDevice_Computer =  st.checkbox('PreferredLoginDevice_Computer')   
PreferredLoginDevice_Phone = st.checkbox('PreferredLoginDevice_Phone') 
PreferredLoginDevice_Mobile_Phone =  st.checkbox('PreferredLoginDevice_Mobile Phone')
PreferredPaymentMode_Debit_Card  =  st.checkbox('PreferredPaymentMode_Debit Card') 
# Obtain user input features
user_input = {
    'CustomerID': CustomerID,
    'Tenure': tenure,
    'CityTier': CityTier,
    'WarehouseToHome': warehouse_to_home,
    'HourSpendOnApp': hour_spend_on_app,
    'NumberOfDeviceRegistered': number_of_devices_registered,
    'SatisfactionScore': satisfaction_score,
    'NumberOfAddress': number_of_address,
    'Complain' : Complain ,
    'OrderAmountHikeFromlastYear': OrderAmountHikeFromlastYear ,
    'CouponUsed' : CouponUsed ,
    'OrderCount' : OrderCount ,
    'DaySinceLastOrder' : DaySinceLastOrder,
    'CashbackAmount' : CashbackAmount ,
    'PreferredPaymentMode_CC' : PreferredPaymentMode_CC,
    'PreferredPaymentMode_COD' :    PreferredPaymentMode_COD      ,        
    'PreferredPaymentMode_Cash on Delivery' :  PreferredPaymentMode_Cash_d , 
    'PreferredPaymentMode_Credit Card'   :      PreferredPaymentMode_Credit_crd , 
    'PreferredPaymentMode_Debit Card' :  PreferredPaymentMode_Debit_Card ,
    'PreferredPaymentMode_E wallet' : PreferredPaymentMode_E_wallet ,
    'PreferredPaymentMode_UPI'    :    PreferredPaymentMode_UPI,           
    'Gender_Female'    :     Gender_Female    ,                
    'Gender_Male'      :       Gender_Male    ,               
    'MaritalStatus_Divorced'  :   MaritalStatus_Divorced,                
    'MaritalStatus_Married'   :     MaritalStatus_Married,             
    'MaritalStatus_Single'    :     MaritalStatus_Single,              
    'PreferedOrderCat_Fashion' :   PreferedOrderCat_Fashion,               
    'PreferedOrderCat_Grocery' :     PreferedOrderCat_Grocery,           
    'PreferedOrderCat_Laptop & Accessory' :    PreferedOrderCat_Laptop,   
    'PreferedOrderCat_Mobile'      :     PreferedOrderCat_Mobile,       
    'PreferedOrderCat_Mobile Phone'  :   PreferedOrderCat_Mobile_ph,         
    'PreferedOrderCat_Others'        :   PreferedOrderCat_Others,        
    'PreferredLoginDevice_Computer'   :     PreferredLoginDevice_Computer,      
    'PreferredLoginDevice_Mobile Phone' : PreferredLoginDevice_Mobile_Phone,
    'PreferredLoginDevice_Phone'  :  PreferredLoginDevice_Phone 

}

if st.button('Prédire'):
    # Perform the prediction
    prediction = predict_churn(user_input)
    st.write('La Classe du churn est:', prediction)