#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import urllib.parse
import re

from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'dockercompose_db_1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'ukpostcodes'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
  postcode = urllib.parse.unquote(request.args.get("postcode"))
  valid_postcode = re.compile(r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})")

  MYSQL_HOST = "db"
  MYSQL_USER = "root"
  MYSQL_PASSWORD = "secret"
  if postcode is not None:
      if valid_postcode.match(postcode):
          cur = mysql.connection.cursor()
          cur.execute("SELECT * FROM postcodelatlng WHERE postcode = '{0}'".format(postcode))
          rv = cur.fetchall()
          payload = []
          content = {}
          for result in rv:
              content = {'id': result[0], 'postcode': result[1], 'longitude': str(result[2]), 'latitude': str(result[2])}
              payload.append(content)
          return jsonify(payload)
      else:
          return "Invalid postcode supplied: {0}.".format(postcode)
  else:
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
