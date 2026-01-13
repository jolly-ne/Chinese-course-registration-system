from flask import Flask, render_template, request, redirect, session
from mysql.connector.pooling import MySQLConnectionPool

app = Flask(__name__)
app.secret_key = "secret123"

pool = MySQLConnectionPool(
    pool_name="chinese_course_pool",
    pool_size=5,
    host="localhost",
    user="root",
    password="",
    database="chinese_course_system",
    connection_timeout=10,
)


def get_db():
    cnx = pool.get_connection()
    if not cnx.is_connected():
        cnx.reconnect(attempts=3, delay=1)
    return cnx

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "SELECT id FROM users WHERE email=%s AND password=%s",
                (email, password),
            )
            row = cursor.fetchone()
        finally:
            cursor.close()
            db.close()

        if row:
            session["user_id"] = row[0]
            return redirect("/dashboard")
        return render_template("login.html")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "SELECT id FROM users WHERE email=%s",
                (email,),
            )
            if cursor.fetchone():
                return render_template("register.html", error="Email already registered")
            cursor.execute(
                "INSERT INTO users (full_name, email, password) VALUES (%s,%s,%s)",
                (name, email, password)
            )
            db.commit()
        finally:
            cursor.close()
            db.close()
        return redirect("/")
    return render_template("register.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    error = None

    db = get_db()
    cursor = db.cursor()
    try:
        if request.method == "POST":
            course_id = request.form["course_id"]

            cursor.execute(
                "SELECT id FROM courses WHERE id=%s",
                (course_id,),
            )
            if not cursor.fetchone():
                error = "Selected course does not exist"
            else:
                cursor.execute(
                    "INSERT INTO registrations (user_id, course_id) VALUES (%s, %s)",
                    (session["user_id"], course_id),
                )
                db.commit()

        cursor.execute("SELECT id, course_name FROM courses ORDER BY id")
        courses = cursor.fetchall()
    finally:
        cursor.close()
        db.close()

    return render_template("dashboard.html", courses=courses, error=error)


@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
