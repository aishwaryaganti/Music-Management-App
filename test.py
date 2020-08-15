# test.py

from app import app
from db_setup import init_db

init_db()


@app.route('/')
def test():
    return "Music Management App"


if __name__ == '__main__':
    app.run()
