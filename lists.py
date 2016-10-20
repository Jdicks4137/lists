# Josh Dickey 10/20/16
# This program displays all of the prime numbers from 2 to a value given by the user


def maximum_value():
    """This receives the maximum value from the user and creates a list of numbers from 2 to that value."""
    number = int(input("please enter the maximum value."))
    list_of_numbers = list(range(2, number + 1))
    return list_of_numbers


def calculate_prime(my_list):
    """This creates a new list and puts prime numbers into it."""
    primes = []
    while len(my_list) > 0:
        first = my_list[0]
        primes.append(first)
        for number in my_list:
            if number % first == 0:
                my_list.remove(number)
    print(primes)


def main():
    """This is the main function that runs the program."""
    number_list = maximum_value()
    calculate_prime(number_list)


main()
