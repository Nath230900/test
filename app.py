from flask import Flask, render_template, request, redirect
import mysql.connector
 
app = Flask(__name__)
 
# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change to your MySQL username
    password="",  # Change to your MySQL password
    database="student_db"
)
 
@app.route('/')
def index():
    return render_template('register.html')
 
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    course = request.form['course']
 
    cursor = db.cursor()
    sql = "INSERT INTO students (name, email, age, course) VALUES (%s, %s, %s, %s)"
    values = (name, email, age, course)
    cursor.execute(sql, values)
    db.commit()
 
    return redirect('/')
 
if __name__ == '__main__':
    app.run(debug=True)