import psycopg2

con = psycopg2.connect(database="bookstore", user="postgres", password="Oracle987", host="127.0.0.1", port="5432")

print("Database opened successfully")

# cur = con.cursor()
# cur.execute('''CREATE TABLE STUDENT
#       (ADMISSION INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       COURSE        CHAR(50),
#       DEPARTMENT        CHAR(50));''')
# print("Table created successfully")

# con.commit()

# cur = con.cursor()

# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3424, 'Bizzy', 18, 'Data Engineering', 'ICT')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')");
# # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')");

# con.commit()
# print("Record inserted successfully")

### Read Operations ###
# cur = con.cursor()
# cur.execute("SELECT admission, name, age, course, department from STUDENT where name ='Bizzy'")
# rows = cur.fetchall()

# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")

# print("Operation done successfully")

### Update Operations ###
# cur = con.cursor()

# cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
# con.commit()
# print("Total updated rows:", cur.rowcount)

# cur.execute("SELECT admission, age, name, course, department from STUDENT")
# rows = cur.fetchall()
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[2])
#     print("DEPARTMENT =", row[3], "\n")

# print("Operation done successfully")

### DELETE OPERATION ###
# cur = con.cursor()

# cur.execute("DELETE from STUDENT where ADMISSION=3420;")
# con.commit()
# print("Total deleted rows:", cur.rowcount)

# cur.execute("SELECT admission, name, age, course, department from STUDENT")
# rows = cur.fetchall()
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")

# print("Deletion successful")


#con.close()

### RETURN JSON OUTPUT  FROM DATABASE###

# from flask import Flask, jsonify, url_for
# app = Flask(__name__)
# import json

# cur = con.cursor()
# cur.execute("SELECT admission, name, age, course, department from STUDENT")
# row_headers=[x[0] for x in cur.description] #this will extract row headers
# rows = cur.fetchall()
# json_data=[]

# for result in rows:
#         json_data.append(dict(zip(row_headers,result)))
# print(json.dumps(json_data))
# con.close()


from flask import Flask, jsonify, url_for, abort
app = Flask(__name__)
import json

@app.route('/get-todo-list')
def get_todolist():
    cur = con.cursor()
    cur.execute("SELECT admission, name, age, course, department from STUDENT")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rows = cur.fetchall()
    json_data=[]

    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    #return json.dumps(json_data)
    return jsonify(json_data)


@app.route('/get-todo-list/<int:task_id>', methods=['GET'])
def get_task(task_id:int):
    cur = con.cursor()
    cur.execute("SELECT * from STUDENT where admission=%s" (task_id))
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rows = cur.fetchall()
   # task = [task for task in tasks if task['id'] == task_id]
    # if len(task) == 0:
    #     abort(404)
    # return jsonify({'task': task[0]})
    json_data=[]

    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

# con.close()

if __name__ == '__main__':
    app.run(debug=True)

