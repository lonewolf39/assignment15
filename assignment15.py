#Q.1- Create a database of students

import sqlite3

out = sqlite3.connect('Students.db')
print("Opened database successfully")
out.close()

#Q.2- Take students name and marks from the user

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'create table students(Name varchar(10) primary key, \
    Marks int(3))'
    
    cursor.execute(query)
    
    print('Table created successfully!!')
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')

a = []
i=0
while(i<10):
    try:
        n = input("Enter name: ")
        m = int(input('Enter Marks: '))
        if(m<0 or m>100):
            raise ValueError('Invalid marks')
            i=i-1
        else:
            t = n,m
            a.append(t)
            i=i+1
    except  ValueError as o:
        print(o)



#Q.3- Append the values in 2 columns


try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = "insert into students(Name, Marks) \
    values(?,?)"
    
    records = l
    
    cursor.executemany(query, records)
    
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')

#Q.4- Print the names of all the students who scored more than 80 marks
try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'select * from students where Marks > 80'
    
    cursor.execute(query)
    
    data = cursor.fetchall()

    print("Student who scored greater then 80 are :")
    for row in data:
        print('Name: {}'\
             .format(row[0]))
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
