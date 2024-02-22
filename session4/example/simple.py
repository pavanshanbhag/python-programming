import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters :
. ^ $ * + ? () {} [] | \

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Jayaprakash
Mr Pavan
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end 0 9 8 '

print(re.search(r'start', sentence, re.I))

pattern = re.compile(r'start', re.I)
print(type(pattern))

matches = pattern.search(sentence)
print(matches)
