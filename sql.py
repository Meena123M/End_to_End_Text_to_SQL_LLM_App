import sqlite3

# 1. Connect to the database

connection = sqlite3.connect("student.db")

#create cursor
cursor=connection.cursor()

#create table
# student_info='''
# create table student(id integer primary key autoincrement,
# name text,
# subject varchar(20),
# marks integer)
# '''

#execute the query
# cursor.execute(student_info)

#insert data
cursor.execute("insert into student(name,subject,marks) values('John','Maths',80)")
cursor.execute("insert into student(name,subject,marks) values('Jane','Science',90)")
cursor.execute("insert into student(name,subject,marks) values('Jim','History',70)")
cursor.execute("insert into student(name,subject,marks) values('Jack','Physics',75)")
cursor.execute("insert into student(name,subject,marks) values('Jill','English',53)")
cursor.execute("insert into student(name,subject,marks) values('mia','Data science',35)")
cursor.execute("insert into student(name,subject,marks) values('ria','Data science',85)")
cursor.execute("insert into student(name,subject,marks) values('kia','Data science',65)")

#read the data
data=cursor.execute('''select * from student''')
for row in data:
    print(row)

connection.commit()
#close the connection
connection.close()
