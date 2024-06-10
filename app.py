import streamlit as st
import pandas as pd
from plotly import express as px
import seaborn as sns

# Load your DataFrame
df = pd.read_csv('new_data.csv')
df['country']=df.country.str.strip()
# Streamlit setup
st.set_page_config(layout='wide', page_title='ONWAY.COM')


# Define page functions
def load_home_page():
    st.title("Navigate Your Dreams: Onway.com")
    st.image('Hotel-jobs imga.jpg')
    st.write('Welcome to Hotels Jobs Analysis, your premier destination for insightful analysis and comprehensive information on careers within the hospitality industry.')
    st.write("Discovering the perfect job in the hotel sector can be a daunting task, but with our expertise and resources, we make it easier than ever. Whether you're a seasoned professional looking for new opportunities or just starting your career journey, our platform offers valuable insights to guide you every step of the way.")
    st.write("From entry-level positions to executive roles, we provide in-depth analysis of job trends, salary expectations, skill requirements, and career growth opportunities within the hotel industry. Our curated content helps you stay informed about the latest developments and industry best practices, ensuring you make informed decisions about your career path.")




def load_Project_page():
    st.title('WELCOME TO PROJECT PAGE ')


    box= st.selectbox('Select one',['Overall Analysis', 'Country_Wise Analysis', 'Jobs Analysis', 'Company_Wise Analysis'])


    if box == 'Overall Analysis':
        st.header('Overall Analysis')
        col1,col2=st.columns(2)

        with col1:
            st.subheader('Top 10 Companies give jobs offer')

            aa = df['hotel_name'].value_counts().head(10)  # Ensure 'hotel_name' is the correct column name
            fig = px.pie(aa, values=aa.values, names=aa.index)  # Use values for value sizes
            st.plotly_chart(fig)


        with col2:
            st.subheader('Jobs in which Country & Cities')
            ss = df[['country', 'city']].value_counts().reset_index(name='count')
            fig=px.sunburst(ss,path=['country','city'],values='count',color='count',range_color=[10, 100], color_continuous_scale='RdYlBu')
            st.plotly_chart(fig)


        col1,col2=st.columns(2)

        with col1:
            st.subheader('Job Type')


            job_type_column_name = 'job_type'

            # Calculate job_type counts
            aa1 = df[job_type_column_name].value_counts().reset_index(name='counts')

            # Create pie chart
            fig = px.pie(aa1, values='counts', names='index')  # Use 'index' for the job types
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

    elif box== 'Country_Wise Analysis':
        st.title('Country_Wise Analysis')

        st.header('Top 20 Countries have most jobs')
        aa2 = df.country.value_counts().head(20).reset_index(name='counts').rename(columns={'index': 'country'})
        fig=px.bar(aa2, x='country', y='counts', text_auto=True)
        fig.update_layout(width=1400,height=500)
        st.plotly_chart(fig)


        st.header('Top 20 Countries have most Jobs-Type')
        cc = df.country.value_counts(ascending=False).head(20).index.to_list()
        pivot = df[df['country'].isin(cc)].pivot_table(index='country', columns='job_type', aggfunc='size').fillna(
                '0')
        pivot = pivot.drop(columns=[' Part-time,Traineeship', ' Traineeship,Part-time'])

        pivot = pivot.stack()
        pivot = pivot.reset_index(name='counts')
        fig=px.bar(pivot, x='country', y='counts', color='job_type', barmode='group', text='counts', log_y=True,color_continuous_scale='viridis')
        fig.update_layout(width=1400,height=500)
        st.plotly_chart(fig)


        btn=st.selectbox('select one country',sorted(df.country.str.strip().unique().tolist()))
        st.title(btn)
        st.header('Types Of Jobs Available In This Country')

        col1,col2=st.columns(2)
        with col1:

            sd = df[df.country == btn]['job_type'].value_counts().reset_index(name='count').rename(
                columns={'index': 'job_type'})
            fig = px.bar(sd, x='job_type', y='count', text_auto=True)
            st.plotly_chart(fig)

        with col2:
            frame=df[df.country == btn]['job_type'].value_counts().reset_index(name='counts').rename(columns={'index': 'job type'})
            st.dataframe(frame)



        # Assuming df and btn are defined elsewhere

        col1, empty_col, col2 = st.columns(3)  # Adjust the ratio as needed

        with col1:
            st.header('Cities In This Country Have Jobs')
            ss = df[df.country == btn].city.value_counts().reset_index(name='counts').rename(
                columns={'index': 'city'}).head(20)
            fig = px.pie(ss, values='counts', names='city')
            st.plotly_chart(fig)

        with empty_col:
            pass  # This column will create the space between col1 and col2

        with col2:
            st.header('Hotel Names that Provide Jobs')
            ss = df[df['country'] == btn].hotel_name.value_counts().reset_index(name='counts').rename(
                columns={'index': 'country'})
            st.dataframe(ss)









    elif box == 'Jobs Analysis':
        st.title('Jobs Analysis')

        st.header('most jobs type')
        aa2 = df.job_type.value_counts().reset_index(name='counts').rename(columns={'index': 'job_type'})
        fig = px.bar(aa2, x='job_type', y='counts', text_auto=True)
        fig.update_layout(width=1400, height=500)
        st.plotly_chart(fig)

        st.header('top 40 Countries give most internship')
        cc = df.job_type.value_counts(ascending=False).head(1).index.to_list()
        pivot = df[df['job_type'].isin(cc)].pivot_table(index='job_type', columns='country', aggfunc='size').fillna('0')
        pivot = pivot.stack()
        pivot = pivot.reset_index(name='counts')
        pivot = pivot.sort_values(by='counts', ascending=False).head(40)
        fig=px.bar(pivot, x='job_type', y='counts', color='country', barmode='group', text='counts', log_y=True,
               color_continuous_scale='viridis')
        fig.update_layout(width=1400,height=500)
        st.plotly_chart(fig)



        st.header('top Countries give most Apprenticeship')
        cc = df[df.job_type == ' Apprenticeship'].job_type.value_counts(ascending=False).index.to_list()
        pivot = df[df['job_type'].isin(cc)].pivot_table(index='job_type', columns='country', aggfunc='size').fillna('0')
        pivot = pivot.stack()
        pivot = pivot.reset_index(name='counts')
        pivot = pivot.sort_values(by='counts', ascending=False).head(40)
        fig=px.bar(pivot, x='job_type', y='counts', color='country', barmode='group', text='counts', log_y=True, color_continuous_scale='viridis')
        fig.update_layout(width=1400,height=500)
        st.plotly_chart(fig)






    else:
        st.header('Company_Wise Analysis')

        st.header('Top 20 Companies have most jobs')
        aa2 = df.hotel_name.value_counts().head(20).reset_index(name='counts').rename(columns={'index': 'Company'})
        fig = px.bar(aa2, x='Company', y='counts', text_auto=True)
        fig.update_layout(width=1400, height=500)
        st.plotly_chart(fig)


        st.header('Top 20 Comppanies have most Jobs-Type')
        cc = df.hotel_name.value_counts(ascending=False).head(20).index.to_list()
        pivot = df[df['hotel_name'].isin(cc)].pivot_table(index='hotel_name', columns='job_type', aggfunc='size').fillna(
            '0')
        pivot = pivot.drop(columns=[' Part-time,Traineeship', ' Traineeship,Part-time'])

        pivot = pivot.stack()
        pivot = pivot.reset_index(name='counts')
        fig = px.bar(pivot, x='hotel_name', y='counts', color='job_type', barmode='group', text='counts', log_y=True,
                     color_continuous_scale='viridis')
        fig.update_layout(width=1400, height=500)
        st.plotly_chart(fig)




        btn=st.selectbox('select one Company',sorted(df.hotel_name.str.strip().unique().tolist()))
        st.title(btn)
        st.header('Types Of Jobs Available In This Company')

        col1,col2=st.columns(2)
        with col1:

            sd = df[df.hotel_name == btn]['job_type'].value_counts().reset_index(name='count').rename(
                columns={'index': 'job type'})
            fig = px.bar(sd, x='job type', y='count', text_auto=True)
            st.plotly_chart(fig)

        with col2:
            frame=df[df.hotel_name == btn]['job_type'].value_counts().reset_index(name='counts').rename(columns={'index': 'job type'})
            st.dataframe(frame)


        col1,col2=st.columns(2)
        with col1:
            st.header('Cities Name Where The Jobs Is Available')
            ss = df[df.hotel_name == btn].city.value_counts().reset_index(name='counts').rename(
                columns={'index': 'hotel_name'}).head(20)
            fig = px.pie(ss, values='counts', names='hotel_name')
            fig.update_layout(width=500, height=400)
            st.plotly_chart(fig)

        with col2:
            st.header('Country Name Where The Jobs Is Available')
            ss = df[df.hotel_name == btn].country.value_counts().reset_index(name='counts').rename(
                columns={'index': 'country'}).head(20)
            fig = px.pie(ss, values='counts', names='country')
            fig.update_layout(width=500, height=400)
            st.plotly_chart(fig)


def load_about_page():
    st.title('Mapping the Job Market: An In-Depth Analysis of Hosco Job Listings')
    st.write("In the age of digital transformation, data analysis has become a pivotal tool for making informed decisions across various domains. Our project embarks on this journey by leveraging advanced data scraping and analysis techniques to derive meaningful insights from the Hosco website. Hosco, a prominent platform in the hospitality industry, provides a wealth of information that can be harnessed to understand trends, patterns, and opportunities within the sector.")

    st.write("The project initiates with web scraping, utilizing Selenium to automate the process of extracting data from the Hosco website. Selenium's robust automation capabilities enable us to navigate the website efficiently, ensuring comprehensive data collection. Following the data acquisition, Beautiful Soup is employed to parse the HTML content, extracting relevant data encapsulated within the web pages.")

    st.write("With the raw data at hand, we proceed to the crucial phase of data cleaning. This step involves meticulous processing to remove inconsistencies, handle missing values, and standardize the dataset, ensuring its readiness for analysis. Leveraging the powerful functionalities of the Pandas library, we conduct a thorough examination and manipulation of the data, preparing it for subsequent analytical procedures.")

    st.write("The analysis phase employs Plotly and Seaborn libraries to visualize the data. Plotly's interactive visualizations, combined with Seaborn's statistical plotting capabilities, facilitate an in-depth exploration of the dataset. Through these visualizations, we can identify trends, outliers, and significant patterns, providing a comprehensive understanding of the underlying data.")

    st.write("To present our findings and make the analysis accessible, we utilize Streamlit, an open-source app framework. Streamlit allows us to create an intuitive and interactive web application, showcasing our data analysis project in a user-friendly manner. This dynamic interface not only presents our insights effectively but also enables stakeholders to interact with the data, fostering a deeper engagement with the analysis.")

    st.subheader("summary")
    st.write("This project exemplifies the integration of modern data scraping, cleaning, and analysis techniques, culminating in an interactive and insightful presentation through Streamlit. By extracting and analyzing data from the Hosco website, we aim to deliver valuable insights into the hospitality industry, demonstrating the power of data-driven decision-making.")
def load_contact_page():

    st.subheader('Contact -')

    st.markdown('https://github.com/AmitNegiOnway')
    st.markdown('https://public.tableau.com/app/profile/amit.negi4750/vizzes')
    st.markdown('amitnegionway@gmail.com')

option = st.sidebar.selectbox('select one', ['Home Page', 'Project', 'About','Contact'])

# Routing logic

if option == 'Home Page':
    load_home_page()

elif option == 'Project':
    load_Project_page()

elif option == 'About':
    load_about_page()

else:
    load_contact_page()