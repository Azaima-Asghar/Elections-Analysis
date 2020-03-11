counties = []
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

temperature = int(input("what is temp outside"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

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

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

voting_data = {}
voting_data = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}

print(voting_data)

for county, registered_votes in voting_data.items():
    print (str(county) + " county has",str(registered_votes )+ " registered voters")

voting_data_list = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data_list:
    print(county_dict)

for i in range(len(voting_data_list)):
    print(voting_data_list[i])

for county_dict in voting_data_list:
    for value in county_dict.values():
        print(value) 

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
 
for county, registered_votes in counties_dict.items():
     print(f"{county} county has {registered_votes:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for county in voting_data:
     print(f"{county['county']} has {county['registered_voters']:,} registered voters.")