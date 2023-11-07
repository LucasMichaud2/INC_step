import pandas as pd
import streamlit as st
import numpy as np
import requests


st.set_page_config(layout='wide')

token = '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'

logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'
df_office = pd.read_csv(name_url)
df_office = pd.DataFrame(df_office)
st.image(logo_url)
office_name = df_office['Office'].tolist()
st.dataframe(df_office) 

office_board=df_office[['Office', 'Steps']]
temp_data = df_office.copy()
col_to_drop = ['Office', 'Steps']
temp_data = temp_data.drop(columns=col_to_drop)

temp_data['Total Steps'] = temp_data.sum(axis=1)

office_boards['Steps'] = temp_data['Total Steps']


st.dataframe(df_office) 

st.dataframe(office_board)
