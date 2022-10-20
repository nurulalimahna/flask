from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'search_engine'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ajaxpost", methods=["POST", "GET"])
def ajaxpost():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        queryString = request.form['queryString']
        print(queryString)
        query = "SELECT * from list_search WHERE value LIKE '{}%' LIMIT 10".format(queryString)
        cur.execute(query)
        cari = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', cari=cari)})


if __name__ == "__main__":
    app.run(debug=True)