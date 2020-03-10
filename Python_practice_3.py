# what is your grade score?#

score = int(input("what is your test score?"))

# determine the grade

if score >= 90:
    print("your grade is an a A")
else: 
    if score >= 80:
        print("your grade is an a B")
    else:
        if score >= 70:
            print("your grade is an a C")
        else:
            if score >= 60:
                print("your grade is an a D")
            else:
                print("your grade is an a F")

# easier way to do this is to have if - elif statements

score = int(input("what is your test score?"))

# determine the grade

if score >= 90:
    print("your grade is an a A") 
elif score >= 80:
    print("your grade is an a B")
elif  score >= 70:
    print("your grade is an a C")
elif  score >= 60:
    print("your grade is an a D")
else:
    print("your grade is an a F")