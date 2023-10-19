# Create a function that adds a string ending to each member in a list.

def add_string_to_list(random_list: list, text: str) -> list:
   return [item + text for item in random_list]

random_list = ["green", "white", "red", "blue", "grey"]
text = "color"
print(add_string_to_list(random_list, text))

