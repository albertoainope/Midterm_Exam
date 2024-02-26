string = "Midterm"
#string[0] = "j"
#We get an error in line 2 because strings are immutable
print(string)
list = [1, 2, 3, 4, 5]
list[0] = 6
print(list)
#We do not get an error for lists because lists are mutable