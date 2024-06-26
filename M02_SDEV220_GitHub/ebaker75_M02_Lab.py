"""
Elizabeth Baker
GPA Checker
This app will ask for a student's name and check if they made the Dean's List ( GPA >= 3.5)
or if they made the Honor Roll (GPA >= 3.25).
"""

lName = input("Enter student's last name or ZZZ to quit: ") #initialize flag (last name as string)
while lName != "ZZZ":
	fName = input("Enter student's first name: ") #first name as string
	gpa = float(input("Enter student's GPA: ")) #GPA as float
	if gpa >= 3.5:
		print(f"{fName} {lName} made Dean's List and Honor Roll!")
	elif gpa >= 3.25:
		print(f"{fName} {lName} made Honor Roll!")
	else:
		print(f"{fName} {lName} is not qualified for Honor Roll or Dean's List.")
	lName = input("Enter next student's last name or ZZZ to quit:")
else:
	print("Program complete.") #inform user that program is finished