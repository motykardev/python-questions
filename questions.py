#Variables
i = 0
name_list = []
age_list = []
height_list = []
#starter question for our script
no_of_people = int(input("How many people? \n"))
#loop connected with no_of_people variable that will 
while True:
    if i < no_of_people:
        name = str(input("What is your name? \n"))
        age = int(input("What is your age? \n"))
        height = str(input("What is your height? \n"))
        name_list.append(name)
        age_list.append(age)
        height_list.append(height)
        i=+1
    else:
        break


print("Details collected Successfully!")
print(name_list)
#successfull check
