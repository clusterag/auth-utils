"""generate account names."""
import datetime


def date_to_number(date):
    """take birthdate as string and convert to the three magic digits."""
    if date.count('.') == 2:
        date = date.split('.')
    else:
        print('Error: String contains more than two dots')
        return ''
    days = int(date[0])
    months = int(date[1])
    years = int(date[2])
    try:
        diff = datetime.date(years, months, days)-datetime.date(1899, 12, 30)
        diff = diff.days
        diff = str(diff)
        number = diff[2:5]
        return number
    except ValueError:
        print('Error: Date is not in range')
        return ''


def name_to_shortname(name):
    """take the first two letters from the first and from the last name."""
    if name.count(' ') >= 1:
        name = name.lower()
        name = name.split(' ')
        name1 = name[0]
        name2 = name[len(name)-1]
        return name1[0:2]+name2[0:2]
    else:
        return ''


def username(name, date):
    return(name_to_shortname(name)+date_to_number(date))

name = input("Name?\n")
date = input("Geburtsdatum?\n")
print(username(name, date))
