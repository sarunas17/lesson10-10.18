

# def add_two_numbers(a, b):
#     print(a + b)

# add_two_numbers(5, 6)

# add_two_numbers(7, 9)

# add_two_numbers(15, 9)

# def say_hello():
#     print("Hello")

# say_hello()

# def add_two_numbers(a, b):
#     return(a + b)

# nr_sum = add_two_numbers(10, 10)

# print(nr_sum)

# Create a function that takes string as parameter and returns number of letters from that string.



# def count_letters(string):
#     letter_count = 0
#     for char in string:
#         if char.isalpha():
#             letter_count += 1
#     return letter_count
# string = "Laba diena kaip sekasi"
# result = count_letters(string)
# print(result)

# ///////////////////////////////////////////////////////////////////

def count_letters(in_string: str):
    return len(in_string.replace(" ", ""))

# ////////////////////////////////////////////////////////

# def add_two_numbers(a: str, b: str) -> str:
#    return a + b

def square_of_number(a: int) -> int:
    print("first function", a)
    return a ** 2

def make_a_string(text: str, x: int) -> str:
    print("second function", x)
    number = square_of_number(x)
    return text + str(number)

print(make_a_string("betkas", 5))
