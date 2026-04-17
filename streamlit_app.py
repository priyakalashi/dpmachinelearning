import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title('Penguin Species Prediction with Machine Learning')
st.header('Priya Kalashi')
st.info('We are going to predict penguin species based on the dataset using machine learning')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
st.write('**X**')
  X_raw = df.drop(columns='species',axis=1)
  

  
