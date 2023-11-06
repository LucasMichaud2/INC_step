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

  csv_data = df_office.to_csv()

  headers = {
    "Authorization": "token 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",
    "Content-Type": "application/json",
  }

  sha_url = "https://api.github.com/repos/LucasMichaud2/INC_step/contents/office_steps.csv"
  sha_response = requests.get(sha_url, headers=headers)
  st.write(sha_response)

  if sha_response.status_code == 200:
    sha = sha_response.json().get("sha")

    payload = {
      "message": "Update CSV file",
      "content": csv_data,
      "sha": "peuneogJjUumOnbZdb52zZbp10ZbcrDYwyyUZ+7hE1Y",
    }

    update_url = "https://api.github.com/repos/LucasMichaud2/INC_step/contents/office_steps.csv"
    response = requests.put(update_url, headers=headers,  json=payload)


    if response.status_code == 200:
      st.success("CSV file updated succesfully on Github!")
  
    else:
      st.error("Failed to update CSV file on Github.")

  else:
    st.error("Failed retrieve Sha")

st.dataframe(df_office)
