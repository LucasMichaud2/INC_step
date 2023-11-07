import pandas as pd
import streamlit as st
import numpy as np
import requests


st.set_page_config(layout='wide')

token = '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'

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'
df_office = pd.read_csv(name_url)
st.image(logo_url)
office_name = df_office['Office'].tolist()


st.dataframe(df_office) 
