import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(layout='wide')

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'
df_office = pd.read_csv(name_url)
st.image(logo_url)
office_name = df_office['Office'].tolist()


st.dataframe(df_office) 


col1, col2 = st.columns(2)

with col1:

  st.subheader('Office')

  col11, col12 = st.columns(2)

  with col11:
    name_select = st.selectbox('Your name', office_name)

  with col12:
    daily_steps = st.number_input('Daily steps')


  date = st.date_input('select date')

st.write(date)

submitted = st.form_submit_button("Submit")

if submitted:
  

  df_office.loc[df_office['Office'] == name_select, date] = daily_steps
  
  st.dataframe(df_office)
