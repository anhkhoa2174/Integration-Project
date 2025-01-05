from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_file
from functools import wraps
# import psycopg2
from logging.config import dictConfig
import logging
import sys
import base64
import os
# from PyPDF2 import PdfReader
from io import BytesIO
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
file_storage = {}

# # Kết nối cơ sở dữ liệu
# def get_db_connection():
#     return psycopg2.connect(database="CNPM", user="postgres", password="p123", host="localhost", port="5432")


@app.route('/')
def login():
    return render_template('index.html') 

@app.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')

@app.route('/transaction_history')
def transaction_history():
    return render_template('transaction_history.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

@app.route('/dashboard')
def admin_dashboard():
    return render_template('administrator/dashboard.html')

@app.route('/navbar')
def admin_navbar():
    return render_template('administrator/navbar.html')

@app.route('/sidebar')
def admin_sidebar():
    return render_template('administrator/sidebar.html')

@app.route('/navsidebar')
def admin_navsidebar():
    return render_template('administrator/navsidebar.html')

@app.route('/test')
def admin_test():
    return render_template('administrator/test.html')

@app.route('/test1')
def admin_test1():
    return render_template('administrator/test1.html')

if __name__ == '__main__':
    app.run(debug=True)
