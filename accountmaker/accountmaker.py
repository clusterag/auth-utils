"""Copyright 2014 Valentin Wagner & Jonathan Eberle."""
import datetime
from string import hexdigits as letters
import random
import bcrypt


def write_file_as_string(filepath, string):
    """
    write string to file.

    Taken from vertretungsplan.py Copyright 2014 Jonathan Eberle.
    """
    outfile = open(filepath, "wb+")
    outfile.write(string.encode("utf-8"))
    outfile.close


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
    """read student list and return as list."""
    list_file = open(path, "r", encoding="ISO-8859-1")
    student_list = list_file.readlines()
    list_file.close()
    del(student_list[0])
    return student_list


def process_student_list(list):
    """process student list. """
    students_and_passwords = []
    students_and_hashes = []
    for line in list:
        line = line.split(";")
        UID = username(line[2], line[1], line[3])
        password, hashed = gen_pw()
        print(UID, password, hashed)
        students_and_passwords.append([line[0], line[2], line[1], UID, password])
        students_and_hashes.append([UID, line[2], line[1], hashed, line[0]])
    return students_and_passwords, students_and_hashes


def write_list_to_file(path, list):
    string = ""
    for i in list:
        string += ("\n" + ";".join(i))
    write_file_as_string(path, string)


def split_classes(list):
    classes = {}
    for student in list:
        if (student[0] in classes):
            classes[student[0]].append(student)
        else:
            classes[student[0]] = [["Klasse", "Vorname", "Nachname", "Benutzername", "Passwort"]]
            classes[student[0]].append(student)
    return(classes)


def write_classes_to_files(directory, classes):
    for singleclass in classes:
        print(classes[singleclass])
        write_list_to_file(directory + "/" + classes[singleclass][1][0] + ".csv", classes[singleclass])


list_plain, list_hashed = process_student_list(read_student_list("students.csv"))
print(list_plain)
print(list_hashed)
write_list_to_file("plain.csv", list_plain)
write_list_to_file("hashed.csv", list_hashed)
classes = split_classes(list_plain)
print(classes)
write_classes_to_files("klassen", classes)
