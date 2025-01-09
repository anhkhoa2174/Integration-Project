from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_file
from functools import wraps
import psycopg2
from logging.config import dictConfig
import logging
import sys
import base64
import os
from PyPDF2 import PdfReader
from io import BytesIO
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
file_storage = {}

# Kết nối cơ sở dữ liệu
def get_db_connection():
    return psycopg2.connect(database="CNPM", user="postgres", password="p123", host="localhost", port="5432")


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

#owner routes ##############################################################

@app.route('/ownercalendar')
def ownercalendar():
    return render_template('owner_calendar.html')

@app.route('/ownercalendar2')
def ownercalendar2():
    return render_template('owner_calendar_var2.html')

@app.route('/ownerdeposit')
def ownerdeposit():
    return render_template('owner_deposit.html')

@app.route('/owner_dashboard')
def owner_dashboard():
    return render_template('owner_dashboard.html')

@app.route('/owner_configure_field')
def owner_configure_field():
    return render_template('owner_configure_field.html')

@app.route('/owner_managefield')
def owner_managefield():
    return render_template('owner_managefield.html')

@app.route('/owner_register_field')
def owner_register_field():
    return render_template('owner_register_field.html')

@app.route('/owner_view_field_more')
def owner_view_field_more():
    return render_template('owner_view_field_more.html')

############################################################################


@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/user_bookfield')
def user_bookfield():
    return render_template('user_bookfield.html')

@app.route('/user_homescreen')
def user_homescreen():
    return render_template('user_homescreen.html')

@app.route('/bookfield_info')
def bookfield_info():
    return render_template('bookfield_info.html')

if __name__ == '__main__':
    app.run(debug=True)