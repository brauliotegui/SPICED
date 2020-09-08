# SPICED Academy Projects

 <p align="center">
  <img src="https://github.com/brauliotegui/SPICED/blob/master/spiced_banner.png" width="75%" height="75%">
  </p>

## Week 01| Gapminder: Data Visualization Project

* The project analyzes the Gapminder project's data and helps to visualize the
correlation between each country's population and fertiliy rate. The gif image was generated with python and matplotlib. 
* Life Expectancy vs. Fertility:
  <p align="center">
  <img src="https://github.com/brauliotegui/SPICED/blob/master/Week_01/animatedplotchart.gif" width="75%" height="75%">
  </p>

* The Jupyter notebook for this small project can be found [here](https://github.com/brauliotegui/SPICED/blob/master/Week_01/2.7_animate.ipynb).

## Week 02| Titanic: Classifier/ Logistic Regression Project

* This project approaches a classic Machine Learning problem, with a classication model, in order to predict passenger survival on the Titanic.
With python and sklearn library, after a detailed process of feature engineering, I was able to train a Random Forest and Logistic Regression model
with accuracy scores inbetween 81% and 84%. A k-fold Cross Validation was used to test the machine learning models and presented consistent scores
around 94%.

* The Jupyter notebook for this project can be found [here](https://github.com/brauliotegui/SPICED/blob/master/Week_02/Titanic_ModelProject.ipynb).

## Week 03| Bikeshare: Linear Regression 

* Here the approach to Machine Learning is done with Linear Regression models. Through intensive Data Exploration Analysis, correlation analysis, and
feature engineering with dates, I was able to construct robust models to estimate number of bike rentals on a particular time. GridSearchCV was used
to attain the best fitting model which indicated Linear models with above average mean test scores.

* The Jupyter notebook for this project can be found [here](https://github.com/brauliotegui/SPICED/blob/master/Week_03/Project_CapitalBikeShare_Regression.ipynb).

## Week 04| Bikeshare: Lyrics Classifier - Natural Language Processing Project

* The goal here is to build a text classification model to predict the artist from a piece of text. I programmed python functions to perform Web Scraping done with BeautifulSoup to download song lyrics from specifc artists url and save only the corpus lyrics as texts files from every single song lyrics url. Class imbalance was dealt with over sampling, texts were engineered with CountVectorizer and TfidfTransformer, and Machine Learning was done by training classification models, which were validated and tested to see the which one was the best fit for the project. A command-line interface is included that allows users to input a text for prediction.

* The Jupyter notebook for this project can be found [here](https://github.com/brauliotegui/SPICED/blob/master/Week_04/Project_Lyrics_Prediction_Final.ipynb).

## Week 05| Forecast Model

* For this project, I created a short-term temperature forecast. This involved Time series to predict future temperature for a specific location using AR and ARIMA models with a Walk Forward approach, achieving a MAE as low as 1.8.

* The Jupyter notebook for this project can be found [here](https://github.com/brauliotegui/SPICED/blob/master/Week_05/Project_TimeSeriesAnalysis-Final.ipynb).

## Week 06| Dashboard: Postgres, SQL, RDS, and AWS

* In this project, I built a dashboard summarizing the Northwind Database. It is a sample database that is shipped along with Microsoft Access. The data is about “Northwind Traders”, a fictional company. The database contains all sales transactions between the company and its customers as well as purchases from Northwinds suppliers. For such project, I created a Postgre database in order to create tables inside and write SQL queries that retrieves data. Data was loaded from CSV files into a database. SQLAlchemy library was also used in this project for accessing a database from Python. Ultimately, AWS was used in this project to upload everything into a cloud server and, in this way, building a dashboard with metabase that stayed up and running 24/7.

These are some examples of dashboards that were generated using the Northwind Database: 
<p align="center">
<img src="https://github.com/brauliotegui/SPICED/blob/master/Week_06/public_dashboard-example1.png" width="691" height="432">
<img src="https://github.com/brauliotegui/SPICED/blob/master/Week_06/public_dashboard-example2.png" width="691" height="232">
  </p>

## Week 07| Data Pipeline: Docker, MongoDB, and ETL

* The goal of this project was to build a Dockerized Data Pipeline that analyzes the sentiment of tweets. The challenges of this project was to get a Docker Pipeline running that would collect tweets with Tweepy API, process it to include a sentiment analysis of the tweets and then send those tweets to a Slack channel via a Slackbot. For that, a skeleton pipeline was built, tweets were collected and stored in a MongoDB, a python code was implemented to create a ETL task running sentiment analysis, and at last a Slackbot was programmed to send the analyzed tweets from a Postgres database to a slack channel periodically. 

* The folder of the project pipeline can be found [here](https://github.com/brauliotegui/SPICED/tree/master/Week_07/Twitter).

## Week 08| Markov Chain-based simulator

* In this project, I teamed up with colleagues to write a program that simulates customer behaviour in a supermarket. The project involed 4 main stages: exploring the data -- which included pandas wrangling, calculating transition probabilities (a 5x5 matrix), implementing a Markov Chain-based simulator and creating a program to visualize how customers move through the supermarket through animation.
The program uses classes, Markov Chain modeling, and a Monte-Carlo simulation...

* The folder of the project can be found [here](https://github.com/brauliotegui/MARKET).
