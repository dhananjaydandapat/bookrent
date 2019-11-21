#!/usr/bin/python3


def book_rented(books, booktype, duration):
    """
    Function to calculate the price for renting books based
    on the duration and book type.
    :params int books: No of books customer wants to rent
    :params string booktype: Type of book customer wants to rent
    :params int duration: For how many days user want to rent(in days)
    :return: (total, {"Book Type": booktype, "Books Count": books, "Duration": duration,
            "Unit price": rate, "Total Price": price})
    """
    rate = 1
    if booktype == 'regular':
        rate = 1.5
        if duration > 2:
            first_two_days = 2 * 1
            remaining_days = (duration - 2) * rate
            rate = first_two_days + remaining_days
        else:
            rate = 2
        price = rate * books
    elif booktype == 'friction':
        rate = 3
        books_rate = books * rate
        price = books_rate * duration
    elif booktype == 'novels':
        if duration > 3:
            rate = 1.5
        else:
            rate = 4.5
        books_rate = books * rate
        price = books_rate * duration
    data = {"Book Type": booktype, "Books Count": books, "Duration": duration,
            "Unit price": rate, "Total Price": price}
    # print(data)
    return price, data


if __name__ == '__main__':
    print("\n")
    customer_name = input("Enter customer name:")
    print("\n")
    print("\tHi, Welcome to book rent shopee, {} !!".format(customer_name))
    total_price = 0
    result = []
    print("\n")
    while True:
        while True:
            booktype = input(
                "Please specify the book type(regular, friction, novels):").lower()
            default_type = ['regular', 'friction', 'novels']
            if booktype not in default_type:
                print("Book type must be regular, friction or novels.")
            else:
                break
        books = int(input("How many books would you like to rent:"))
        # for el in range(books):
        duration = int(input("For how many days:"))
        res = book_rented(books, booktype, duration)
        print(res)
        total_price += res[0]
        result.append(res[1])
        print("\n")
        rent_more = input("Do you want to exit y/n:").lower()
        if rent_more in ['y', 'yes']:
            break
    print("\n")
    print("Your total price is {}".format(total_price))
