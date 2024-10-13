import sys


def split(email):
    return email.split("@")


email = sys.argv[1]
username, domain = split(email)
print(f"Your username is {username}.")
print(f"Your domain is {domain}.")