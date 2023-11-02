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

  with st.form("form1"):

    col11, col12 = st.columns(2)
  
    with col11:
      name_select = st.selectbox('Your name', office_name)
  
    with col12:
      daily_steps = st.number_input('Daily steps')
  
  
    date = st.date_input('select date')
    submitted = st.form_submit_button("Submit")
    

st.write(date)

if submitted:
  

  df_office.loc[df_office['Office'] == name_select, date] = daily_steps

  df_office.to_csv('https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv')

  import git

  repo = git.Repo('https://raw.github.com/LucasMichaud2/INC_step/main/')
  repo.index.add(['https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv'])
  repo.index.commit("Update CSV file")
  repo.remote().push()
    
  st.dataframe(df_office)
