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
    name = name.lower()
    if name.count(' ') == 1:
        pos_of_space = name.index(' ')
        part1 = name[0:2]
        part2 = name[pos_of_space+1:pos_of_space+3]
        shortname = part1+part2
        return shortname


print(name_to_shortname("Max Mustermann")+date_to_number("1.1.1970"))
