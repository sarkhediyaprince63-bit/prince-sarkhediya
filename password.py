import random 
import string

length=int(input("enter a password:"))

include_latters = input("enter latters(y/n): ")
include_symbole = input("enter symbole(y/n): ")
include_number = input("enter number(y/n): ")


characters = ""


if include_latters.lower().strip() == 'y':
    characters += string.ascii_letters

if include_symbole.lower().strip() == 'y':
    characters += string.punctuation

if include_number.lower().strip() == 'y':
    characters += string.digits

password = "".join(random.choice(characters) for i in range(length))

print("Generated Password:", password)