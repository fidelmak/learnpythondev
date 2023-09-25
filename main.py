# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone, that was a great magic show!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
even_numbers = list(range(2, 11, 2))
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
squares = [value**3 for value in range(1, 11)]
print(squares)