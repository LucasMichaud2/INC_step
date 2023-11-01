import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(layout='wide')

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/namelist.csv'
df_name = pd.read_csv(name_url)
col_drop = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']
df_name = df_name.drop(columns=col_drop)
st.image(logo_url)

df_office = df_name[['OFFICE']].copy()
df_office['Steps'] = 0
df_site = df_name[['On site']].copy()
df_site = df_site.head(3)
df_site['Steps'] = 0
st.dataframe(df_office)
st.dataframe(df_site)

office_list = df_office['OFFICE'].tolist()


col1, col2 = st.columns(2)

with col1:

  name_select = st.selectbox('Your name', office_list)
