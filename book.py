#!/usr/bin/python3


def book_rented(books, booktype, duration):
    rate = 1
    if booktype == 'regular':
        rate = 1.5
    elif booktype == 'friction':
        rate = 3
    elif booktype == 'novels':
        rate = 1.5
    books_rate = books * rate
    price = books_rate * duration
    return price


if __name__ == '__main__':
    customer_name = input("Enter customer name:")
    print("\n")
    print("Hi, Welcome to book rent shopee, {} !!".format(customer_name))
    total_price = 0
    print("\n")
    while True:
        while True:
            booktype = input(
                "Please specify the book type(regular, friction, novels):").lower()
            default_type = ['regular', 'friction', 'novels']
            if booktype not in default_type:
                print("Book type must be regular, friction or novels.")
            else:
                break;
        books = int(input("How many books would you like to rent:"))
        for el in range(books):
            duration = int(input("For how many days:"))
            price = book_rented(books, booktype, duration)
            print(price)
            total_price += price
            print("\n")
        rent_more = input("Do you want to exit y/n:").lower()
        if rent_more in ['y', 'yes']:
            break;
    print("\n")
    print("Your total price is {}".format(total_price))