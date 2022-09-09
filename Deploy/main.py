
#imports
import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow  import keras
import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from preprocessing import custom_standardization
import base64
import SentimentAnalysisApp as WebApp
import DataAnalysis
from pathlib import Path


#we select wide mode for the screen
st.set_page_config(layout="wide")


#Get current directory
current_directory = Path(__file__).parent 

 
#we get the css file
with open(os.path.join(current_directory, 'style.css')) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)



#we clear the local image
st.markdown(
      f"""
      <style>
      .stApp {{
          background: url(data:image/{"jpg"};base64,{base64.b64encode( open(os.path.join(current_directory, "imgFundo.jpg"), 'rb').read()).decode()});
          background-repeat: no-repeat;
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )



#create the menu contendo o aplicativo e uma análise exploratória de dados
st.sidebar.write('<h1 style = "color:#ded5d5;"> MENU</h1>', unsafe_allow_html=True)
Page_user = st.sidebar.selectbox(

'Choice',['Sentiment Analysis App','Exploratory Data Analysis'] 
 
)


#we write the page title
st.write('<h1 style = "color:white;text-align: center;"> Analyzing user satisfaction in apps - App</h1>', unsafe_allow_html=True)


#we took the banner image
image = Image.open(os.path.join(current_directory, "imgBanner.png"))

#we show the banner image on the page
st.image(image)

#we put a line below the banner
st.markdown("""<hr style="height:8px;border:none;color:#B1A9A8;background-color:#B1A9A8; margin-botton:-20px;" /> """, unsafe_allow_html=True)


#to show my name and my social networks I put each of this information in columns
ctitle,c1,c2,c3,pa2 = st.columns([10,2,2,2,2])

with ctitle:
  st.write('<h4 class="h4title"> Developed by: Marcos Matheus de Paiva Silva</h4>', unsafe_allow_html=True)


with c1:
  st.write("""
          <div style='text-align: center;'>
          <a href='https://www.linkedin.com/in/marcos-matheus-silva-089699b3/'><img src='https://icon-library.com/images/linkedin-social-media-icon/linkedin-social-media-icon-8.jpg' 
           width='60' height='60'></a>
          </div>""", unsafe_allow_html=True)

with c2:
  st.write("""
            <div style='text-align: center;'>
            <a href='https://github.com/M-MSilva'><img src='https://icon-library.com/images/github-logo-icon/github-logo-icon-12.jpg' 
             width='60' height='60'></a>
            </div>""", unsafe_allow_html=True)
 
with c3:
  st.write("""
            <div style='text-align: center;'>
            <a href='silvamarcosxd@gmail.com'><img src='https://icon-library.com/images/gmail-email-icon/gmail-email-icon-19.jpg' 
             width='60' height='60'></a>
            </div>""", unsafe_allow_html=True)


#change the pages
if Page_user == 'Sentiment Analysis App':
    WebApp.code()

if Page_user == 'Exploratory Data Analysis':
    DataAnalysis.Allfunctions()
