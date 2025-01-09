from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash, send_file
from functools import wraps
import psycopg2
from logging.config import dictConfig
import logging

from psycopg2.extras import RealDictCursor
# from PyPDF2 import PdfReader
from io import BytesIO
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
file_storage = {}

# Kết nối cơ sở dữ liệu
def get_db_connection():
    return psycopg2.connect(database="project", user="postgres", password="p123", host="localhost", port="5432")


# Đăng nhập
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Kết nối cơ sở dữ liệu và truy vấn thông tin người dùng
        try:
            conn = get_db_connection()
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                session['username'] = user['username']
                session['role'] = user['role']

                # Chuyển hướng theo vai trò
                if user['role'] == 'user':
                    return redirect(url_for('user_homescreen'))
                elif user['role'] == 'admin':
                    return redirect(url_for('admin_dashboard'))
                elif user['role'] == 'owner':
                    return redirect(url_for('owner_dashboard'))
                else:
                    flash("Vai trò không hợp lệ.", "error")
            else:
                flash("Tên đăng nhập hoặc mật khẩu không đúng.", "error")
        except Exception as e:
            logger.error(f"Lỗi kết nối cơ sở dữ liệu: {e}")
            flash("Có lỗi xảy ra, vui lòng thử lại.", "error")

    return render_template('index.html')  # Trang đăng nhập

@app.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')

@app.route('/transaction_history')
def transaction_history():
    return render_template('transaction_history.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')


@app.route('/admin_transaction_history')
def admin_transaction_history():
    return render_template('administrator/admin_transaction_history.html')

@app.route('/admin_manage_user')
def admin_manage_user():
    return render_template('administrator/admin_manage_user.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('administrator/dashboard.html')

@app.route('/admin_manage_field')
def admin_manage_field():
    return render_template('administrator/admin_manage_field.html')

@app.route('/admin_statistics')
def admin_statistics():
    return render_template('administrator/admin_statistics.html')

@app.route('/admin_field_info')
def admin_field_info():
    return render_template('administrator/admin_field_info.html')

@app.route('/test1')
def test1():
    return render_template('administrator/test1.html')

@app.route('/test2')
def test2():
    return render_template('administrator/test2.html')
  
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