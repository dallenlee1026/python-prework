# QUESTION 1

def hello_name(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")


hello_name('david')


# QUESTION 2

def first_odds():
    """Print all odd numbers from 1-100."""
    for i in range(1, 100):
        if i % 2 != 0:
            print(i)


first_odds()


# QUESTION 3

def max_num_in_list(a_list):
    """Determine the maximum number in a list."""
    return max(a_list)


print(max_num_in_list([1, 5, 300, 100, 7]))


# QUESTION 4

def is_leap_year(a_year):
    """Determine if a given year is a leap year."""
    if a_year % 4 == 0:
        if a_year % 100 != 0:
            return True
        elif a_year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


print(is_leap_year(2000))


# QUESTION 5

def is_consecutive(a_list):
    """Determine if the numbers in a list are consecutive."""
    for i in range(len(a_list)-1):
        if a_list[i] != a_list[i+1] - 1:
            return False
    return True


print(is_consecutive([2, 3, 4, 5, 6, 7]))
