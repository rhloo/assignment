# assignment
This Flask application is designed to manage users with features such as listing users, adding new users, and viewing detailed information about specific users. The application uses MySQL for database management and Bootstrap for front-end styling.
1. Clone the project repository from GitHub:git clone <repository-url>
cd <repository-folder>

2. Install the required Python packages using pip:pip install -r requirements.txt

3. a. Install MySQL
b. Create the Database and Table
Log in to MySQL:mysql -u root -p

Run the following commands :
CREATE DATABASE users;
USE users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL
);
c. Insert Sample Data:
INSERT INTO users (name, email, role) VALUES
('Rahul', 'rahul@gmail.com', 'Software developer'),
('Akash', 'akash@gmail.com', 'digital market'),
('Krishna', 'kri@gmail.com', 'Adisor');

4. Update the database credentials in the flask_api_users.py file:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'users'

5. Start the Flask server:
python flask_api_users.py

6. Routes:

/hello: Displays "Hello World!"

/users: Lists all users in an HTML table.

/new_user: Form to add a new user.

/users/<id>: Displays details for a specific user.

Error Handling: Handles missing resources (404) and invalid requests (400).

7. Additional Dependencies-
-Flask
-Flask-MySQLdb
-Bootstrap (via CDN)
Install Python dependencies:pip install Flask Flask-MySQLdb

8. Git Workflow

Clone the repository:
git clone <url>


Make your changes and commit:
git --add all 
git commit -m "assigment"

Push your changes to the remote repository:
git push origin 

Open a Pull Request (PR) on GitHub.

9. Write SQL queries to:

Insert sample data into the "users" table.

INSERT INTO users (name, email, role) VALUES
('Rahul', 'rahul@gmail.com', 'Software developer'),
('Akash', 'akash@gmail.com', 'digital market'),
('Krishna', 'kri@gmail.com', 'Adisor');

Retrieve all users from the "users" table.
SELECT * FROM users

Retrieve a specific user by their ID.
SELECT * FROM users WHERE id 
