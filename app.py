# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:09:38 2023

@author: MMMutua
"""
import streamlit as st
import pickle
import numpy as np

#Load model that was initially trained and saved as a pkl file
file = open('model_pickle.pkl', 'rb')
price_model = pickle.load(file)



def price_range_prediction(input_data):
    
    #Change input data into numpy array
    input_data_array=np.asarray(input_data)
    
    #Reshape the array given that we will be predicting for only one case
    input_data_reshaped = input_data_array.reshape(1,-1)
    
    #prediction using loaded model
    prediction = price_model.predict(input_data_reshaped)
    
    #Adding class name to make it readable & understandable
    if (prediction[0] == 0):
        return 'Price range =  LOW COST'
    elif (prediction[0] == 1):
        return 'Price range =  MEDIUM COST'
    elif (prediction[0] == 2):
        return 'Price range =  HIGH COST'
    else:
        return 'Price range = VERY HIGH COST'



# Use streamlight to build user interface
def main():
    #create a title
    st.title("Mobile Phone Price Range Estimation Model")
    
    #User to enter the values for different features
    s_battery = st.slider('Select Battery power in mAh', 500,2000,1)
    s_ram = st.slider('Select RAM size - Mbs ', 250,3000,50)
    s_px_height = st.slider('Select Pixel resolution height ', 0,200,5)
    s_px_width = st.slider('Select Pixel resolution width ', 0,200,5)
    s_mobile_wt = st.slider('Select mobile weight in grams ', 50,200,1)
    s_memory = st.slider('Select internal memory size - GB', 0,20,1)
    s_fc = st.slider('Select Front Camera MegaPixels ', 0,20,1)
    s_pc = st.slider('Select primary camera MegaPixes ', 0,20,1)
    s_sc_h = st.slider('Select screen height Cms ', 0,20,1)
    s_sc_w = st.slider('Select screen width Cms ', 0,20,1)
    s_talk_time = st.slider('Select estimated longest time a battery takes hrs ', 0,20,1)
    s_n_cores = st.slider('Select number of processor cores ', 1,10,1)
    s_blue = st.slider('Has Bluetooth? N=0, Y=1 ', 0,1)
    s_clock = st.slider('Select Clock Speed ', 0.0,3.0,0.5)
    s_dual = st.slider('Has dual SIM slot N=0, Y=1 ', 0,1)
    s_three_g = st.slider('Supports 3G N=0, Y=1 ', 0,1)
    s_four_g = st.slider('Supports 4G N=0, Y=1 ', 0,1)
    s_touch = st.slider('Is a touch screen? 3G N=0, Y=1 ', 0,1)
    s_wifi = st.slider('Supports Wifi N=0, Y=1 ', 0,1)
    s_m_dep = st.slider('Select mobile depth in cms ', 0.0,1.0,0.1)
    

    #Define input features for prediction
    inputs = [s_battery,s_blue,s_clock,s_dual,s_fc,
           s_four_g,s_memory,s_m_dep,s_mobile_wt,
           s_n_cores,s_pc,s_px_height,s_px_width, s_ram,s_sc_h,
           s_sc_w,s_talk_time,s_three_g, s_touch, s_wifi]

    #code for price prediction
    price = ''
    
    #create button for Estimating price
    if st.button('Estimate Phone Price Range'):
        price = price_range_prediction(inputs)
        
    st.success(price)
    
if __name__ == '__main__':
    main()
        
