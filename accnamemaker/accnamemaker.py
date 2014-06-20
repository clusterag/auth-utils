import datetime


def date_to_number(date):
	"""take the 8-10 character long birthdate as a string and convert it to the three magic digits."""
	pos_of_dot = date.index('.')
	if date.count('.') <> 2:
		return
	else:
		if len(date) == 10:  #for 01.01.2014
			days = int(date[0:2])
			months = int(date[3:5])
			years = int(date[6:10])
		elif len(date) == 9:
			if pos_of_dot == 2:  #for 01.1.2014
				days = int(date[0:2])
				months = int(date[3])
				years = int(date[5:9])
			elif pos_of_dot == 1:  #for 1.01.2014
				days = int(date[0])
				months = int(date[3:4])
				years = int(date[5:9])
			else:
				return
		elif len(date) == 8:  #for 1.1.2014
				days = int(date[0])
				months = int(date[2])
				years = int(date[4:8])
		else:
			return
	diff = datetime.date(years, months, days)-datetime.date(1899, 12, 30)
	diff = diff.days
	diff = str(diff)
	number = diff[2:5]
	return number


def name_to_shortname(name):
	"""take the first two letters from the first and from the last name."""
	name = name.lower()
	if name.count(' ') == 1:
		pos_of_space = name.index(' ')
		part1 = name[0:2]
		part2 = name[pos_of_space+1:pos_of_space+3]
		shortname = part1+part2
		return shortname


print name_to_shortname("Max Mustermann")+date_to_number("1.1.1970")


