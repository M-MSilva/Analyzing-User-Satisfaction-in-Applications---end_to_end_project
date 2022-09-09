
#imports
import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow  import keras
import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from preprocessing import custom_standardization
from pathlib import Path
import zipfile

#we create a function to be called in the main file
def code():

  #we create the function to say if the individual is happy or not
  def sentment_prediction(input_data,app):

    if(FinalModel.predict(input_data) > 0.5):
      return ' 😊 User is satisfied with ' + app + ' app 😊'
    else:
      return '😒 User is NOT satisfied with ' + app + ' app 😒'

  #we start the title of what the app does
  st.write("""
    <div >
      <br />
      <h4 class='h4title'> Sentiment Analysis App:</h4>
      <br /> 
    </div>
  </div>""", unsafe_allow_html=True)

  #we write a brief description of the application
  st.write("""
  <div class="rectangle">
    <div class='formatexto'>
    <p class='mytext'>
      This is a web application built on Streamlit,
      whose main objective is to perform a sentiment analysis of users in 
      mobile applications, that is, when the user criticizes an application in this 
      environment, we can inform if the user is satisfied or not with what he is assessing.
      In this project, we deal with a Natural Language problem using neural networks.
    </p> 
    </div>
  </div>  <br />""", unsafe_allow_html=True)


  #app name to be entered by the user
  app = st.text_input('What is the name of the APP you want to criticize?')
  
  #criticism that the user will make
  critica = st.text_area(
              label='Make your review! (Please write in English)'
          )


  #Get current directory
  current_directory = Path(__file__).parent 
  
  #we open the file with the review
  with open(os.path.join(current_directory, "dados.txt"), 'w') as f:
    f.write(critica)

  #we extract the zipped model
  model_path = os.path.join(current_directory, "mymodelZipado.zip")
  archive = zipfile.ZipFile(model_path, 'r')
  archive.extractall()

  #we get the directory with the model
  FinalModel = keras.models.load_model(os.path.join(current_directory, "final_model.tf"))


  #we take an example of criticism
  sample_text = tf.expand_dims([critica],-1)


  #we create a condition for prediction
  Condition = ''

  #if the application name is entered by the user, then we can run the code
  if(app!=''):

    #in case we have the criticism and everything is ok with the button we carry out the prediction 
    if st.button('Generate Result') and critica!='':
        Condition = sentment_prediction(sample_text,app)

    st.success(Condition)
  else:
    st.info('Please enter the review and the name of the app you would like to review!')
