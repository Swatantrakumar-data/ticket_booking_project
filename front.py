from seat_detail import seat_detail

while True:
    print('1.Show the seats')
    print('2.Buy a Ticket')
    print('3.Statistics')
    print('4.Show booked Tickets User info')
    print('0.Exit')

    choice = input('enter ur choice : ')
    if choice == '1':
        seat_detail.show_seat(seat_detail)
        print()

    elif choice == '2':
        seat_detail.book_ticket(seat_detail)
        print()

    elif choice == '3':
        seat_detail.statistics(seat_detail)
        print()

    elif choice == '4':
        seat_detail.user_info(seat_detail)
        print()

    else:
        break







