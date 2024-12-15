from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rahulgupta'  # Update with your MySQL password
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/users')
def list_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template('users.html', users=users)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        if not name or not email or not role:
            return "All fields are required", 400

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('list_users'))
    return render_template('new_user.html')


@app.route('/users/<int:id>')
def user_details(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    if not user:
        return "User not found", 404
    return render_template('user_details.html', user=user)




if __name__ == '__main__':
    app.run(debug=True)

