#!/usr/bin/python3


def book_rented(books, duration):
    rate = 1
    books_rate = books * rate
    price = books_rate * duration
    return price


if __name__ == '__main__':
    customer_name = input("Enter customer name:")
    print("Hi, Welcome to book rent shopee, {} !!".format(customer_name))
    books = int(input("How many books would you like to rent:"))
    duration = int(input("For how much duration:"))
    price = book_rented(books, duration)
    print(price)
