import re
import requests

#  * means to look one or all occurrences
# ? means look for 0 or one occurrence
# {} means you can provide a certain amount of occurrences in a row.




# EXAMPLE FOR TAKING A STRING WITH WORDS SEPERATED BY SPACES
# print(re.split(r'\s*', 'here are some words'))


# ANOTHER EXAMPLE WHERE THE LETTER/STRING SPECIFIED IS FOUND THE STRING IS SPLIT
# print(re.split(r'(o*)', 'here are some words'))


# ANOTHER EXAMPLE: Split upon finding any character from A to F

# print(re.split(r'[a-f]','Hello Far From Here there is a Cup.', re.I|re.M))

# re.I|re.M - be case Insensitive and if input string is multilined, evaluate continously.


# ANOTHER EXAMPLE:


# print(re.findall(r'\d{1,5}\s\w+\s\w+\.', '123 Awesome st. aslkdjalksjd, NY'))

# \d means digits
# \s means a space
# \w means word
# \. means period

# PRACTICAL HTML EXAMPLE


googleResponse = requests.get('http://www.wsj.com').content
try:
	googleResponse = str(googleResponse,'ISO-8859-1')
	print('ISO', googleResponse[:1000])
except:
	googleResponse = str(googleResponse,'utf-8')
	print('UTF', googleResponse[:1000])

titleTags = re.findall(r'<title+.*</title>+',googleResponse, re.I|re.M)
print(titleTags)





