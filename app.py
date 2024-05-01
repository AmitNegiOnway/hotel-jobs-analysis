import streamlit as st
import pandas as pd
from plotly import express as px
import seaborn as sns

# Load your DataFrame
df = pd.read_csv('new_data.csv')

# Streamlit setup
st.set_page_config(layout='wide', page_title='ONWAY.COM')


# Define page functions
def load_home_page():
    st.title('WELCOME TO HOME PAGE')


def load_Project_page():
    st.title('WELCOME TO PROJECT PAGE ')

    box = st.selectbox('Select one',
                       ['Overall Analysis', 'Country_Wise Analysis', 'Jobs Analysis', 'Company_Wise Analysis'])


    if box == 'Overall Analysis':
        st.header('Overall Analysis')
        col1,col2=st.columns(2)

        with col1:

            st.subheader('Top 10 Companies give jobs offer')
            aa = df['hotel_name'].value_counts().head(10)  # Ensure 'hotel_name' is the correct column name
            fig = px.pie(aa, values='count', names=aa.index)  # Use 'count' for value sizes
            st.plotly_chart(fig)

        with col2:
            st.subheader('Jobs in which Country & Cities')
            ss = df[['country', 'city']].value_counts().reset_index(name='count')
            fig=px.sunburst(ss,path=['country','city'],values='count',color='count',range_color=[10, 100], color_continuous_scale='RdYlBu')
            st.plotly_chart(fig)


        col1,col2=st.columns(2)

        with col1:
            st.subheader('Job Type')
            aa1 = df.job_type.value_counts().reset_index(name='counts')
            fig=px.pie(aa1,values='counts',names='job_type')
            st.plotly_chart(fig)


        with col2:
            st.subheader('Jobs Type in Countries and Their Cities')
            sa = df[['country', 'city', 'job_type']].value_counts().reset_index(name='counts')
            fig= px.sunburst(sa, path=['country', 'job_type', 'city'], values='counts', color='counts',range_color=[10, 100], color_continuous_scale='Viridis')
            st.plotly_chart(fig)


        st.title('Job Type All Over The world')

        dd = df[['country', 'job_type', 'job_title']].value_counts().reset_index(name='counts')
        fig=px.treemap(dd, path=[px.Constant('world'), 'country', 'job_type'], values='counts', color='counts',color_continuous_scale='thermal')
        fig.update_layout(width=1400, height=600)
        st.plotly_chart(fig)






    elif box == 'Country_Wise Analysis':
        st.header('Country_Wise Analysis')

    elif box == 'Jobs Analysis':
        st.header('Jobs Analysis')

    else:
        st.header('Company_Wise Analysis')


def load_contact_page():
    st.title('WELCOME TO CONTACT PAGE')


# Sidebar
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('select one', ['Home Page', 'Project', 'contact'])

# Routing logic
if option == 'Home Page':
    load_home_page()

elif option == 'Project':
    load_Project_page()

else:
    load_contact_page()
