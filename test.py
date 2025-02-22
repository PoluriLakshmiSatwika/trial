from flask import Flask, render_template
import psycopg2
from psycopg2 import OperationalError
from urllib.parse import quote as url_quote

app = Flask(__name__)

# PostgreSQL Database Configuration (Render)
db_config = {
    "host": "dpg-cus7gfhopnds7397o1l0-a",  # Render hostname
    "database": "spm_he2x",  # Database name
    "user": "system",  # Database username
    "password": "c5WmxUhSETVfxCjt9y6Yu8cxrgzuay2i",  # Database password
    "port": "5432",  # PostgreSQL default port
}

# Attempt to establish a database connection
try:
    db_connection = psycopg2.connect(**db_config)
    print("Database connection established successfully!")
except OperationalError as e:
    print(f"Error connecting to the database: {e}")
