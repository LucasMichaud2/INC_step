import os
import requests
import pandas as pd
import streamlit as st

# GitHub repository information
owner = "LucasMichaud2"
repo = "INC_step"
file_path = "https://raw.github.com/LucasMichaud2/INC_step/main/office_steps.csv"

# Read and update the CSV data
df = pd.read_csv(file_path)

with st.form("form1"):
# Your update logic here
  new_value = st.number_input('heelo')
  df['Steps'] = new_value
  submitted = st.form_submit_button("Submit")

if submitted:

  # Convert DataFrame back to CSV
  updated_csv = df.to_csv(index=False)
  
  # GitHub API endpoint
  url = f"https://api.github.com/repos/{owner}/{repo}/contents/'office_steps.csv'"
  
  # Prepare the request headers
  headers = {
      "Authorization": f"Bearer {os.environ['TOKEN']}",
  }
  
  # Prepare the request data
  data = {
      "message": "Update CSV file",
      "content": updated_csv,
  }
  
  # Send the PUT request to update the file
  response = requests.put(url, headers=headers, json=data)
  
  if response.status_code == 200:
      print("CSV file updated successfully on GitHub!")
  else:
      print(f"Failed to update CSV file on GitHub. Status code: {response.status_code}")
