import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('new_data.csv')
st.set_page_config(layout='wide',page_title='ONWAY.COM')



st.title('WELCOME TO ONWAY HOPITALITY JOBS')

st.image('pexels-ricky-esquivel-1586298.jpg')

st.write('Welcome to our website, your gateway to the world of hospitality careers! Are you a beginner looking to kickstart your journey in the dynamic hospitality industry? Look no further! Our platform offers an exclusive focus on internships, apprenticeships, and trainee positions, making it the perfect starting point for individuals eager to dive into this exciting field.')

st.write('Whether you dream of managing a luxury hotel, crafting exquisite culinary creations, or orchestrating unforgettable events, our platform is designed to support your aspirations. Join us today and embark on your journey towards a fulfilling career in hospitality!')

st.write("Through innovative web scraping technology, we gather job opportunities from renowned platforms like Hosco, ensuring that you have access to the latest openings in the hospitality sector. But we don't stop there. Our website goes beyond mere listings – we empower you with the tools for data analysis, helping you make informed decisions about your career path.Whether you dream of managing a luxury hotel, crafting exquisite culinary creations, or orchestrating unforgettable events, our platform is designed to support your aspirations. Join us today and embark on your journey towards a fulfilling career in hospitality!")