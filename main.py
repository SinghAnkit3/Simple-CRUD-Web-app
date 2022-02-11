import pymysql
from app import app
from db_config import mysql
from flask import render_template
from flask import flash, request

@app.route('/', methods=['GET'])
def add_employee():
   return render_template("view.html",datas=finalList())
   
@app.route("/add", methods=["POST"])
def home():
 try:
   id=request.form.get('id')
   name=request.form.get('uname')
   email=request.form.get('email')
   salary=request.form.get('salary')
   sql = "INSERT INTO employee(id, uname, email,salary) VALUES(%s, %s, %s ,  %s)"
   data = (id, name, email,salary)
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(sql, data)
   conn.commit()
   return render_template('view.html',datas=finalList())
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
   conn.close()

@app.route('/deleteEmployee', methods=['POST'])
def deleteEmployee():
 try:
   id=request.form.get('id')
   print(id)
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute("DELETE FROM employee WHERE id=%s", (id))
   conn.commit()
   return render_template('view.html',datas=finalList())
 except Exception as e:
  print(e)
 finally:
  cursor.close() 
  conn.close()
def finalList():
 try:
   conn = mysql.connect()
   cursor = conn.cursor(pymysql.cursors.DictCursor)
   cursor.execute("SELECT * FROM employee")
   rows = cursor.fetchall()
   return rows
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
   conn.close()

@app.route('/employeeUpdate', methods=['POST'])
def update_employee():
 try:
   id=request.form.get('id')
   name=request.form.get('uname')
   email=request.form.get('email')
   salary=request.form.get('salary')
  
   sql = "UPDATE employee SET uname=%s, email=%s, salary=%s WHERE id=%s"
   data = (name, email, salary, id,)
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute(sql, data)
   conn.commit()
   return render_template('view.html',datas=finalList())
 except Exception as e:
  print(e)
 finally:
  cursor.close() 
  conn.close()

if __name__ == "__main__":
    app.run(host='localhost',port='8080')