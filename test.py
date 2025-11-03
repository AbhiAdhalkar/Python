import re
arn = "arn:aws:iam::123456789012:user/johndoe"
splitted = arn.split("/")[1]
print(splitted)
name = "Abhishek Adhalkar"
length = len(name)
print(length)
print(name.upper())
str1 = "Abhishek"
str2 = "Adhalkar"
result = str1 + " " + str2
print(result)
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

text = "Python is awesome is"
substring = "is"
if substring in text:
    print(substring, "found in the text")

pattern = r"is"
search = re.search(pattern, text)
if search:
    print("found:", search.group())
else:
    print("not found")