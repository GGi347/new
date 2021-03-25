import os
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#create_app is the application factory which will create the 
#application or instance of flask class. This file will tell 
#python where to look for the application.
DB_HOST = "localhost"
DB_NAME = "foodforall"
DB_USER = "postgres"
DB_PASS = "admin"
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()

    conn.commit()
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        cur.execute("select * from customer;")
        print(cur.fetchall())
        return 'Hello, World!'
   
    return app
    cur.close()
    conn.close()
