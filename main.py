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

@app.route('/brazil')
def brazil():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'Brazil'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in Brazil')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="Brazil"
    description = """
    Showing live statistics for Brazil
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/china')
def china():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'China'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in China')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="China"
    description = """
    Showing live statistics for China
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/mexico')
def mexico():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'Mexico'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in Mexico')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="Mexico"
    description = """
    Showing live statistics for Mexico
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/jordan')
def jordan():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'Jordan'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in Jordan')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="Jordan"
    description = """
    Showing live statistics for Jordan
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/india')
def india():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'India'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in India')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="India"
    description = """
    Showing live statistics for India
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/italy')
def italy():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'Italy'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in Italy')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="Italy"
    description = """
    Showing live statistics for Italy
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/peru')
def peru():
    #initialize query
    client = bigquery.Client()
    sql = """
        SELECT date, SUM(confirmed) num_reports
        FROM `bigquery-public-data.covid19_open_data.compatibility_view`
        WHERE country_region = 'Peru'
        GROUP BY date
        HAVING num_reports IS NOT NULL
        ORDER BY date DESC
        LIMIT 20
    """
    df = client.query(sql).to_dataframe()

    fig = px.line(df, x="date", y="num_reports",title='Confirmed COVID-19 Cases in Peru')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    header="Peru"
    description = """
    Showing live statistics for Peru
    """
    return render_template('chart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/case_study')
def casestudy():
    header="Let's Plan a Trip to The 7 Wonders of The World!"
    
    return render_template('webpage.html', header=header)

@app.route('/code_snippet')
def code():
    return render_template('code.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)