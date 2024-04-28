import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('new_data.csv')
st.set_page_config(layout='wide',page_title='ONWAY.COM')

def load_campany_analysis():
    pass
def load_country_analysis():
    pass
def load_jobstype_analysis():
    pass


st.title('WELCOME TO ONWAY HOPITALITY JOBS')

st.image('pexels-ricky-esquivel-1586298.jpg')

st.write('Welcome to our website, your gateway to the world of hospitality careers! Are you a beginner looking to kickstart your journey in the dynamic hospitality industry? Look no further! Our platform offers an exclusive focus on internships, apprenticeships, and trainee positions, making it the perfect starting point for individuals eager to dive into this exciting field.')

st.write('Whether you dream of managing a luxury hotel, crafting exquisite culinary creations, or orchestrating unforgettable events, our platform is designed to support your aspirations. Join us today and embark on your journey towards a fulfilling career in hospitality!')

st.write("Through innovative web scraping technology, we gather job opportunities from renowned platforms like Hosco, ensuring that you have access to the latest openings in the hospitality sector. But we don't stop there. Our website goes beyond mere listings – we empower you with the tools for data analysis, helping you make informed decisions about your career path.Whether you dream of managing a luxury hotel, crafting exquisite culinary creations, or orchestrating unforgettable events, our platform is designed to support your aspirations. Join us today and embark on your journey towards a fulfilling career in hospitality!")



st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('select one', ['Country-Wise Analysis', 'Company-Wise Analysis', 'Jobs Type Analysis'])

if option == 'Country-Wise Analysis':
    st.sidebar.selectbox('select Country', sorted(df.country.str.strip().unique().tolist()))
    btn0=st.sidebar.button('Countries analysis')


    if btn0:
        load_country_analysis()



elif option == 'Company-Wise Analysis':
    st.sidebar.selectbox('select Company', sorted(df.hotel_name.str.strip().unique().tolist()))
    btn1=st.sidebar.button('companies detail')


    if btn1:
        load_campany_analysis()
else:
    selected_investor=st.sidebar.selectbox('select Jobs Type', sorted(df.job_type.str.strip().unique().tolist()))
    btn2 = st.sidebar.button('Jobs Type Analysis ')
    if btn2:
        load_jobstype_analysis()


