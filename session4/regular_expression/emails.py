import re

emails = '''
pavanshanbhag@gmail.com
jayaprakash@university.edu
test-123@my-work.net
dummy_email@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

