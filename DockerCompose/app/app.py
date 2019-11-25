#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template

from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'ukpostcodes'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
  postcode = request.args.get("postcode")
  MYSQL_HOST = "dockercompose_db_1"
  MYSQL_USER = "root"
  MYSQL_PASSWORD = "secret"
  if postcode is not None:
      cur = mysql.connection.cursor()
      cur.execute("SELECT * FROM postcodelatlng WHERE postcode = %s", postcode)
      rv = cur.fetchall()
      payload = []
      content = {}
      for result in rv:
          content = {'id': result[0], 'postcode': result[1], 'longitude': result[2], 'latitude': result[2]}
          payload.append(content)
      return jsonify(payload)

  else:
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
