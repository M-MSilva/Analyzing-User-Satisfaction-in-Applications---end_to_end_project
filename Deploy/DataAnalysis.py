
#imports
import streamlit as st
import os
from pathlib import Path
from wordcloud import WordCloud, STOPWORDS
import re
import sys
from nltk.util import ngrams 
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
import spacy
import seaborn as sns
from collections import Counter

#initialize the model using English
nlp = spacy.load("en_core_web_sm")

#take seaborn theme
sns.set_theme()
#Get current directory
current_directory = Path(__file__).parent



def Allfunctions():
  #we create a preprocessing function
  def preprocess(data):
      data = re.sub(r"<(?!br).*?>", " ",data)
      data = re.sub(r"[^a-zA-Z]", " ",data)
      return data

  #we create the function to return the ngrams
  def  topNgram(corpus, n=None) : 
      cVec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
      bag_words = cVec.transform(corpus)
      sum_words = bag_words.sum(axis= 0 )
      
      freq_of_words  = []
      for word, idx in cVec.vocabulary_.items():
        freq_of_words.append((word , sum_words[ 0 , idx]))
                    
      freq_of_words.sort(key=lambda tup: tup[1], reverse=True)
      return freq_of_words[:10]

  #we create a function that generates a doc variable, which contains an instance with the entities and from it we extract the entities
  def ner(text):
      doc=nlp(text, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
      return [u.label_ for u in doc.ents]

  #page title
  st.write("""
    <div >
      <br />
      <br />
      <br />
      <h4 class='h4title'> Exploratory Data Analysis:</h4>
      <br /> 
    </div>
  </div>""", unsafe_allow_html=True)
  
  #if the user has already made the criticism, we read the file with the criticism, otherwise we induce him to insert the criticism
  #when we have the review we show the user a button to create the data analysis
  try:
    with open(os.path.join(current_directory, 'dados.txt'), 'r') as file:
      critica = file.read()
      if not critica:
        raise ValueError('erro')
  except:
    critica = st.text_area(
              label='Make your review! (Please write in English)'
          )
  if(st.button('Generate Exploratory Analysis') and critica != ''):
    st.write("""
      <div >
        <br />
        <h4 class='h4title'> Most frequent words in the text:</h4>
        <br /> 
      </div>
    </div>""", unsafe_allow_html=True)

    #WE DO A LOT OF DATA PROCESSING
    data_without_sp = " ".join(critica.split())

    data_without_sp = preprocess(data_without_sp)

    datasemLowerv = data_without_sp.lower()

    stopwords = STOPWORDS
    stopwords.update(['game','it','app','t','s','m'])

    auxdata = ' '.join([word for word in datasemLowerv.split() if word not in (stopwords)])

    #we count the most common words in the data
    mostcommon_small = Counter(''.join(auxdata).split()).most_common(10)


    #we plot the first picture of the most frequent words
    col1, col2, col3= st.columns([1, 3, 1])
    with col2:
      for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#262730' 


      for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
        plt.rcParams[param] = '0.9' 

      #we take every word and its frequency
      words,freq = zip(*mostcommon_small)

      #we plot the figure in the form of a donut
      fig1, ax1 = plt.subplots()
      ax1.grid(color='#262730')
      ax1.pie(x=freq,labels=words,autopct='%1.0f%%',pctdistance=0.85)
      ax1.set_title('Most frequent words in criticism ')
      my_circle=plt.Circle( (0,0), 0.7, color='#262730')
      p=plt.gcf()
      p.gca().add_artist(my_circle)
      fig1.tight_layout()
      st.pyplot(fig1)
      
    #let's plot another figure now, so we enter a new title
    st.write("""
      <div >
        <br /><br /><br />
        <br /> <br /><br />  
        <br /><br /><br />
        <h4 class='h4title'> Bigrams Present in the Text:</h4>
        <br /> 
      </div>
    </div>""", unsafe_allow_html=True)

    #we write on the page what we are plotting
    st.write("""

    <div class="rectangle">

      <div class='formatexto'>
      <p class='mytext'>
        Ngram means strings of words found in the text, 
        for example a 2-gram = bigram may have the words 'wasted time'
        indicating a poor user experience in apps.
      </p> 
      </div>
    
    </div>  <br />""", unsafe_allow_html=True)

    #start plotting and data transformation
    col1, col2, col3= st.columns([1, 3, 1])
    with col2:


      #we scan our dataset to strip out the stopwords
      initdata = ' '.join([word for word in datasemLowerv.split() if word not in (stopwords)])

      #we create a list of initdata
      finaldata = [initdata]

      if(len(initdata.split()) > 10):

        #we call the topNgram function and take the top 10 positive bigrams in the lists xp,yp,
        xp,yp=map(list,zip(*topNgram(finaldata,2)[:10]))

        #we create a dataframe containing the above results
        dfngran = pd.DataFrame(list(zip(xp,yp)), columns = ['ngram','frequency'])
        
        #We create a figure with subplots,
        fig2, ax2 = plt.subplots( )


        #we sort the dataframe by frequency,
        dfngran.sort_values(by=['frequency'],inplace=True)

        #we plot the dataframe in the form of a horizontal bar.
        ax2.barh(dfngran['ngram'].values,dfngran['frequency'].values,color='#6b6e88')
        ax2.set_xlabel('Frequency')
        ax2.set_ylabel('Bigrams')
        ax2.set_title('Reviews Bigram')


        fig2.tight_layout()
        st.pyplot(fig2)
      else:
        st.info('Please enter a more detailed review, as with your meager review it is not possible to perform data analysis!')

    #we start the title of the last figure
    st.write("""
      <div >
        <br />
        <h4 class='h4title'> Named entity recognition:</h4>
        <br /> 
      </div>
    </div>""", unsafe_allow_html=True)

    #We explain what entities are
    st.write("""

    <div class="rectangle">

      <div class='formatexto'>
      <p class='mytext'>
        We can sort our text into some entities such as countries, buildings, dates, institutions, etc.
        Everything will be clearer with the example, right before anything we will glimpse all the entities 
        that the model can classify and their description.
      </p> 
      </div>
    
      <br />""", unsafe_allow_html=True)  

    #we put a title to illustrate examples of entities
    st.write("""
      <div >
        <br />
        <h4 class='h4title'> examples of entities:</h4>
        <br /> 
      </div>
      </div>""", unsafe_allow_html=True)
    

    #WE SHOW EXAMPLES OF POSSIBLE ENTITIES
    col1, col2, col3= st.columns([1, 3, 1])
    with col2:
    

      #we get the labels of all entities
      labels = nlp.get_pipe("ner").labels

      #we collect the description of each entity
      desc=[spacy.explain(i) for i in labels]

      #We create a dataframe
      mydf = pd.DataFrame({'Entity': labels,
          'Description': desc
          })
      #we transform the dataframe into html table
      st.table(mydf)

    #we inform you that we will start plotting our entities
    st.write("""
    <div >
      <h4 class='h4title'> Entities Found in Reviews:</h4>
      <br /> 
      </div>
    </div>""", unsafe_allow_html=True)
      
    #we plot our entities
    col1, col2, col3= st.columns([1, 3, 1])
    with col2:

      #aux step
      auxdata = str(finaldata)

      #we apply the ner function on the data
      entp=ner(auxdata)


      #we count the words, then we take the most common ones and finally we take the words and the word frequencies in two lists

      if len(entp) > 0:
        countp=Counter(entp)
        countp=Counter(entp).most_common()
        px, py = list(zip(*countp))[0], list(zip(*countp))[1]


        

        #we create dataframes with the entities and frequencies 
        dfm = pd.DataFrame(list(zip(px,py)), columns = ['Entity','frequency'])

        #we plot graphs with the percentage of each entity
        fig3, ax3 = plt.subplots()
        ax3.pie(dfm['frequency'].values,labels=dfm['Entity'].values,shadow=False, startangle=90,autopct='%1.0f%%',pctdistance=0.8)
        ax3.set_title('Entities in The Criticism',fontsize = 17)
        fig3.tight_layout()
        st.pyplot(fig3)
      else:
        st.info('Please enter a more detailed review, as with your meager review it is not possible to perform data analysis!')

  
    
