import re
fruits = "apple,banana,veg"
pattern = r","
split = re.split(pattern,fruits)
print("splitted string:", split)