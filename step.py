import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(layout='wide')

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'
df_name = pd.read_csv(name_url)
st.image(logo_url)


st.dataframe(df_name) 


col1, col2 = st.columns(2)

with col1:

  st.subheader('Office')

  col11, col12 = st.columns(2)

  with col11:
    name_select = st.selectbox('Your name', office_list)

  with col12:
    daily_steps = st.number_input('Daily steps')


date = st.date_input('select date')

st.write(date)
