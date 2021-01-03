import math
import mysql.connector
class seat_detail:
    row = int(input('enter the no. of rows : '))
    col = int(input('enter the no. of cols : '))
    cnx = mysql.connector.connect(user='root', password='SW@sw@12345', host='localhost',database='booking')
    mycursor = cnx.cursor()


    def show_seat(self):
        seat_detail.mycursor.execute('SELECT selected_row,selected_col FROM booking_ticket')
        myresult = seat_detail.mycursor.fetchall()

        for i in range(1,seat_detail.row+1):
            print(i,end=" ")
            for j in range(1,seat_detail.col+1):
                if (i,j) in myresult:
                    print('B',end=" ")
                else:
                    print('S', end=" ")
            print()


    def book_ticket(self):
        selected_row = int(input('enter the row u selected to sit : '))
        selected_col = int(input('enter the col u selected to sit : '))
        seat_detail.mycursor.execute('SELECT selected_row,selected_col FROM booking_ticket')
        myresult = seat_detail.mycursor.fetchall()
        if (selected_row,selected_col) in myresult:
            print('Sorry, this seat is already booked')

        else:
            if seat_detail.row * seat_detail.col < 60 or (seat_detail.row * seat_detail.col > 60 and selected_row <= math.floor(seat_detail.row / 2)):
                self.price = 10

            else:
                self.price = 8
            print(f'${self.price} for ur ticket')
            choice = input('enter ur choice  yes/no : ')
            if choice == 'yes':

                name = input('enter ur name : ')
                gender = input('enter ur gender male/female : ')
                age = int(input('enter ur age : '))
                mob_no = int(input('enter ur mob no. : '))
                s = 'INSERT INTO booking_ticket VALUES(%s,%s,%s,%s,%s,%s,%s)'
                b = (name,gender,age,mob_no,self.price,selected_row,selected_col)
                seat_detail.mycursor.execute(s, b)
                seat_detail.cnx.commit()
                print('Booked Sucessfully')
            else:
                print('...No problem...')

    def statistics(self):
        s = 'SELECT COUNT(Name) FROM booking_ticket'
        seat_detail.mycursor.execute(s)
        counting = seat_detail.mycursor.fetchall()
        print('Number of Purchased Ticket: ',counting[0][0])

        percentage_counting = (counting[0][0]*100)/(seat_detail.row * seat_detail.col)
        print(f'Percentage: {percentage_counting}%')

        t='SELECT SUM(per_price) FROM booking_ticket'
        seat_detail.mycursor.execute(t)
        current_income = seat_detail.mycursor.fetchall()
        print(f'Current Income: ${current_income[0][0]}')

        if seat_detail.row * seat_detail.col < 60:
            total_price = 10*seat_detail.row * seat_detail.col
        else:
            total_price = 10 * math.floor(seat_detail.row/2)*seat_detail.col + 8*(seat_detail.row - math.floor(seat_detail.row/2))*seat_detail.col
        print(f'Total Income: ${total_price}')


    def user_info(self):
        row = int(input('enter the row u selected to sit : '))
        col = int(input('enter the col u selected to sit : '))
        s=f'SELECT *FROM booking_ticket WHERE selected_row={row} and selected_col={col}'
        seat_detail.mycursor.execute(s)
        myresult = seat_detail.mycursor.fetchall()
        if myresult:
            name,gender,age,phone_no,ticket_price,row_,col_=myresult[0]
            print('Name: ',name)
            print('Gender: ',gender)
            print('Age: ',age)
            print(f'Ticket Price: ${ticket_price}')
            print('Phone No.: ',phone_no)
        else:
            print('This sit is not booked')



if __name__ == '__main__':
    x = seat_detail()








