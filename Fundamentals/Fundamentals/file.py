num1 = 42 # variable declaration, initialize int (a whole number)
num2 = 2.3 # variable declaration, initialize float (a decimal number)
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # log statement, calls type() function on variable fruit; should display tuple in terminal
print(pizza_toppings[1]) # log statement that accesses value of list at index 1
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) # log statement that accesses the dictionary person and logs the value associated with the key 'name'
person['name'] = 'George' # changes value for the key 'name' in the dictionary 'person'
person['eye_color'] = 'blue' # adds key 'eye_color' with value 'blue' in dictionary 'person'
print(fruit[2]) # logs the second index in the tuple 'fruit'

if num1 > 45: # conditional, if
    print("It's greater") # log statement
else: # conditional, else
    print("It's lower") # log statement

if len(string) < 5: # conditional, if
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional, else if
    print("It's a long word!") # log statement
else: # conditional, else
    print("Just right!") # log statement

for x in range(5): # start for loop, 0-4
    print(x) # log statement
for x in range(2,5): # start for loop, 2-4
    print(x) # log statement
for x in range(2,10,3): # start for loop, 2-9 by 3s
    print(x) # log statement
x = 0 # variable declaration, int
while(x < 5): # start while loop, runs until x >=5
    print(x) # log statement
    x += 1 # increment statement

pizza_toppings.pop() # remove last value from list
pizza_toppings.pop(1) # remove index 1 from list

print(person) # log statement
person.pop('eye_color') # remove key:value pair from dictionary
print(person) # log statement

for topping in pizza_toppings: # start for loop through each index of list
    if topping == 'Pepperoni': # conditional, if
        continue # continue to next iteration
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional, if
        break # break out of for loop

def print_hello_ten_times(): # creates function 
    for num in range(10): # for loop that'll run 0-9
        print('Hello') # log statement

print_hello_ten_times() # runs function

def print_hello_x_times(x): # creates a function that takes an input (x)
    for num in range(x): # for loop that'll run 0-(x-1)
        print('Hello') # log statement

print_hello_x_times(4) # runs function with input x=4

def print_hello_x_or_ten_times(x = 10): # creates function w/ variable declaration
    for num in range(x): # for loop that'll run 0-9
        print('Hello') # log statement

print_hello_x_or_ten_times() # runs function
print_hello_x_or_ten_times(4) # runs function with input 4


"""
Bonus section
"""

# print(num3) # will return error since num3 is not defined yet
# num3 = 72 # variable delcaration, int

# fruit[0] = 'cranberry' # will result in error since tuples are immutable

# print(person['favorite_team']) # will result in an error since that key is not defined in the dictionary

# print(pizza_toppings[7]) # index out of range error

#   print(boolean) # error since it's indented when it shouldn't be

# fruit.append('raspberry') # error since tuples are immutable
# fruit.pop(1) # error since tuples are immutable