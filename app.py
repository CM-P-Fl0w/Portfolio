
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, message
import os
# from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def blog():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
