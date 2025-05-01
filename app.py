from flask import Flask, render_template
import pyodbc
from config import conn_str


app = Flask(__name__)


def get_data(sql_query):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    items = cursor.fetchall()
    conn.close()
    return items


@app.route('/')
def home():
    data = get_data("SELECT * FROM dbo.Rijeci")
    return render_template('home.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=False)
