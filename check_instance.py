import sys

type = sys.argv[1]
if type == "t2.micro":
    print("OK, we have instance, charges: 20$")

elif type == "t2.medium":
    print("OK, we have instance, charges: 30$")

elif type == "t2.large":
    print("OK, we have instance, charges: 40$")
else:
    print("We dont have this kind of instance")
