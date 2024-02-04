"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Chase Kalina-Wilson #FIXME1 #fixed#
    Date: 1/30/2024 #FIXME2 #fixed#
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

from unicodedata import name


print("Welcome to ASCII Art Program...\n")

# FIXME3: prompt user to enter their name and store the value into name variable using input function #Fixed#
names: str = input("What is your name? ") 
# FIXME4: greet the name using the variable as the following output #Fixed#
print("Nice meeting you, "+ names +"  ")
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

# FIXME5: prompt user to enter the year and store the value into year variable using input function #fixed#
year: str = input("What year is it? ")
# FIXME6: print the year using the variable as the following output #fixed#
print("This is "+year+" year")
# must output: This is <year> year.

print("Hope you like my ASCII art...\n\n")

line1: str = "  |\\_/|   **********************     (\\_/)\n   "
print(line1)

# FIXME7: use variable to print the second line of the graphic #fixed#
line2: str = "/  @ @  \  *    ASCII Lab  l   *   ( ='.'= )\n "

print(line2) 
# FIXME8: print the third line of the graphics #fixed#
line3: str ="( > 0 < )  *      "+names+"       *   "'( " )_( " )'" \n"

print(line3)

# FIXME9: use variable to print the fourth line ##fixed#
line4: str = "  >>x<<   *      CSCI 110      *\n   "

print(line4)

# FIXME10: use variable to print the fifth line #fixed#
line5: str = "  / O \   *        "+year+"        *\n   "

print(line5)

line6: str = "          ************************\n    "

print(line6)

# Note: You can add more lines or print more ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")
