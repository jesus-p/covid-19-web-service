from flask import Flask, render_template
from google.cloud import bigquery
import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np
import time
import db_dtypes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mexico')
def mexico():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT country_name, population
        FROM `covid-19-web-service.covid19data.covid19_open_data` 
        LIMIT 10
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="country_name", y="population",title='Population in Mex')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="Mexico"
    description = """
    test
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/usa')
def usa():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["London", "London", "London", "Madrid", "Madrid", "Madrid"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="USA"
    description = """
    ****** USA INFO
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/case_study')
def casestudy():
    header="Let's plan a trip to the 7 Wonders of the World!"
    
    description = """
    A recent Vrbo survey of 8,000-plus people found that 65 percent of Americans plan on traveling more in 2022 than they did pre-Covid. Traveling after lockdown will look much different than before. 
    International travel poses additional risks, and even fully vaccinated travelers might be at increased risk for getting and possibly spreading some COVID-19 variants.
    It is now extremely important to be aware of the dangers of COVID19 when travelling.  Our group decided that a visual representation of these dangers, in terms of how many reported cases of COVID19 there is internationally,
    would help travellers be safer when taking trips internationally. We created a Google App Engine that uses Machine Learning to help discern this informatio when considering taking a trip to one of the Seven Wonders of the World.
    The New Seven Wonders of the Worlds are:
    """
    return render_template('webpage.html', header=header,description=description)