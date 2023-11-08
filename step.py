import pandas as pd
import streamlit as st
import numpy as np
import requests


st.set_page_config(layout='wide')


logo_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/INC_Step_Challenge.jpg'
name_url = 'https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'
name_url1 = 'https://raw.github.com/LucasMichaud2/INC_step/main/onsite_steps.csv'
think_tech = 'https://raw.github.com/LucasMichaud2/INC_step/main/Original%20on%20Transparent.png'
st.image(logo_url)


def formatting(url):
 df_office = pd.read_csv(url)
 df_office = pd.DataFrame(df_office)
 office_name = df_office['Office'].tolist()
 
 office_board = df_office[['Office', 'Steps']]
 one_day = df_office.drop('Steps', axis=1)
 one_day['Daily Steps'] = one_day.iloc[:, 1:].max(axis=1)
 one_day = one_day[['Office', 'Daily Steps']]
 temp_data = df_office.copy()
 col_to_drop = ['Office', 'Steps']
 temp_data = temp_data.drop(columns=col_to_drop)
 
 temp_data['Total Steps'] = temp_data.sum(axis=1)
 
 
 
 office_board['Steps'] = temp_data['Total Steps']
 office_board = office_board.sort_values(by='Steps', ascending=False)
 office_board = office_board.reset_index(drop=True)
 office_board.index = range(1, len(office_board) + 1)
 one_day = one_day.sort_values(by='Daily Steps', ascending=False)
 one_day = one_day.reset_index(drop=True)
 one_day.index = range(1, len(one_day) + 1)
 
 return office_board, one_day

office_board, office_day = formatting(name_url)
onsite_board, onsite_day = formatting(name_url1)


col1, col2 = st.columns(2)

with col1:
 st.subheader('Office', divider='grey')
 col11, col12 = st.columns(2)

 with col11:
  st.write('Overall Leaderboard')
  
       
  st.dataframe(office_board)

 with col12:
  st.write('Most Steps in a Day')
  st.dataframe(office_day)

with col2:
 st.subheader('On Site', divider='grey')
 col21, col22 = st.columns(2)
 with col21:
  st.write('Overall Leaderboard')
  
       
  st.dataframe(onsite_board)

 with col22:
  st.write('Most Steps in a Day')
  st.dataframe(onsite_day)
  st.write(' ')
  st.write(' ')
  st.write(' ')
  st.write(' ')
  st.write(' ')
  st.write(' ')
  st.write(' ')
  st.write(' ')
  st.image(think_tech)
  
 
