import random
import string
l= int(input("Enter length of the password:"))
if l <= 0:
    print("Invalid Number")
else:
    character = string.ascii_letters + string.digits + string.punctuation
    p = ''.join(random.choice(character) for _ in range(l))
    print(f"Generated Password: {p}")

