# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:40:32 2019

@author: Omkar Nallagoni
"""




import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Item_Identifier,Item_Weight,Item_Fat_Content, Item_Visibility,
                                    Item_Type, Item_MRP, Outlet_Identifier, Outlet_Size,
                                         Outlet_Location_Type, Outlet_Type,Item_MRP2):
   
    prediction=classifier.predict([[Item_Identifier,Item_Weight,Item_Fat_Content, Item_Visibility,
                                    Item_Type, Item_MRP, Outlet_Identifier, Outlet_Size,
                                         Outlet_Location_Type, Outlet_Type,Item_MRP2]])
    print(prediction)
    return prediction



def main():
    st.title("Big Mart  outlet sales prediction quality")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bigmart salaes predict </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Item_Identifier = st.text_input("Item_Identifier","Type Here")
    Item_Weight = st.text_input("Item_Weight","Type Here")
    Item_Fat_Content = st.text_input("Item_Fat_Content","Type Here")
    Item_Visibility = st.text_input("Item_Visibility","Type Here")
    Item_Type = st.text_input("Item_Type","Type Here")
    Item_MRP  = st.text_input("Item_MRP","Type Here")
    Outlet_Identifier= st.text_input("Outlet_Identifier","Type Here")
    Outlet_Size = st.text_input("Outlet_Size","Type Here")
    Outlet_Location_Type= st.text_input("Outlet_Location_Type","Type Here")
    Outlet_Type = st.text_input("Outlet_Type","Type Here")
    Item_MRP2= st.text_input("Item_MRP2","Type Here")
    
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(Item_Identifier), eval(Item_Weight), eval(Item_Fat_Content), 
                                           eval(Item_Visibility),eval(Item_Type), eval(Item_MRP), 
                                           eval(Outlet_Identifier), eval(Outlet_Size),eval(Outlet_Location_Type),eval(Outlet_Type),eval(Item_MRP2))
        
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("This is about Bigmart outlet sales prediction Price Prediction")

if __name__=='__main__':
    main()
    
    
    