import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/namelist.csv'
df_name = pd.read_csv(name_url)
st.image(logo_url)
st.dataframe(df_name)
