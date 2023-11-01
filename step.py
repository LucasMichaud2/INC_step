import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/namelist.csv'
df_name = pd.read_csv(name_url)
col_drop = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5']
df_name = df_name.drop(columns=col_drop)
st.image(logo_url)

df_office = df_name['OFFICE']
df_site = df_name['On Site']
st.dataframe(df_office)
st.dataframe(df_site)
