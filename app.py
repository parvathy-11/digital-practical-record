from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(_name_)
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        # define the data to be inserted into the table
        data = [
        ('Jane123@gmail.com', '4321',student,'Jane',14,'S5'),('rahul10@gmail.com', '4326', student,'Rahul',25,'S5')
        ('Boban876@gmail.com','1234',student,'Bob',5,'S5')]

        c.execute('SELECT * FROM users WHERE email = ?, password = ? and user_type=?', (email, password,user_type))
  
        if user_type == 'student':
            user = c.fetchone()

            if user:
                session['email'] = email
                session['user_type'] = user_type
                return redirect(url_for('student_dashboard'))
            else:
                flash('Invalid email or password')
                return redirect(url_for('login'))

        elif user_type == 'faculty':
             user = c.fetchone()

             if user:
                session['email'] = email
                session['user_type'] = user_type
                return redirect(url_for('faculty_dashboard'))
             else:
                flash('Invalid email or password')
                return redirect(url_for('login'))

        conn.close()

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('user_type', None)
    return redirect(url_for('home'))

@app.route('/student_dashboard')
def student_dashboard():
    if 'email' in session and session['user_type'] == 'student':
        return render_template('student_dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/faculty_dashboard')
def faculty_dashboard():
    if 'email' in session and session['user_type'] == 'faculty':
        return render_template('faculty_dashboard.html')
    else:
        return redirect(url_for('login'))

if _name_ == '_main_':
    app.run(debug=True)