from flask import Flask, render_template
from flask_wtf import FlaskForm
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return""

if __name__ == "__main__":
    app.run()





    

