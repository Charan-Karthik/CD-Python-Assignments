# 1. Update Values in Dictionaries and Lists
# 1.1: Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# 1.2: Change the last_name of the first student from 'Jordan' to 'Bryant'
# 1.3: In the sports_directory, change 'Messi' to 'Andres'
# 1.4: Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.1
x[1][0] = 15
print(x)
#1.2
students[0]['last_name'] = "Bryant"
print(students)
#1.3
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
#1.4
z[0]['y'] = 30
print(z)


print()
# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(len(students)):
        display_string = ""
        for key, value in students[i].items():
            if key != 'last_name':
                display_string = display_string + str(key) + " - " + str(value) + ", "
            else:
                display_string = display_string + str(key) + " - " + str(value)
        print(display_string)
iterateDictionary(students)


print()
# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

def iterateDictionary2(key,list):
    for i in range(len(students)):
        print(students[i][key])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


print()
# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for key in dictionary:
        print(len(dojo[key]), key.upper())
        for i in range(len(dojo[key])):
            print(dojo[key][i])
        print()
printInfo(dojo)