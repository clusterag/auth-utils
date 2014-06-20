"""dasfasdfasdf."""
import random
import bcrypt
from string import hexdigits as letters
from sys import argv as arguments


def append_to_file(filepath, string):
    """write string to file."""
    outfile = open(filepath, "a")
    outfile.write(string)
    outfile.close


def gen_pw():
    """generate a password."""
    pw = ""
    for i in range(7):
        pw += random.choice(letters)
    hashed = str(
        bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt()))[2:-1]
    return pw, hashed


def get_users(user_file_path):
    """read usernames from file."""
    user_file = open(user_file_path)
    users = user_file.readlines()
    user_file.close()


def single_password():
    """print a single password and exit."""
    print(gen_pw)


def batch():
    """generate to csv."""
    user_file_path = input("path to file containing user names:")
    plaintext_file_path = input("output path of csv file containing passwords in plaintext:")
    hashed_file_path = input("output path of csv file containing hashed passwords:")
    users_and_pws = []
    users = get_users(user_file_path)
    for user in users:
        user = user[:-1]
        pw, hashed = gen_pw()
        append_to_file(plaintext_file_path, user + ";" + pw + "\n")
        append_to_file(hashed_file_path, user + ";" + hashed + "\n")

if arguments[1] == "batch":
    batch()
else:
    single_password()
