password = input("Enter password: ")

strength = {}

if len(password) >= 8:
    strength["length"] = True
else:
    strength["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

strength["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

strength["uppercase"] = uppercase

total = sum(strength.values())

if total == 3:
    print("Strong password")
elif total == 2:
    print("Medium password")
else:
    print("Weak password")
