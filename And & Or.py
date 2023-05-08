age = int(input("How old are you?"))

if age < 18:
    print("You can't drink.")
elif age >= 18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")


True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False