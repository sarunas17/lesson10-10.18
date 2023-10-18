# Create at least 5 different functions by your own and test it.

def sum_of_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c
print(sum_of_three_numbers(5, 10, 20))

def about_me(name: str, surname: str, age: int) -> str:
    return name + " "  + surname + " " + str(age)
print(about_me("Sarunas", "Staskevicius", 33))

def letters_a_count(text: str) -> int:
    return(len([word for word in text.split(" ") if "a" in word]))
print(letters_a_count("Laba diena kaip jums sekasi"))

def separate(text: str) -> str:
    return text.replace(" ", "|")
print(separate("Mano vardas yra Sarunas"))

def round_my_number(number: float) -> float:
    return round(number, 3)
print(round_my_number(3.666666666665489754))