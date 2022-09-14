# UNDER CONSTRUCTION

# Analyzing-User-Satisfaction-in-Applications_end-to-end

https://user-images.githubusercontent.com/92632851/190245479-a2556841-d559-44e8-b73b-9f96fc97bc0e.mp4

## Important notes about the project

Este projeto foi construído com inúmeras ferramentas e tecnologias, este é um documento resumido. Portanto, se você deseja obter mais informações estatísticas e computacionais consulte [jupyter Notebook](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/blob/main/jupyterNotebook/Analyzing_User_Satisfaction_in_ApplicationsNotebook.ipynb), para ler sobre as conclusões encontradas sobre o projeto, analise o [Report](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/blob/main/Report/Report_Sentiment_Analysis__Marcos_Matheus.pdf), você também pode acessar o aplicativo criado em [Deploy](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/tree/main/Deploy). Meu objetivo inicial era criar um modelo para classificar o sentimento de um usuário como bom, neutro ou ruim, mas transformei o problema em binário (bom ou ruim). Não dividimos os labels em positivo, neutro e negativo, pois o código fica demasiado lento e ruim, já que devemos aplicar diversas técnicas para classificação multi classe, como por exemplo camadas Flatten e BatchNormalization. No vídeo acima uso o discurso de martin luther king para criar os gráficos fonte: [Discurso de Martin Luther King, Jr](https://www.americanrhetoric.com/speeches/mlkihaveadream.htm). :hugs:

## About this project

O objetivo deste projeto é classificar se um usuário está satisfeito ou não com um aplicativo da google play, com base em seu comentário, ou seja, basicamente prevemos se o usuário gosta ou não de um aplicativo da google play através de seu comentário. Ademais, este é um projeto completo, pois passamos por várias etapas de um projeto usual de ciência de dados, como coleta de dados, engenharia de recursos, limpeza de dados, transformação de dados, visualização de dados, análise de dados, modelagem e implantação.

## Applications 

The current project can be used to help an athlete in his training to know how many points he would make based on some information, and it can also be used in competitions and betting. Although this program is part of my personal portfolio, feel free to use it for studies, repairs and improvements. :call_me_hand:

## Motivation
This project was developed to be part of my personal portfolio and served both to test my skills and for my learning, since countless technologies could be used in it. Despite being an end-to-end project, it still needs some future improvements, such as having a larger and more diverse dataset. :smiley:

## Functionalities

### Developed Web APPs:

* Enter athlete data and the like;
* Find out how many points an athlete would have.

### Web APP included by Streamlit

* Rerun;
* Automatically update the app when the underlying code is updated;
* Enable wide mode so the app takes up the entire width of the screen;
* Choose by dark or light theme;
* Record a video or audio of the screen;
* Report a bug;
* Get Help;
* About.


## Instructions to run and/or compile the code

### Initial Requirements

The application is already running and it is not necessary to install anything on your machine, however, if you want to run the application locally, you must install the  [Python](https://www.python.org/downloads/release/python-390/) language on your machine. In addition, you must have the libraries listed below on your machine.

### Built With

* [Pandas 1.4.1](https://pypi.org/project/pandas/);
* [Imblearn 0.0](https://pypi.org/project/imblearn/);
* [seaborn 0.11.2](https://pypi.org/project/seaborn/0.11.2/);
* [pickle-mixin 1.0.2](https://pypi.org/project/pickle-mixin/);
* [numpy 1.22.2](https://pypi.org/project/numpy/);
* [Streamlit 1.6.0](https://pypi.org/project/streamlit/);
* [scikit-learn 1.0.2](https://pypi.org/project/scikit-learn/);
* [xgboost 0.90](https://pypi.org/project/xgboost/0.90/);
* [Requests 2.27.1](https://pypi.org/project/requests/);
* [Beautifulsoup 4.10.0](https://pypi.org/project/beautifulsoup4/).

Hosted In:

* heroku


### Running the Code

The installations of the libraries are already explained in the links above, but if you want to be in the same versions I do:

```bash
pip install scikit-learn==1.0.2
```
```bash
pip install streamlit==1.6.0
```
```bash
pip install numpy==1.22.2
```
```bash
pip install pickle-mixin==1.0.2
```
```bash
pip install pandas==1.4.1
```
```bash
pip install imblearn==0.0
```

```bash
pip install xgboost==0.90
```

done, go to the Deploy folder and type:

```bash
streamlit run PredictPointsWebAPP.py
```


and see the application run on your machine. :open_mouth:


## Contributing

Criticism, doubts and suggestions feel free to send me:

e-mail: marcosmatheusdepaivasilva@gmail.com

LinkedIn: https://www.linkedin.com/in/marcos-matheus-silva-089699b3/ :hugs:

## Author

Marcos Matheus de Paiva Silva

## Credits

Web scraping was done from https://www.nbastuffer.com/player-stats/. The code written in Google Colaboratory was based on the steps of the book Aurelien Geron - hands on machine learning-2019. In addition, this code was developed based on everything I learned from: Jesse E.Agbe, Siddhardhan, Lucas Grassano Lattari, Shashank Kalanithi, Walisson Silva, Israel Dryer, Fernando Nakamuta,  Alex Freberg.


## License

This project is licensed under the MIT License - see the file [LICENSE](LICENSE) for more details.

