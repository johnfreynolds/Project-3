import cgi

def alphabet_position(letter):
	ltr = letter.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alist = list(alphabet)
	pos = alist.index(ltr)
	return(pos)

def rotate_character(char, rot):
    if char.isupper():
        # Upper case letter
        charpos = alphabet_position(char)
        newpos = (charpos + rot) % 26
        newchr = chr(newpos + 65)
        return(newchr)
    elif char.islower():
        # Lower case letter
        charpos = alphabet_position(char)
        newpos = (charpos + rot) % 26
        newchr = chr(newpos + 97)
        return(newchr)
    else:
        # Unrecognized character
        return(char)

# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

# -----------
# User Instructions
#
# Modify the valid_day() function to verify
# whether the string a user enters is a valid
# day. The valid_day() function takes as
# input a String, and returns either a valid
# Int or None. If the passed in String is
# not a valid day, return None.
# If it is a valid day, then return
# the day as an Int, not a String. Don't
# worry about months of different length.
# Assume a day is valid if it is a number
# between 1 and 31.
# Be careful, the input can be any string
# at all, you don't have any guarantees
# that the user will input a sensible
# day.
#
# Hint: The string function isdigit() might be helpful.

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

# -----------
# User Instructions
#
# Modify the valid_year() function to verify
# whether the string a user enters is a valid
# year. If the passed in parameter 'year'
# is not a valid year, return None.
# If 'year' is a valid year, then return
# the year as a number. Assume a year
# is valid if it is a number between 1900 and
# 2020.
#

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1500 and year < 2080:
            return year

# User Instructions
#
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#

def escape_html(s):
    return cgi.escape(s, quote = True)
