"""Copyright 2014 Valentin Wagner & Jonathan Eberle."""
import datetime
from string import hexdigits as letters
import random
import bcrypt


def date_to_number(date):
    """
    take birthdate as string and convert to the three magic digits.

    from accnamemaker.py Copyright 2014 Nicolai Koukal.
    Heavily modified.
    birthdate is 8-10 character long.
    """
    date = date.split(".")
    years = int(date[2])
    months = int(date[1])
    days = int(date[0])
    diff = datetime.date(years, months, days)-datetime.date(1899, 12, 30)
    diff = diff.days
    diff = str(diff)
    number = diff[-3:]
    return number


def username(first_name, last_name, date):
    """make username."""
    name = first_name[:2] + last_name[:2]
    name = name.lower()
    return(name + date_to_number(date))


def gen_pw():
    """
    generate a password.

    Copyright 2014 Jonathan Eberle.
    """
    pw = ""
    for i in range(7):
        pw += random.choice(letters)
    hashed = str(
        bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt()))[2:-1]
    return pw, hashed


def read_student_list(path):
    list_file = open(path)
    student_list = list_file.readlines()
    path.close()
    del(student_list[0])
    return student_list


def process_student_list(list):
    """process student list. """
    students_and_passwords = []
    students_and_hashes = []
    for line in student_list:
        line = line.split(";")
        UID = username(line[2], line[1], line[3])
        password, hashed = gen_pw()
        print(UID, password, hashed)
        students_and_passwords.append([UID, line[2], line[1], password, line[0]])
        students_and_passwords.append([UID, line[2], line[1], hashed, line[0]])
    return students_and_passwords, students_and_hashes


def store(path_plain, path_hashed):
    

