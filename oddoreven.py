#python program to check even or odd of a given number
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

user_input = int(input("Enter a number: "))
result = even_or_odd(user_input)
print(f"{user_input} is {result}")
