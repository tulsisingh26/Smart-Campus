from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)

app.secret_key = "smartcampus123"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tulsi@2006",
    database="campus"
)

cursor = db.cursor()

@app.route("/")
def home():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    roll_no = request.form["roll_no"]
    department = request.form["department"]
    email = request.form["email"]
    phone = request.form["phone"]

    sql = """
    INSERT INTO students(name, roll_no, department, email, phone)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, (name, roll_no, department, email, phone))
    
    
    db.commit()

    flash("Student registered successfully!")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)