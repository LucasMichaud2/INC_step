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

  col11, col12 = st.columns(2)

  with col11:
    name_select = st.selectbox('Your name', office_name)

  with col12:
    daily_steps = st.number_input('Daily steps')


  date = st.date_input('select date')

st.write(date)



# Create a form using st.form
with st.form("my_form"):
    # Add a text input field for the user to enter a name
    name = st.text_input("Enter your name")

    # Add a submit button
    submitted = st.form_submit_button("Submit")

# Check if the "Submit" button was clicked
if submitted:
    # Display a message with the submitted name
    st.write(f"Hello, {name}!")

# You can also add more form elements here if needed

# Display the result


  

df_office.loc[df_office['Office'] == name_select, date] = daily_steps
  
st.dataframe(df_office)
