import sys
instance_type = sys.argv[1]
if instance_type == "t2.micro":
    print("yes, Instance is available")
elif instance_type == "t3.micro":
    print("yes, Instance is available")
elif instance_type == "t4.micro":
    print("yes, Instance is available")
else:
    print("Wrong choice")
