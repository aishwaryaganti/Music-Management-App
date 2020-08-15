# test.py
from flask import flash, render_template, request, redirect
from app import app
from db_setup import init_db

init_db()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
