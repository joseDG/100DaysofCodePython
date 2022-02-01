# ejercicio1
""""
import random

choice = input("What is your choice?Head or Tail")

number = random.randint(0, 1)

if number == 1:
    print('You have got Tail')
else:
    print('You got a Tail!')
"""
# Ejercicio2
import random
names_string = input("Give me everybody name, separete by a comma.")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the message")
