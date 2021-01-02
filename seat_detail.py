import math
import mysql.connector
class seat_detail:
    row = int(input('enter the no. of rows : '))
    col = int(input('enter the no. of cols : '))
    cnx = mysql.connector.connect(user='root', password='SW@sw@12345', host='localhost',database='booking')
    mycursor = cnx.cursor()


    def show_seat(self):
        seat_detail.mycursor.execute('select selected_row,selected_col from booking_ticket')
        myresult=seat_detail.mycursor.fetchall()

        for i in range(seat_detail.row):
            for j in range(seat_detail.col):
                if (i,j) in myresult:
                    print('B',end=" ")
                else:
                    print('S', end=" ")
            print()


    def book_ticket(self):
        selected_row = int(input('enter the row u selected to sit : '))
        selected_col = int(input('enter the col u selected to sit : '))
        seat_detail.mycursor.execute('select selected_row,selected_col from booking_ticket')
        myresult = seat_detail.mycursor.fetchall()
        if (selected_row,selected_col) in myresult:
            print('Sorry, this seat is already booked')
        else:
            print('this seat is avilable')

        if seat_detail.row * seat_detail.col < 60 or (
                seat_detail.row * seat_detail.col > 60 and selected_row <= math.floor(seat_detail.row / 2)):
            self.price = 10

        else:
            self.price = 8
        print(f'${self.price} for ur ticket')
        choice=input('enter ur choice  yes/no : ')
        if choice == 'yes':

            name=input('enter ur name : ')
            gender=input('enter ur gender male/female : ')
            age=int(input('enter ur age : '))
            mob_no=int(input('enter ur mob no. : '))
            s = 'insert into booking_ticket values(%s,%s,%s,%s,%s,%s,%s)'
            b = (name,gender,age,mob_no,self.price,selected_row,selected_col)
            seat_detail.mycursor.execute(s, b)
            seat_detail.cnx.commit()
            print('Booked Sucessfully')
        else:
            print('...No problem...')

    def statistics(self):
        s='select count(Name) from booking_ticket'
        seat_detail.mycursor.execute(s)
        counting=seat_detail.mycursor.fetchall()
        print('Number of Purchased Ticket: ',counting[0][0])

        percentage_counting = counting[0][0]/(seat_detail.row * seat_detail.col)
        print('Percentage: ',percentage_counting)

        t='select sum(per_price) from booking_ticket'
        seat_detail.mycursor.execute(t)
        current_income=seat_detail.mycursor.fetchall()
        print('Current Income: $',current_income[0][0])

        if seat_detail.row * seat_detail.col < 60:
            total_price = 10*seat_detail.row * seat_detail.col
        else:
            total_price = 10 * math.floor(seat_detail.row/2)*seat_detail.col + 8*(seat_detail.row - math.floor(seat_detail.row/2))*seat_detail.col
        print('Total Income: $',total_price)



    def user_info(self):
        row = int(input('enter the row u selected to sit : '))
        col = int(input('enter the col u selected to sit : '))
        s=f'select *from booking_ticket where selected_row={row} and selected_col={col}'
        seat_detail.mycursor.execute(s)
        myresult=seat_detail.mycursor.fetchall()
        if myresult:
            name,gender,age,phone_no,ticket_price,row_,col_=myresult[0]
            print('Name: ',name)
            print('Gender: ',gender)
            print('Age: ',age)
            print(f'Ticket Price: ${ticket_price}')
            print('Phone No.: ',phone_no)
        else:
            print('This sit is not booked')










