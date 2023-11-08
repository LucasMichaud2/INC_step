import pandas as pd
import streamlit as st
import numpy as np
import requests


st.set_page_config(layout='wide')


logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'
df_office = pd.read_csv(name_url)
df_office = pd.DataFrame(df_office)
st.image(logo_url)
office_name = df_office['Office'].tolist()

office_board = df_office[['Office', 'Steps']]
st.dataframe(office_board) 
temp_data = df_office.copy()
col_to_drop = ['Office', 'Steps']
temp_data = temp_data.drop(columns=col_to_drop)

temp_data['Total Steps'] = temp_data.sum(axis=1)



office_board['Steps'] = temp_data['Total Steps']


col1, col2 = st.columns(2)

with col1:
 st.subheader('Office', divider='grey')
 col11, col12 = st.columns(2)

 with col11:
  st.write('Overall Leaderboard')
  office_board = office_board.sort_values(by='Steps', ascending=False)
  office_board = office_board.reset_index()
  office_board.index = range(1, len(office_board) + 1)
       
  st.dataframe(office_board)
