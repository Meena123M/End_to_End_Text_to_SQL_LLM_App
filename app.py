from dotenv import load_dotenv
import streamlit as st
import sqlite3
import os
import google.generativeai as genai

load_dotenv()
# os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
GOOGLE_API_KEY='AIzaSyBVa0oc4e5kXdgfbr16mM4jKPeVRvGSJC8'

# load the genai model
def load_model(question,prompt):
    genai.configure(api_key=GOOGLE_API_KEY)
    model=genai.GenerativeModel(model_name='gemini-1.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrieve the query from the database
def read_sql_query(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows  


prompt=[""" 
             you are a sql expert converting english text to sql query.
             The sql query database has been in the name of student and consists of columns
             such as name,subject,marks. I wanted to know the total count of rows.
             \n sql command will be like select * from student . and tell me the students
             who studies in data science. sql query like select subject from student where subject='Data science'
             sql code shouldnt have ''' at the beginning or end of the output.    
    """]      
import streamlit as st
st.header('The SQL Retrival')
st.title('SQL Query Chatbot')

question=st.text_input('input:',key='input')

submit=st.button('Ask the question')

if submit:
    response=load_model(question,prompt)
    print(response)
    data=read_sql_query(response,'student.db')
    st.subheader('The Response is')
    for row in data:
        print(row)
        st.header(row)