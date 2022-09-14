# UNDER CONSTRUCTION

# Analyzing-User-Satisfaction-in-Applications_end-to-end

https://user-images.githubusercontent.com/92632851/190245479-a2556841-d559-44e8-b73b-9f96fc97bc0e.mp4

## Important notes about the project

Este projeto foi construído com inúmeras ferramentas e tecnologias, este é um documento resumido. Portanto, se você deseja obter mais informações estatísticas e computacionais consulte [jupyter Notebook](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/blob/main/jupyterNotebook/Analyzing_User_Satisfaction_in_ApplicationsNotebook.ipynb), para ler sobre as conclusões encontradas sobre o projeto, analise o [Report](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/blob/main/Report/Report_Sentiment_Analysis__Marcos_Matheus.pdf), você também pode acessar o aplicativo criado em [Deploy](https://github.com/M-MSilva/Analyzing-User-Satisfaction-in-Applications---end_to_end_project/tree/main/Deploy). Meu objetivo inicial era criar um modelo para classificar o sentimento de um usuário como bom, neutro ou ruim, mas transformei o problema em binário (bom ou ruim). Não dividimos os labels em positivo, neutro e negativo, pois o código fica demasiado lento e ruim, já que devemos aplicar diversas técnicas para classificação multi classe, como por exemplo camadas Flatten e BatchNormalization. No vídeo acima uso o discurso de martin luther king para criar os gráficos fonte: [Discurso de Martin Luther King, Jr](https://www.americanrhetoric.com/speeches/mlkihaveadream.htm). :hugs:

## About this project

O objetivo deste projeto é classificar se um usuário está satisfeito ou não com um aplicativo da google play, com base em seu comentário, ou seja, basicamente prevemos se o usuário gosta ou não de um aplicativo da google play através de seu comentário. Ademais, este é um projeto completo, pois passamos por várias etapas de um projeto usual de ciência de dados, como coleta de dados, engenharia de recursos, limpeza de dados, transformação de dados, visualização de dados, análise de dados, modelagem e implantação.

## Applications 

Através desse projeto automatizamos a análise de feedback de usuários, como também somos capazes de usar tal aplicação, para criar a classificação de um aplicativo, quando o usuário não o faz, mas realiza apenas o comentário. A partir desse projeto poderemos no futuro criar um  gerenciamento de suporte ao cliente, com base em seu comentário. Aliás, meu projeto pode ser generalizado para ser usado em avaliações de chats, análises de respostas de pesquisas, pesquisa de mercado e acompanhar a reputação de aplicativos. :call_me_hand:

## Motivation
Este projeto foi desenvolvido para fazer parte do meu portfólio pessoal e serviu tanto para testar minhas habilidades quanto para meu aprendizado, já que usamos inúmeras tecnologias nele. Apesar de ser um projeto de ponta a ponta, ainda precisa de algumas melhorias futuras, como ter um conjunto de dados maior e mais diversificado. :smiley:

## Functionalities

### Developed Web APPs:

* Entre com o nome do aplicativo e realize o comentário;
* descubra o nível de satisfação de um usuário;
* Crie uma análise exploratória de dados contendo as palavras mais frequentes, os bigramas e as entidades nomeadas na crítica (caso a crítica for robusta e bem detalhada!);



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


As instalações das bibliotecas já estão explicadas nos links acima, digite o relatado abaixo para todas as biliotecas MENOS PARA TENSORFLOW E KERAS, para estas últimas siga os links recomentadados acima e use as mesmas versões que eu. Portanto, para as outras bibliotecas faça:

```bash
pip install Streamlit==1.12.2
```
ou seja para cada biblioteca acima citada com sua respectiva versão, basta digitar:

```bash
pip install "library name"=="library version"
```
SEM AS ASPAS É CLARO. Feito, vá para a pasta Deploy e garanta que possui todos os arquivos que estão lá em sua máquina e faça:

```bash
streamlit run main.py
```

e veja o aplicativo rodando na sua máquina. :open_mouth:

voce pode também colocar todos estes arquivos da pasta deploy no google colab, instalar apenas o streamlit o e digitar:
```bash
!pip install Streamlit==1.12.2
!streamlit run main.py & npx localtunnel --port 8501
```

e veja o aplicativo rodando nos google collab. :smirk: 


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

