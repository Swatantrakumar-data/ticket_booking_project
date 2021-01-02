import mysql.connector
cnx = mysql.connector.connect(user='root', password='SW@sw@12345', host='localhost', database='booking')
mycursor = cnx.cursor()
s = "CREATE TABLE booking_ticket (Name VARCHAR(20), Gender VARCHAR(6), Age INT, Phone_number INT, per_price INT, selected_row INT, selected_col INT)"
mycursor.execute(s)







