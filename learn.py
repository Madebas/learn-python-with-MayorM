
             #----LESS LEARN PYTHON BY MAYORM----
print("Hello World!") #this is a string in simple words textual data
print(5) #this is a number in simple words numerical data
#Why do we use " " or ' ' in Python?   In Python, both double quotes (") and
# single quotes (') are used to define strings—which are sequences of characters like words or sentences.

print("It's a beautiful day!")  # Use double quotes if the string contains a single quote
print('He said, "Hello!"')      # Use single quotes if the string contains double quotes

#What is print() used for? # The print() function in Python is used to output data to the console or standard output device.
#The print() function is used to display output on the screen. It’s one of the most common functions in Python, especially for:
#Showing results
#Debugging your code
#Displaying messages to users
name = "Mayor M"
print("My name is", name)


      #------VARIABLES IN PYTHON------
#What is a variable in Python? # A variable in Python is a name that refers to a value. It allows you to store data and refer to it later.
#we start by the name of the variable, followed by an equal sign (=), and then the value we want to assign to that variable.
#Variables can store different types of data, such as numbers, strings, lists, and more.
#Example:
age = 25  # Here, 'age' is the variable name, and 25 is the value assigned to age.
print(age)
#Variables can be reassigned to new values
age = 30  # Reassigning a new value to the variable 'age'

price = 19.99  # A variable to store a price
first_name = "Mayor"  # A variable to store a 

#boolean variable
is_student = True  # A variable to store a boolean value (True or False)
is_online = False  # Another boolean variable

#-----input from user---
#The input() function is used to get information from the user while the program is running
#It pauses the program and waits for the user to type something and press Enter.
#input() lets your program ask a question and receive an answer from the person using it.

#Example:

name = input("What is your name? ")
print("Hello, " + name + "!")

user_name = input("Enter your name: ")  # Prompting the user to enter their name
print("Hello,", user_name)  # Displaying a greeting with the user's name

age = input("Enter your age: ")
print("You are " + age + " years old.")
#Note: input() always returns a string. If you want to do math, you need to convert it using int() or float().
#string concatenation means joining two or more strings together to make one longer string.


first_name = "Achieng"
last_name = "Otieno"
full_name = first_name + " " + last_name
print(full_name)
#This will output: Achieng Otieno


# Get the Type
# The type() function is used to determine the type of a variable or value in Python.
# It returns the type of the object passed to it, which can be useful for debugging or understanding your code.
#Example:
x = 5
y = "John"
#This will output:
print(type(x)) # <class 'int'>
print(type(y)) #<class 'str'>
#The type() function can be used with any data type, including numbers, strings, lists, dictionaries, and more.


           #----Python - Variable Names------
#Variable names in Python are used to identify variables and must follow certain rules:
#1. They can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
#2. They must start with a letter or an underscore, not a digit.
#3. They are case-sensitive (e.g., myVar and myvar are different variables).
#4. They cannot be a reserved keyword in Python (like if, else, while, etc.).
#5. They should be descriptive to make your code more readable.
#Examples of valid variable names:
my_variable = 10
age_1 = 25
user_age = 30
#Examples of invalid variable names:
#1myVariable = 5  # Cannot start with a digit
# my-variable = 10  # Cannot contain hyphens
# my variable = 20  # Cannot contain spaces
# _myVariable = 15  # Valid, starts with an underscore
# my@variable = 30  # Cannot contain special characters like @

#----Multi Words Variable Names------
#When creating variable names with multiple words, you can use:
#1. Snake Case: Use underscores to separate words (e.g., my_variable_name).
#2. Camel Case: Capitalize the first letter of each word except the first (e.g., myVariableName).
#3. Pascal Case: Capitalize the first letter of each word (e.g., MyVariableName).
#4. Kebab Case: Use hyphens to separate words (e.g., my-variable-name) - not recommended in Python.


                 #-----Python Variables - Assign Multiple Values------
#In Python, you can assign multiple values to multiple variables in a single line.
#Example:
x, y, z = 1, 2, 3  # Assigning values to multiple variables
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3
x = y = z = "Orange"  # Assigning the same value to multiple variables
print(x)  # Output: Orange
print(y)  # Output: Orange
print(z)  # Output: Orange
#You can also assign multiple values to a single variable using a list or tuple.
#Example:
my_list = [1, 2, 3]  # Assigning a list to a variable
my_tuple = (4, 5, 6)  # Assigning a tuple to a variable
#You can unpack the values from a list or tuple into multiple variables.
a, b, c = my_list  # Unpacking values from a list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
#You can also use the * operator to unpack values into a variable.
#Example:
my_list = [1, 2, 3, 4, 5]
a, *b = my_list  # Unpacking the first value into 'a' and the rest into 'b'
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]
#You can also use the ** operator to unpack values into a dictionary.
#Example:
my_dict = {"name": "John", "age": 30}
a, b = my_dict  # Unpacking the keys of the dictionary into 'a' and 'b'
print(a)  # Output: name
print(b)  # Output: age
#You can also use the ** operator to unpack values into a dictionary.
my_dict = {"name": "John", "age": 30}
a, b = my_dict.values()  # Unpacking the values of the dictionary into 'a' and 'b'
print(a)  # Output: John
print(b)  # Output: 30

             #-----Python - Global Variables------
#A global variable is a variable that is defined outside of any function and can be accessed from anywhere in your Python code — inside or outside functions.
# and a function is a block of code that performs a specific task and can be called to execute that task.
#A function is like a mini-program inside your program. It helps you organize your code, avoid repetition, and make your work easier to understand and maintain.
#Example of a function 
def greet():
    print("Hello, welcome to Python!")

greet()  # This calls the function

#def greet(): defines a function named greet. #def stands for define. It tells Python “I’m about to create a function and give it a name.”
#greet() is the function call — it runs the code inside the function.

#Example with Input:
def greet_user(name):
    print("Hello, " + name + "!")

user_name = input("Enter your name: ")
greet_user(user_name)
#Functions can also return values using the return statement.
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)  # Calling the function and storing the result
print("The sum is:", result)  # Output: The sum is: 15
#Global variables are defined outside of any function and can be accessed by any function in the same module.
#Global variables are useful when you need to share data across multiple functions or modules.
#Example:
global_var = "I am a global variable"  # This is a global variable
def my_function():
    print(global_var)  # Accessing the global variable inside a function
my_function()  # Output: I am a global variable

x = 10  # This is a global variable

def show():
    print("Value of x is:", x)

show()
# Output: Value of x is: 10

count = 0

def increase():
    global count
    count += 1

increase()
print(count)
# Output: 1

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
# Output: Python is awesome

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# Output: Python is awesome
# In this example, the variable x inside myfunc() is local to that function, while the x outside is global.
# If you want to change the value of a global variable inside a function, you need to use the global keyword.
# Example:
x = "awesome"
def myfunc():
    global x  # Declare x as a global variable
    x = "fantastic"  # Change the value of the global variable
myfunc()
print("Python is " + x)
# Output: Python is fantastic
# In this example, the global keyword allows the function to modify the global variable x.


                 #----Python - Local Variables------
#A local variable is a variable that is defined inside a function and can only be accessed within that function.
#Local variables are created when the function is called and destroyed when the function exits.
#Example:
def my_function():
    local_var = "I am a local variable"  # This is a local variable
    print(local_var)  # Accessing the local variable inside the function
my_function()  # Output: I am a local variable
# print(local_var)  # This would raise an error because local_var is not accessible outside the function
#Local variables are useful for temporary data that is only needed within a specific function.
#Example with Input:
def calculate_area(length, width):
    area = length * width  # area is a local variable
    return area
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = calculate_area(length, width)  # Calling the function and storing the result
print("The area is:", area)  # Output: The area is: (calculated value)

                  #---Python Data Types------
#In Python, data types are the categories of values that tell the interpreter what kind of data you're working with
#Common data types in Python include:
#1. Integers (int): Whole numbers, both positive and negative, without decimals.
#   Example: 5, -10, 0
#2. Floating-point numbers (float): Numbers with decimal points.
#   Example: 3.14, -0.001, 2.0
#3. Strings (str): Sequences of characters enclosed in single or double quotes.
#   Example: "Hello", 'Python', "123"
#4. Booleans (bool): Represents True or False values.
#   Example: True, False
#5. Lists: Ordered collections of items that can be of different data types.
#   Example: [1, 2, 3], ["apple", "banana", "cherry"], [1, "two", 3.0]
#6. Tuples: Similar to lists, but immutable (cannot be changed after creation).
#   Example: (1, 2, 3), ("apple", "banana"), (1, "two", 3.0)
#7. Dictionaries (dict): Collections of key-value pairs, where each key is unique.
#   Example: {"name": "John", "age": 30}, {"fruit": "apple", "color": "red"}
#8. Sets: Unordered collections of unique items.
#   Example: {1, 2, 3}, {"apple", "banana", "cherry"}
#9. None: Represents the absence of a value or a null value.
#   Example: None

                       #-----Python Numbers------
#In Python, numbers can be of different types, including integers and floating-point numbers.
#1. Integers (int): Whole numbers without a decimal point.
#   Example: 5, -10, 0
#2. Floating-point numbers (float): Numbers with a decimal point.
#   Example: 3.14, -0.001, 2.0
#3. Complex numbers: Numbers with a real and imaginary part, represented as a + bj.
#   Example: 2 + 3j, where 2 is the real part and 3 is the imaginary part.
#You can perform various arithmetic operations on numbers in Python, such as addition, subtraction, multiplication, and division.
#Example:
a = 10  # Integer
b = 3.5  # Floating-point number
sum_result = a + b  # Addition
difference_result = a - b  # Subtraction
product_result = a * b  # Multiplication
quotient_result = a / b  # Division
print("Sum:", sum_result)  # Output: Sum: 13.5
print("Difference:", difference_result)  # Output: Difference: 6.5
print("Product:", product_result)  # Output: Product: 35.0
print("Quotient:", quotient_result)  # Output: Quotient: 2.857142857142857
#You can also use the ** operator for exponentiation (raising to a power).
exponent_result = a ** 2  # a raised to the power of 2
print("Exponent:", exponent_result)  # Output: Exponent: 100
#Python also supports mathematical functions like square root, absolute value, and more through the math module.
import math
sqrt_result = math.sqrt(a)  # Square root of a
print("Square root:", sqrt_result)  # Output: Square root: 3.1622776601683795
#----Python - Type Conversion------
#Type conversion in Python allows you to change the data type of a value from one type to another.
#This is useful when you need to perform operations that require specific data types.
#There are several built-in functions for type conversion:
#1. int(): Converts a value to an integer.
#   Example: int(3.14) will convert the float 3.14 to the integer 3.
#2. float(): Converts a value to a floating-point number.
#   Example: float(5) will convert the integer 5 to the float 5.0.
#3. str(): Converts a value to a string.
#   Example: str(100) will convert the integer 100 to the string "100".
#4. bool(): Converts a value to a boolean (True or False).
#   Example: bool(0) will convert the integer 0 to False, while bool(1) will convert it to True.
#5. list(): Converts a value to a list.
#   Example: list("hello") will convert the string "hello" to a list of characters ['h', 'e', 'l', 'l', 'o'].
#6. tuple(): Converts a value to a tuple.
#   Example: tuple([1, 2, 3]) will convert the list [1, 2, 3] to the tuple (1, 2, 3).
#Example of Type Conversion:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

               #---Random Numbers in Python------
#Python provides a built-in module called random that allows you to generate random numbers.
#You can use this module to generate random integers, floating-point numbers, and even random choices from a list.
#Example:
import random
print(random.randrange(1, 10))
#This will generate a random integer between 1 and 9 (inclusive of 1, exclusive of 10).
#You can also generate random floating-point numbers using the random.uniform() function.
random_float = random.uniform(1.0, 10.0)  # Generates a random float between 1.0 and 10.0
print(random_float)
#You can also use random.choice() to select a random element from a list.
my_list = [1, 2, 3, 4, 5]
random_choice = random.choice(my_list)  # Selects a random element from the list
print(random_choice)



              #---What is Python Casting?---
#Casting in Python means converting one data type into another. For example, turning a string into a number, or a float into an integer.
#You can use built-in functions like int(), float(), and str() to perform casting.
#Why Use Casting?
#Sometimes you get data in the wrong format (like user input from input() which is always a string), 
# and you need to convert it to do calculations or comparisons.
#Example of Casting:
age_str = input("Enter your age: ")  # User input is always a string
age = int(age_str)  # Convert the string to an integer
print("Your age is:", age)  # Now you can use age as a number
#--- Convert string to integer:
age = "26"
age_number = int(age)
print(age_number + 1)  # Output: 27

#--Convert float to integer:--
price = 99.99
whole_price = int(price)
print(whole_price)  # Output: 99

#-- Convert number to string:--
score = 100
message = "Your score is " + str(score)
print(message)
# Output: Your score is 100
#---Convert string to float:---
height = "5.9"
height_float = float(height)
print(height_float + 0.1)  # Output: 6.0
#---Convert integer to float:---
age = 30
age_float = float(age)
print(age_float + 0.5)  # Output: 30.5

                   #---Python Strings------
#A string in Python is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").
#Strings can contain letters, numbers, symbols, and spaces.
#Example:
greeting = "Hello, World!"  # A simple string

             #---Quotes Inside Quotes------
#You can use single quotes inside double quotes or vice versa to include quotes in a string.
quote = "He said, 'Python is great!'"  # Using single quotes inside double quotes
quote2 = 'She replied, "Yes, it is!"'  # Using double quotes inside single quotes

                  #---Multiline Strings------
#You can create multiline strings using triple quotes (''' ''' or """ """).
multiline_string = """This is a string
that spans multiple lines.
You can write anything here,
including line breaks."""

             #---Looping Through a String-----
#You can loop through each character in a string using a for loop.
for char in greeting:
    print(char)  # This will print each character in the string on a new line

for x in "banana":
  print(x)

#---String Length------
a = "Hello, World!"
print(len(a))

# The len() function returns the length of a string, which is the number of characters it contains.

               #---String Indexing------
#You can access individual characters in a string using indexing.
#Indexing starts at 0, so the first character is at index 0, the second at index 1, and so on.
first_char = greeting[0]  # Accessing the first character
second_char = greeting[1]  # Accessing the second character
print(first_char)  # Output: H
print(second_char)  # Output: e
#---Negative Indexing------
#You can also use negative indexing to access characters from the end of the string.
last_char = greeting[-1]  # Accessing the last character
second_last_char = greeting[-2]  # Accessing the second last character
print(last_char)  # Output: !
print(second_last_char)  # Output: d

   #-----Check String---------
#You can check if a substring exists within a string using the 'in' keyword.
#Example
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
#This will output: True, because "free" is indeed present in the string.
#You can also check if a substring is not present using 'not in'.
print("expensive" not in txt)  # This will output: True, because "expensive" is not in the string.

         #---String Slicing------
#You can extract a part of a string using slicing.
#Slicing allows you to specify a start index and an end index to get a substring.
#Example:
b = "Hello, World!"
print(b[2:5])
#This will output: "llo", which is the substring from index 2 to index 4 (the end index is exclusive).
#You can also omit the start or end index to slice from the beginning or to the end of the string.
print(b[:5])  # Output: "Hello" (from the start to index 4)
print(b[7:])  # Output: "World!" (from index 7 to the end)
b = "Hello, World!"
print(b[2:])
#This will output: "llo, World!", which is the substring from index 2 to the end of the string.
#You can also use negative indexing in slicing.
print(b[-6:-1])  # Output: "World" (from index -6 to -2, excluding the last character)
b = "Hello, World!"
print(b[-5:-2])
#This will output: "orl", which is the substring from index -5 to -3 (the end index is exclusive).
#You can also use the step parameter in slicing to skip characters.
print(b[0:5:2])  # Output: "Hlo" (every second character from index 0 to 4)
#In this example, the slice starts at index 0, goes to index 4, and skips every second character.
#You can also use negative step to reverse the string.
print(b[::-1])  # Output: "!dlroW ,olleH" (the entire string reversed)
#In this example, the slice starts at the end of the string and goes to the beginning, effectively reversing it.
#You can also use slicing to create a new string with specific characters.
new_string = b[0:5] + " Python"  # Concatenating a substring with another string
print(new_string)  # Output: "Hello Python"
#You can also use slicing to create a new string with specific characters.
#Example:
new_string = b[7:12] + " is great!"  # Concatenating a substring with another string
print(new_string)  # Output: "World is great!"
#You can also use slicing to create a new string with specific characters.
#Example:
new_string = b[0:5] + " Python"  # Concatenating a substring with another string
print(new_string)  # Output: "Hello Python
#You can also use slicing to create a new string with specific characters.
#Example:
new_string = b[7:12] + " is great!"  # Concatenating a substring with another string
print(new_string)  # Output: "World is great!"


                        #--Python - Modify Strings
#You can modify strings in Python using various string methods.
#1. Changing Case:
#You can change the case of a string using methods like upper(), lower(), title(), and capitalize().
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.title())  # Capitalizes the first letter of each word
print(a.capitalize())  # Capitalizes the first letter of the string
#2. Stripping Whitespace:
#You can remove leading and trailing whitespace from a string using the strip() method.
b = "   Hello, World!   "
print(b.strip())  # Removes leading and trailing whitespace
#3. Replacing Substrings:
#You can replace a substring within a string using the replace() method.
c = "Hello, World!"
print(c.replace("World", "Python"))  # Replaces "World" with "Python"
#4. Splitting and Joining:
#You can split a string into a list of substrings using the split() method.
d = "Hello, World!"
print(d.split(", "))  # Splits the string at ", " and returns a list of substrings
#You can also join a list of strings into a single string using the join() method.
e = ["Hello", "World"]
print(", ".join(e))  # Joins the list with ", " and returns a single string


           #----Python - String Concatenation
#String concatenation is the process of joining two or more strings together to create a new string.
#Example:
a = "Hello"
b = "World"
c = a + b
print(c)
#This will output: HelloWorld, which is the result of concatenating the two strings.
#You can also add a space or any other character between the strings during concatenation.
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#This will output: Hello World, which is the result of concatenating the two strings with a space in between.

              #---What Does Python - Format - Strings Mean?--
#String formatting in Python means inserting variables or values into a string in a clean and readable way. 
# It helps you build dynamic messages or outputs.
#There are several ways to format strings in Python:
#1. Using f-strings (Python 3.6+):
name = "Mayor M"
age = 27
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
# This will output: My name is Mayor M and I am 27 years old.
#2. Using the format() method:
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# This will output: My name is Mayor M and I am 27 years old.
#3. Using the % operator (old style):
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)
# This will output: My name is Mayor M and I am 27 years old.


#----- What Are Escape Characters in Python?--
#Escape characters in Python are special sequences that allow you to include 
# characters in a string that would otherwise be difficult or impossible to type directly.
#They start with a backslash (\) and are used to represent characters like newlines, tabs, quotes, and more.
#Common escape characters include:
#1. \n: Newline (moves to the next line)
#2. \t: Tab (inserts a tab space)
#3. \\: Backslash (to include a backslash in the string)
#4. \': Single quote (to include a single quote in a string enclosed by single quotes)
#5. \": Double quote (to include a double quote in a string enclosed by double quotes)
#Example:
text = "Hello,\nWorld!"  # Using \n for a newline
print(text)
text_with_tab = "Hello,\tWorld!"  # Using \t for a tab space
print(text_with_tab)
text_with_quotes = "He said, \"Python is great!\""  # Using \" for double quotes
print(text_with_quotes)
#You can also use escape characters to include special characters in a string.
#Example:
special_characters = "This is a backslash: \\\\ and this is a single quote: \'"
print(special_characters)
#This will output: This is a backslash: \ and this is a single quote: '