import re # imports regular expressions (regex) module.
namesFile = open("names.txt", encoding="utf-8")
data = namesFile.read()
namesFile.close()
# print(re.match(r'Love',data)) # match method only finds first criteria at beginning of the string.
# print(re.search(r'Obama',data)) # finds it somewhere in the string.
# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d',data)) # matches the phone numbers
# print(re.search(r'\(\d{3}\) \d{3}-\d{4}',data)) # an easier way to search the characters of a phone number
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}',data)) # finds all instances and ? makes the () and - in phone number optional.
print(re.findall(r'\w*, \w+',data))
