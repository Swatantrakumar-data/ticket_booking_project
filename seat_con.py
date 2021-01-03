import mysql.connector
cnx = mysql.connector.connect(user='root', password='SW@sw@12345', host='localhost',database='booking')
mycursor = cnx.cursor()
mycursor.execute('CREATE DATABASE booking')
mycursor.execute('USE booking')
s = "CREATE TABLE booking_ticket (Name VARCHAR(20), Gender VARCHAR(6), Age INT, Phone_number INT, per_price INT, selected_row INT, selected_col INT)"
mycursor.execute(s)
mycursor.execute('alter table booking_ticket add primary key(selected_row,selected_col)')







