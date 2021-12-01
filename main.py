#import re to more efficiently create a list from the text file
import re

#Open day 1 input text file
my_file = open("Day1.txt", "r")

#Create a list to put the inputs from Day1.txt into
day1inputlist = []

#Looping the inputs into the list
for line in my_file:
    day1inputlist = list(map(int, re.findall('\d+', my_file.read())))
my_file.close()

#i equal the counter for locating the integers in the list
i = 0
#j is the counter for keeping track of increased measurement
j = 1

#Looping through the list to find increase and decrease for each measurement
for i in range(i, len(day1inputlist)):

    try:
        if i == 0:
            print(day1inputlist[i], '(N/A - no previous measurement)')

        elif day1inputlist[i-1] < day1inputlist[i]:
            j = j + 1
            print(day1inputlist[i], '(Increased)' , j)

        elif day1inputlist[i-1] > day1inputlist[i]:
            print(day1inputlist[i], '(Decreased)')

        elif day1inputlist[i-1] == day1inputlist[i]:
            print(day1inputlist[i], '(No Change)')

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print(f'In this example, there are {j} measurements that are larger than the previous measurement.')
