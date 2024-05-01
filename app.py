import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('new_data1.csv')
finall=df[df.job_type.str.contains('Full-time,Traineeship')]
finall['job_type']=finall['job_type'].str.replace('Full-time,Traineeship','Full time Traineeship')
df.loc[finall.index,'job_type']=finall['job_type']

finall=df[df.job_type.str.contains('Traineeship,Full-time')]
finall['job_type']=finall['job_type'].str.replace('Traineeship,Full-time','Full time Traineeship')
df.loc[finall.index,'job_type']=finall['job_type']



st.set_page_config(layout='wide',page_title='ONWAY.COM')
def load_home_page():
    st.title('WELCOME TO HOME PAGE')

def load_Project_page():
    st.title('WELCOMR TO PROJECT PAGE ')

def load_contact_page():
    st.title('WELCOME TO CONTACT PAGE')



st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('select one',['Home Page', 'Project', 'contact'])



if option == 'Home Page':
    btn0=st.sidebar.button('Select the above page')
    if btn0:
        load_home_page()

elif option == 'Project':
    btn1=st.sidebar.button('Select the above page')
    if btn1:
        load_Project_page()

else:
    btn2 = st.sidebar.button('Select the above page')
    if btn2:
        load_contact_page()


