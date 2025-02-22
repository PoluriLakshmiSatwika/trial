from flask import Flask, render_template
import psycopg2  # Use psycopg2 for PostgreSQL connection
from urllib.parse import quote as url_quote

app = Flask(__name__)

# Database configuration for PostgreSQL on Render
db_config = {
    "host": "dpg-cus7gfhopnds7397o1l0-a",  # Your Render hostname
    "database": "spm_he2x",  # Your Render database name
    "user": "system",  # Your database username
    "password": "c5WmxUhSETVfxCjt9y6Yu8cxrgzuay2i",  # Your database password
    "port": "5432",  # Default PostgreSQL port
}

# Attempt to establish a database connection
try:
    # Create a database connection
    db_connection = psycopg2.connect(**db_config)

    # Check if the connection was successful
    print("Database connection established successfully!")

except psycopg2.Error as e:
    # Handle the error if the connection fails
    print(f"Error connecting to the database: {e}")

# Close the database connection when you're done
if 'db_connection' in locals():
    db_connection.close()

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
