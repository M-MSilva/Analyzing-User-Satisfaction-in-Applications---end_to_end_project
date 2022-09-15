# UNDER CONSTRUCTION

# Analyzing-User-Satisfaction-in-Applications_end-to-end

https://user-images.githubusercontent.com/92632851/190245479-a2556841-d559-44e8-b73b-9f96fc97bc0e.mp4

## Important notes about the project

This project was built with numerous tools and technologies, this is a summary document. So if you want more statistical and computational information see [jupyter Notebook](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/blob/main/jupyterNotebook/Analyzing_User_Satisfaction_in_ApplicationsNotebook.ipynb), to read about the conclusions found about the project, review the [Report](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/blob/main/Report/Report_Sentiment_Analysis__Marcos_Matheus.pdf), you can also access the application created in [Deploy](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/tree/main/Deploy ). My initial goal was to create a model to classify a user's sentiment as good, neutral or bad, but I turned the problem into a binary (good or bad). We don't divide the labels into positive, neutral and negative, because the code is too slow and bad, since we must apply several techniques for multi-class classification, such as Flatten and BatchNormalization layers. In the video above I use martin luther king's speech to create the font graphics: [Speech by Martin Luther King, Jr](https://www.americanrhetoric.com/speeches/mlkihaveadream.htm). :hugs:

## About this project

The purpose of this project is to classify whether or not a user is satisfied with a google play app, based on their review, that is, we basically predict whether or not the user likes a google play app through their review. Furthermore, this is a complete project as we go through several steps of a usual data science project such as data collection, feature engineering, data cleansing, data transformation, data visualization, data analysis, modeling and deployment.

## Applications 

Through this project we automate the analysis of user feedback, as we are also able to use such a project to create the classification of an application, when the user does not do so, but only performs the comment. From this project we will be able in the future to create a customer support management, based on your comment. In fact, my project can be generalized to be used in chat ratings, survey response analysis, market research, and tracking app reputation. :call_me_hand:

## Motivation
This project was developed to be part of my personal portfolio and it served both to test my skills and for my learning, since we used numerous technologies in it. Despite being an end-to-end project, it still needs some future improvements, such as having a larger and more diverse dataset. :smiley:

## Functionalities

### Developed Web APPs:

* Enter the application name and comment;
* Find out a user's satisfaction level;
* Create an exploratory data analysis containing the most frequent words, bigrams and entities named in the review (if the review is robust and very detailed).



## Instructions to run and/or compile the code

### Initial Requirements

The application is already running and it is not necessary to install anything on your machine, however, if you want to run the application locally, you must install the  [Python](https://www.python.org/downloads/release/python-390/) language on your machine. In addition, you must have the libraries listed below on your machine.

### Built With

* [Pandas 1.4.1](https://pypi.org/project/pandas/1.4.1/);
* [seaborn 0.11.2](https://pypi.org/project/seaborn/0.11.2/);
* [numpy 1.22.2](https://pypi.org/project/numpy/1.22.2/);
* [matplotlib 3.2.2](https://pypi.org/project/matplotlib/3.2.2/);
* [Streamlit 1.12.2](https://pypi.org/project/streamlit/1.12.2/);
* [wordcloud: 1.8.2.2](https://pypi.org/project/matplotlib/1.8.2.2);
* [scikit-learn 1.0.2](https://pypi.org/project/scikit-learn/1.0.2);
* [scikeras 0.8.0](https://pypi.org/project/scikeras/0.8.0/);
* [nltk 3.7](https://pypi.org/project/nltk/3.7/);
* [spacy 3.4.1](https://pypi.org/project/spacy/3.4.1/);
* [tensorflow 2.8.2](https://www.tensorflow.org/install?hl=pt-br);


### Running the Code


The installations of the libraries are already explained in the links above, type what is reported below for all libraries **EXCEPT FOR TENSORFLOW AND KERAS**, for the latter follow the links recommended above and use the same versions as me. So for the other libraries do:

```bash
pip install Streamlit==1.12.2
```
that is, for each library mentioned above with its respective version, just type:

```bash
pip install "library name"=="library version"
```
**WITHOUT THE QUOTES OF COURSE**. Done, go to the Deploy folder and ensure that you have all the files that are there on your machine, and residing in that folder do:

```bash
streamlit run main.py
```

and see the application running on your machine. :open_mouth:

you can also put all the files in the deploy folder in google colab, install just the streamlit o and type:
```bash
!pip install Streamlit==1.12.2
!streamlit run main.py & npx localtunnel --port 8501
```

and see the application running on google collab. :smirk: 


## Contributing

Criticism, doubts and suggestions feel free to send me:

e-mail: marcosmatheusdepaivasilva@gmail.com

LinkedIn: https://www.linkedin.com/in/marcos-matheus-silva-089699b3/ :hugs:

## Author

Marcos Matheus de Paiva Silva

## Credits

The dataset we pulled from [kaggle](https://www.kaggle.com/datasets/lava18/google-play-store-apps
), but it was initially collected by user LAVANYA with its proper [licence](https://creativecommons.org/licenses/by/3.0/), in this dataset the changes made were, creating entities, cleaning and data transformation, creation of bigrams and the tokenization of words. The code written in Google Collaboratory was based on the steps of the book Aurelien Geron - hands on machine learning-2019. Also, this code was developed based on everything I learned from: Jesse E.Agbe, Siddhardhan, Lucas Grassano Lattari, Shashank Kalanithi, Walisson Silva, Israel Dryer, Fernando Nakamuta, Alex Freberg.


## My License

This project is licensed under the MIT License - see the file [LICENSE](LICENSE) for more details.

