"""dasfasdfasdf."""
import random
import bcrypt
from string import hexdigits as letters


def append_to_file(filepath, string):
    """write string to file."""
    outfile = open(filepath, "a")
    outfile.write(string)
    outfile.close


user_file = open("users")
users = user_file.readlines()
user_file.close()

users_and_pws = []

"""for user in users:
    user = user[:-1]
    pw = ""
    for i in range(7):
        pw += random.choice(letters)
    # pw = user + ";" + pw + "\n"
    append_to_file("users.csv", user + ";" + pw + "\n")
    append_to_file("users_hashed.csv", user + ";" + str(bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt()))[2:-1] + "\n")"""
pw = ""
for i in range(7):
    pw += random.choice(letters)
print(pw)
