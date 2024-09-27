import sys


def split(email):
    return email.split("@")


email = sys.argv[1]
list = split(email)
print(f"Your username is {list[0]}.")
print(f"Your domain is {list[1]}.")