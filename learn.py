
                #----Introduction to Python Programming Language----
#Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility.
# It was created by Guido van Rossum and first released in 1991.
# Python emphasizes code readability with a clean and easy-to-understand syntax, making it ideal for both beginners and professionals.
# Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
# It has a large standard library and a vibrant ecosystem of third-party packages,
# making it suitable for a wide range of applications, from web development to data analysis and machine learning.

             #Why is Python Commonly Used in:
#1. Statistics
#   - Python is widely used in statistics due to its powerful libraries like NumPy, pandas, and SciPy,
#     which provide tools for data manipulation, analysis, and statistical modeling.
#   - It allows statisticians to perform complex calculations, visualize data, and build statistical models efficiently.

#2. Data Science & Machine Learning.
#   - Python is a popular choice in data science and machine learning because of its simplicity and extensive libraries like scikit-learn, TensorFlow, and PyTorch.
#   - It provides tools for data preprocessing, feature engineering, model training, and evaluation,
#     making it easier for data scientists to build and deploy machine learning models.

#3. Web Development & Software Development.
#   - Python is commonly used in web development with frameworks like Django and Flask, which simplify the process of building web applications.
#   - It is also used in software development for scripting, automation, and building desktop applications with libraries like Tkinter and PyQt.
#   - Python's readability and ease of use make it a preferred language for rapid application development.



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
#This will output: This is a backslash: \ and this is a single quote: 

       #------Python Lists---
#A list in Python is a collection of items that can be of different data types, such as numbers, strings, or even other lists.
#Lists are ordered, meaning the items have a specific order, and they are mutable, meaning you can change their content.
#You can create a list by placing items inside square brackets [] and separating them with commas.
my_list = [1, 2, 3, "apple", "banana", 4.5]  # A list with mixed data types
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#This will output: 3, which is the number of items in the list.
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#This will output: <class 'list'>, indicating that mylist is a list.
#You can access individual items in a list using indexing, just like with strings.
print(my_list[0])  # Accessing the first item (index 0)
print(my_list[3])  # Accessing the fourth item (index 3)

    #------Python Collections (Arrays)-------------
#In Python, a collection is a data structure that allows you to store multiple items in a single variable.
#There are several types of collections in Python, including:
#1. Lists: Ordered collections of items that can be of different data types.
#   Example: my_list = [1, 2, 3, "apple", "banana"]
#2. Tuples: Similar to lists, but immutable (cannot be changed after creation).
#   Example: my_tuple = (1, 2, 3, "apple", "banana")
#3. Sets: Unordered collections of unique items.
#   Example: my_set = {1, 2, 3, "apple", "banana"}
#4. Dictionaries: Collections of key-value pairs, where each key is unique.
#   Example: my_dict = {"name": "John", "age": 30, "city": "New York"}
#5. Arrays: Similar to lists, but can only contain items of the same data type.
#   Example: You can use the array module to create an array of integers.
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])  # 'i' indicates an array of integers.

# ---Python If ... Else------
#The if...else statement in Python is used to make decisions in your code based on certain conditions.
#It allows you to execute different blocks of code depending on whether a condition is true or false.
#Example:
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#In this example, if the age is 18 or older, it prints "You are an adult." Otherwise, it prints "You are a minor."

  #----Python Conditions and If statements--
#You can use multiple conditions with elif (else if) to check for additional conditions.
#Example:
age = 16
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
#In this example, it checks if the age is less than 13, then checks if it's less than 18, and finally defaults to "You are an adult."
#You can also use logical operators like and, or, and not to combine conditions.
#Example:
age = 20
is_student = True
if age >= 18 and is_student:
    print("You are an adult student.")
else:
    print("You are either not an adult or not a student.")
#In this example, it checks if the age is 18 or older and if the person is a student. If both conditions are true, it prints "You are an adult student."

a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

   #---The pass Statement---
#The pass statement in Python is a null operation; it does nothing when executed.
#It is used as a placeholder in situations where you need a statement syntactically but don't want to execute any code.
#For example, you might use it in an if statement or a function definition that you plan to implement later.
#Example:
def my_function():
    pass  # This function does nothing for now
if True:
    pass  # This block does nothing for now
#You can also use pass in loops or classes where you want to define a structure but haven't implemented it yet.
#Example:
class MyClass:
    pass  # This class is empty for now
#Using pass allows you to write code that is syntactically correct without having to fill in the details immediately.
#It helps you avoid syntax errors while you plan or develop your code further.

    #  ---Python Match---
#The match statement is used to perform different actions based on different conditions.
          #  -- The Python Match Statement--
#It allows you to perform pattern matching, which is similar to switch statements in other languages but much more flexible and expressive.
#The match statement checks a value (called the subject) against a series of patterns and executes the block of code for the first pattern that matches.
#Example:
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"
#In this example, the match statement checks the value of code against different patterns (200, 404, 500).
#If it matches one of the cases, it returns the corresponding message. The case _ acts as a default case, similar to the else statement.
#You can also use match statements with more complex patterns, such as tuples or lists.
#Example:
point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
#In this example, the match statement checks the point against different patterns to determine its position in a 2D coordinate system.
#The match statement is a powerful feature in Python that allows you to write cleaner and more readable code when dealing with multiple conditions.
#It can be used to simplify complex if-elif-else chains and make your code more maintainable.

#examples 

match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
#it does contain a logic issue when used in a match statement in Python.
#This will not work as expected because x, y, and z are treated as capture patterns, not constants.
# That means Python will always match the first case, because it thinks you're trying to assign value to x
#The match statement evaluates the expression and checks it against each case.
#If the expression matches a case, the corresponding code block is executed.
#If no cases match, the code block under case _ (the default case) is executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
##In this example, the match statement checks the value of day and prints the corresponding day of the week.

           #---Python While Loop--
#A while loop in Python is used to repeatedly execute a block of code as long as a specified condition is true.
#It allows you to perform actions until a certain condition is no longer met.
#Python Loops

#Python has two primitive loop commands:
#1while loops
#2for loops
#Example:

    #The while Loop
#The while loop continues to execute as long as the specified condition is true.
count = 0  # Initialize a counter variable
while count < 5:  # Condition to check
    print("Count is:", count)  # Print the current value of count
    count += 1  # Increment the counter by 1
#In this example, the while loop will continue to execute as long as count is less than 5.
#It will print the current value of count and increment it by 1 in each iteration.
#When the condition becomes false (when count reaches 5), the loop will stop executing.

#Example:
i = 1
while i < 6:
  print(i)
  i += 1
#In this example, the while loop will print the numbers from 1 to 5.
#If you want to stop the loop before the condition becomes false, you can use the break statement.
#The break statement is used to exit the loop immediately, regardless of the condition.
#Example:
count = 0
while count < 5:
    if count == 3:  # Check if count is equal to 3
        break  # Exit the loop when count is 3
    print("Count is:", count)
    count += 1
#In this example, the loop will stop executing when count reaches 3, and it will not print "Count is: 3".

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#In this example, the while loop will print the numbers from 1 to 2 and then stop when i equals 3.
#You can also use the continue statement to skip the current iteration and move to the next one.
#The continue statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.
#Example:
count = 0
while count < 5:
    count += 1  # Increment the counter by 1
    if count == 3:  # Check if count is equal to 3
        continue  # Skip the rest of the code for this iteration
    print("Count is:", count)  # Print the current value of count
#In this example, the loop will skip printing "Count is: 3" and continue with the next iteration.
#In this example, the while loop will print the numbers from 1 to 5, but it will skip printing "Count is: 3".

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#In this example, the while loop will print the numbers from 1 to 6, but it will skip printing "3".
#You can also use the else statement with a while loop.
#The else statement is executed when the loop condition becomes false, meaning the loop has completed all iterations without being interrupted by a break statement.
#Example:
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
else:
    print("Loop has completed all iterations.")
#In this example, the else block will execute after the while loop has completed all iterations, printing "Loop has completed all iterations."
#In this example, the while loop will print the numbers from 1 to 5, and then the else block will execute, printing "Loop has completed all iterations."
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#In this example, the while loop will print the numbers from 1 to 5, and then the else block will execute, printing "i is no longer less than 6".

     #  ---Python For Loop---
#A for loop in Python is used to iterate over a sequence (like a list, tuple, string, or range) 
# and execute a block of code multiple times, once for each item in the sequence.
for item in sequence:
    # do something with item
#Example:
#Using a for loop to iterate over a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
#In this example, the for loop iterates over each item in the fruits list and prints a message for each fruit.

#You can also use a for loop to iterate over a string.
for i in range(5):
    print(i)
#In this example, the for loop iterates over a range of numbers from 0 to 4 (5 is exclusive) and prints each number.


for letter in "Python":
    print(letter)
#In this example, the for loop iterates over each character in the string "Python" and prints each letter.

for x in "banana":
  print(x)
#In this example, the for loop iterates over each character in the string "banana" and prints each letter.

#----The break Statement--
#The break statement is used to exit a loop prematurely, meaning it stops the loop even if the condition is still true.
#Example:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#In this example, the for loop will print "apple" and "banana", but it will stop when it reaches "banana" due to the break statement.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#In this example, the for loop will stop when it reaches "banana" and will not print "banana" or "cherry".
#You can also use the continue statement to skip the current iteration and move to the next one.
#The continue statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.
#Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#In this example, the for loop will skip printing "banana" and will print "apple" and "cherry".
#You can also use the else statement with a for loop.
#The else statement is executed when the loop has completed all iterations without being interrupted by a break statement.
#Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
else:
    print("Loop has completed all iterations.")
#In this example, the else block will execute after the for loop has completed all iterations, printing "Loop has completed all iterations."
#In this example, the for loop will print "apple", "banana", and "cherry", and then the else block will execute, printing "Loop has completed all iterations."


            #---The range() Function--
#To loop through a set of code a specified number of times, we can use the range() function,
#which generates a sequence of numbers.
#The range() function can take one, two, or three arguments:
#1. range(stop): Generates numbers from 0 to stop-1.
#2. range(start, stop): Generates numbers from start to stop-1.
#3. range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.
#Example:
for x in range(6):
  print(x)
#In this example, the for loop will print numbers from 0 to 5 (6 is exclusive).
for x in range(2, 6):
  print(x)
#In this example, the for loop will print numbers from 2 to 5 (6 is exclusive).
for x in range(2, 30, 3):
  print(x)
#In this example, the for loop will print numbers from 2 to 29, incrementing by 3 each time.
#You can also use the range() function to create a list of numbers.
numbers = list(range(10))  # Creates a list of numbers from 0 to 9
print(numbers)
#In this example, the list() function converts the range object into a list of numbers from 0 to 9.
#You can also use the range() function to create a list of even or odd numbers.
even_numbers = list(range(0, 20, 2))  # Creates a list of even numbers from 0 to 18
print(even_numbers)
odd_numbers = list(range(1, 20, 2))  # Creates a list of odd numbers from 1 to 19
print(odd_numbers)
#In this example, the range() function generates a list of even numbers from 0 to 18 and a list of odd numbers from 1 to 19.
#You can also use the range() function to create a list of numbers in reverse order.
reverse_numbers = list(range(10, 0, -1))  # Creates a list of numbers from 10 to 1
print(reverse_numbers)
#In this example, the range() function generates a list of numbers from 10 to 1 in reverse order.

   #----Else in For Loop---~
#You can use the else statement with a for loop to execute a block of code after the loop has completed all iterations.
#The else block will execute only if the loop has not been interrupted by a break statement.
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#In this example, the for loop will print numbers from 0 to 5, and then the else block will execute, printing "Finally finished!".
#You can also use the else statement with a for loop to execute a block of code after the loop has completed all iterations.
for x in range(2, 6):
  print(x)
else:
    print("Loop has completed all iterations.")
#In this example, the for loop will print numbers from 2 to 5, and then the else block will execute, printing "Loop has completed all iterations.".

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#In this example, the for loop will print numbers from 0 to 2, and then it will stop when it reaches 3 due to the break statement.
# The else block will not execute because the loop was interrupted by the break statement.

          #~~~~~~~~Nested Loops~~~~~~~~
#Nested loops are loops inside other loops. They allow you to iterate over multiple sequences or perform complex iterations.
#Example:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#In this example, the outer loop iterates over the list of adjectives, and for each adjective, the inner loop iterates over the list of fruits.
#This will print all combinations of adjectives and fruits.

            #~~~~~~~~Python Functions~~~~~~
#A function in Python is a reusable block of code that performs a specific task.
#You define it once and can use (or "call") it as many times as needed.
#Creating a Function
#To create a function, you use the def keyword followed by the function name and parentheses.
#In Python a function is defined using the def keyword:
def function_name(parameters):
    # code block
    return value  # Optional return statement
#Example:
def greet(name):
    print("Hello, " + name + "!")
#In this example, the function greet takes one parameter (name) and prints a greeting message.
#Calling a Function
#To use a function, you simply call it by its name and pass any required arguments.
greet("Alice")  # Calling the function with the argument "Alice"
#In this example, the function greet is called with the argument "Alice", and it will print "Hello, Alice!".
#You can also call the function with different arguments.
greet("Bob")  # Calling the function with the argument "Bob"
#In this example, the function greet is called with the argument "Bob", and it will print "Hello, Bob!".
#You can also define functions that return a value using the return statement.
def add(a, b):
    return a + b  # Returns the sum of a and b
#In this example, the function add takes two parameters (a and b) and returns their sum.
result = add(5, 3)  # Calling the function with arguments 5 and 3
print("Sum:", result)  # Output: Sum: 8
#In this example, the function add is called with the arguments 5 and 3, and it returns their sum (8), which is then printed.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
my_function("Tobias", "Refsnes")  # Calling the function with two arguments
my_function("Linus", "Tobias", "Refsnes")  # Calling the function with three arguments
#In this example, the function my_function is called with different numbers of arguments.


       #~~~Recursion~~~~~~
#Recursion is a programming technique where a function calls itself to solve a problem.
#Recursion is a programming technique where a function calls itself to solve a smaller version of a problem, until it reaches a base case that stops the recursion.
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call
#In this example, the function factorial calculates the factorial of a number n by calling itself with a smaller value (n - 1) until it reaches the base case (0 or 1).
def factorial(n):
    if n == 0:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))  # Output: 120
#In this example, the function factorial is called with the argument 5, and it returns the factorial of 5 (120).
#Recursion can be powerful, but it can also lead to performance issues if not used carefully, especially with deep recursion.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
#In this example, the function tri_recursion calculates the sum of numbers from k down to 0 using recursion.
#It prints the intermediate results as it goes through the recursive calls.

     #~~~~~~Python Arrays~~~~~~
#An array is a collection of items stored at contiguous memory locations.
#An array is a special variable, which can hold more than one value at a time
#In Python, you can use the array module to create arrays, but lists are more commonly used for similar purposes.
import array as arr
#Creating an array of integers
my_array = arr.array('i', [1, 2, 3, 4, 5])  # 'i' indicates an array of integers
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5])


  #----Python OOP------
#Object-Oriented Programming (OOP) is a programming paradigm that uses objects to represent data and methods to manipulate that data.
#In Python, you can create classes to define objects and their behavior.
#A class is a blueprint for creating objects, and an object is an instance of a class
#Creating a Class
class MyClass:
    x = 5  # Class attribute
#In this example, MyClass is a class with a class attribute x set to 5.
#Creating an Object
my_object = MyClass()  # Creating an instance of MyClass
print(my_object.x)  # Accessing the class attribute x
#In this example, my_object is an instance of MyClass, and it can
access the class attribute x, which is 5.
#You can also define methods (functions) within a class to perform actions on the object's data.
class MyClass:
    def greet(self, name):
        print("Hello, " + name + "!")  # Method to greet a person
#In this example, MyClass has a method greet that takes a name as a parameter and prints a greeting message.


#-----Python Polymorphism---
#Polymorphism is a concept in OOP that allows objects of different classes to be treated as objects of a common superclass.
#It allows you to define methods in a class that can be
#used by objects of different classes, enabling flexibility and code reuse.
class Animal:
    def speak(self):
        pass  # Base method to be overridden by subclasses
class Dog(Animal):
    def speak(self):
        return "Woof!"  # Dog's implementation of speak method
class Cat(Animal):
    def speak(self):
        return "Meow!"  # Cat's implementation of speak method
#In this example, the Animal class has a base method speak that is overridden by the Dog and Cat subclasses.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
#In this example, the thisdict dictionary has three key-value pairs, and the len() function returns the number of items in the dictionary, which is 3.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
#In this example, the Car, Boat, and Plane classes have a method move that is called on each object in the loop, demonstrating polymorphism.
#The move method is defined in each class, and when called, it prints a message specific to the type of vehicle.

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
#In this example, the Vehicle class is a base class, and Car, Boat, and Plane are subclasses that inherit from it.
#The move method is overridden in the Boat and Plane classes, demonstrating polymorphism.

       ##---Python Modules
#A module in Python is a file containing Python code that can define functions, classes, and variables.
#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.
#You can create your own modules or use built-in modules provided by Python.
#Creating a Module
#To create a module, simply create a Python file with a .py extension and define functions
# or classes in it.
#For example, create a file named my_module.py with the following content:
def greet(name):
    print("Hello, " + name + "!")  # Function to greet a person
#In this example, my_module.py defines a function greet that takes a name as a parameter and prints a greeting message.
#Using a Module
#To use a module, you can import it into your Python script using the import statement.
import my_module  # Importing the module
my_module.greet("Alice")  # Calling the function from the module
#In this example, the my_module module is imported, and the greet function is called with the argument "Alice", printing "Hello, Alice!".
#You can also import specific functions or classes from a module using the from keyword.
from my_module import greet  # Importing the greet function from the module
greet("Bob")  # Calling the function directly
#In this example, the greet function is imported directly from the my_module module, allowing you to call it without prefixing it with the module name.

        #Variables in Module
#You can also define variables in a module and use them in your script.
my_variable = "Hello, World!"  # Variable in the module
#In the my_module.py file, you can define a variable like this:
def greet(name):
    print("Hello, " + name + "!")  # Function to greet a person
my_variable = "Hello, World!"  # Variable in the module
#In your script, you can access the variable like this:
import my_module  # Importing the module
print(my_module.my_variable)  # Accessing the variable from the module
#In this example, the my_variable variable is defined in the my_module module, and it can be accessed in your script after importing the module.


                  #----Python PIP---
#PIP (Python Package Installer) is a package manager for Python that allows you to install 
# and manage additional libraries and dependencies that are not part of the standard Python library.
# PIP is a package manager for Python packages, or modules if you like.
# It allows you to install and manage additional libraries and dependencies that are not part of the standard Python library.              
#What is a Package?
#A package is a collection of modules that are organized in a specific way to provide functionality.
#Packages can be installed using PIP, and they can be used in your Python scripts to extend functionality.
#Installing Packages
#To install a package using PIP, you can use the following command in your terminal or command prompt:
pip install package_name  # Replace package_name with the name of the package you want to install
#For example, to install the requests package, you would run:
pip install requests
#In this example, the requests package is installed, which allows you to make HTTP requests in your Python scripts.
#Using Installed Packages
#After installing a package, you can import it into your Python script and use its functionality.
import requests  # Importing the requests package
response = requests.get("https://api.example.com/data")  # Making a GET request
print(response.json())  # Printing the JSON response
#In this example, the requests package is imported, and a GET request is made to a specified URL. The JSON response is then printed.

# #Handling files in python
#Python File Open
#To open a file in Python, you can use the built-in open() function.
#The open() function takes two arguments: the file name and the mode in which you want to open the file.
#The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'b' for binary mode.
#Example:
#Opening a file for reading
file = open("example.txt", "r")  # Open the file in read mode
#Reading the contents of the file
content = file.read()  # Read the entire file content
print(content)  # Print the content of the file
#Closing the file
file.close()  # Close the file after reading
#In this example, the file "example.txt" is opened in read mode, its contents are read and printed, and then the file is closed.
#Opening a file for writing
file = open("output.txt", "w")  # Open the file in write mode
#Writing to the file
file.write("Hello, World!\n")  # Write a line to the file
file.write("This is a test file.\n")  # Write another line to the file
#Closing the file
file.close()  # Close the file after writing
#In this example, a new file "output.txt" is created (or overwritten if it already exists) in write mode, and two lines are written to it.
#Opening a file for appending
file = open("output.txt", "a")  # Open the file in append mode
#Appending to the file
file.write("This line is appended to the file.\n")  # Append a line to the file
#Closing the file
file.close()  # Close the file after appending
#In this example, the existing file "output.txt" is opened in append mode, and a new line is added to the end of the file.
#Python Delete File
#To delete a file in Python, you can use the os module's remove() function.
import os  # Importing the os module
#Deleting a file
if os.path.exists("output.txt"):  # Check if the file exists
    os.remove("output.txt")  # Delete the file
    print("File deleted successfully.")
else:
    print("The file does not exist.")
#In this example, the os module is imported, and the remove() function is used to delete the file "output.txt" if it exists.


          #---Python exercises---
#1. Write a Python program to find the largest of three numbers.
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
#Example usage
print("Largest of 3 numbers:", largest_of_three(10, 20, 30))  # Output: 30

#2. Write a Python program to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#Example usage
print("Is 29 prime?", is_prime(29))  # Output: True
#3. Write a Python program to calculate the factorial of a number.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
#Example usage
print("Factorial of 5:", factorial(5))  # Output: 120

#4.Create and Print Variables
#Create variables to store your name (string), age (integer), and height in meters (float).
#Print a sentence using these variables, e.g., "My name is [name], I am [age] years old, and my height is [height] meters."
#Use the type() function to print the data type of each variable.

name = "Simon Madeba Odhiambo"
age = 25
height = 1.75

# Printing a sentence using the variables
print(f"My name is {name}, I am {age} years old, and my height is {height} meters.")

# Printing the data types of each variable
print("Data types:")
print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))

#Variable Reassignment
#Create a variable score and assign it the value 100.
#Reassign score to 150 and print it.
#Create a boolean variable is_active set to True and print it.
score = 100
print("Initial score:", score)
# Reassigning the score variable
score = 150
print("Reassigned score:", score)
# Creating a boolean variable
is_active = True
print("Is active:", is_active)

#5 Assign three different values (e.g., 10, 20, 30) to three variables (x, y, z) in a single line.
#Print all three variables.
#Assign the same string value (e.g., "Python") to three variables (a, b, c) in a single line and print them.
x, y, z = 10, 20, 30
print("Values of x, y, z:", x, y, z)
a = b = c = "Python"
print("Values of a, b, c:", a, b, c)

#6 Use input() to ask the user for their first name and last name.
#Concatenate the names with a space between them and print a greeting, e.g., "Hello, [full name]!"
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Hello, {full_name}!")

#7 Ask the user for their current age using input().
#Convert the input to an integer and calculate their age next year.
#Print a message like "Next year, you will be [age] years old."
current_age = int(input("Enter your current age: "))
next_year_age = current_age + 1
print(f"Next year, you will be {next_year_age} years old.")

#8. Create a string variable with the value "Python Programming".
#Use the len() function to print the length of the string.
#Print the first and last characters of the string using indexing.
my_string = "Python Programming"
string_length = len(my_string)
print("Length of the string:", string_length)
first_char = my_string[0]  # First character
last_char = my_string[-1]  # Last character
print("First character:", first_char)
print("Last character:", last_char)

#9. Create a variable price with the value 99.99.
#Convert it to a string and concatenate it with the text " dollars" (e.g., "99.99 dollars").
#Print the result.
price = 99.99
price_str = str(price) + " dollars"
print("Price:", price_str)

#10. Create a variable temperature with the value 36.6.
# Convert it to an integer and print both the original and converted values.
temperature = 36.6
temperature_int = int(temperature)
print("Original temperature:", temperature)
print("Converted temperature:", temperature_int)

#11. Create a string variable with the value "Hello, World!".
#Use slicing to print:
#The substring "Hello".
#The substring "World".
#The string in reverse order.
my_string = "Hello, World!"
hello_substring = my_string[:5]  # "Hello"
world_substring = my_string[7:12]  # "World"
reversed_string = my_string[::-1]  # "dlroW ,olleH"
print("Substring 'Hello':", hello_substring)
print("Substring 'World':", world_substring)
print("Reversed string:", reversed_string)

#12. Create a string variable with the value " Welcome to Python! ".
#Use string methods to:
#Remove leading and trailing whitespace.
#Convert the string to uppercase.
#Replace "Python" with "Programming".
#Split the string into a list of words.

my_string = " Welcome to Python! "
trimmed_string = my_string.strip()  # Remove leading and trailing whitespace
uppercase_string = trimmed_string.upper()  # Convert to uppercase
replaced_string = uppercase_string.replace("PYTHON", "PROGRAMMING")  # Replace "Python" with "Programming"
split_string = replaced_string.split()  # Split into a list of words
print("Trimmed string:", trimmed_string)
print("Uppercase string:", uppercase_string)
print("Replaced string:", replaced_string)
print("Split string:", split_string)

#13. Create a list of five fruits (e.g., ["apple", "banana", "cherry", "date", "elderberry"]).
#Print the entire list.
#Print the second and last items in the list using indexing.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Fruits list:", fruits)  # Print the entire list
print("Second fruit:", fruits[1])  # Print the second item
print("Last fruit:", fruits[-1])  # Print the last item

#14. Create a list of three numbers.
#Change the second number to 100.
#Append a new number to the list.
#Print the modified list.
numbers = [10, 20, 30]  # Create a list of three numbers
numbers[1] = 100  # Change the second number to 100
numbers.append(40)  # Append a new number to the list
print("Modified numbers list:", numbers)  # Print the modified list

#15. Create a list of numbers from 1 to 10.
#Use slicing to print:
#The first three numbers.
#The last three numbers.
#Every second number (e.g., [1, 3, 5, 7, 9]).

numbers = list(range(1, 11))  # Create a list of numbers from 1 to 10
first_three = numbers[:3]  # First three numbers
last_three = numbers[-3:]  # Last three numbers
every_second = numbers[::2]  # Every second number
print("First three numbers:", first_three)
print("Last three numbers:", last_three)
print("Every second number:", every_second)

#16. Ask the user for their age using input().
#Use if, elif, and else to categorize them as:
#"Child" if under 13.
#"Teenager" if 13–17.
#"Adult" if 18 or older.
#Print the category.

age = int(input("Enter your age: "))  # Ask the user for their age
if age < 13:
    category = "Child"
elif 13 <= age <= 17:
    category = "Teenager"
elif age >= 18:
    category = "Adult"
print("You are categorized as:", category)  # Print the category

#17. Ask the user to input a number.
#Use an if statement to check if the number is even or odd (use the modulo operator %).
#Print "Even" or "Odd" accordingly.
number = int(input("Enter a number: "))  # Ask the user for a number
if number % 2 == 0:
    print("Even")  # Print "Even" if the number is even
else:
    print("Odd")
#In this example, the user is prompted to enter a number, and the program checks if it is even or odd using the modulo operator (%).
# If the number is divisible by 2, it is even; otherwise, it is odd.

#18. Write a function check_number(num) that takes a number as input.
#Use an if statement to check if the number is positive, negative, or zero.
#For one of the conditions, use the pass statement as a placeholder.
#Print a message for the other conditions
def check_number(num):
    if num > 0:
        print("The number is positive.")  # Message for positive numbers
    elif num < 0:
        print("The number is negative.")  # Message for negative numbers
    else:
        pass  # Placeholder for zero condition
        print("The number is zero.")



#Example usage
check_number(10)  # Output: The number is positive.
check_number(-5)  # Output: The number is negative.
check_number(0)   # Output: The number is zero.
#In this example, the function check_number takes a number as input and checks if it is positive, negative, or zero.
# If the number is positive, it prints a message indicating that; if negative, it prints a different message; and if zero, it uses the pass statement as a placeholder.


#19. Use a while loop to print numbers from 1 to 10.
#Add an else block to print "Loop completed!" when the loop finishes.
i = 1
while i <= 10:
    print(i)  # Print the current number
    i += 1  # Increment the number by 1
else:
    print("Loop completed!")
#In this example, a while loop is used to print numbers from 1 to 10.
# After the loop finishes, the else block executes, printing "Loop completed!".

#20. Create a list of colors (e.g., ["red", "blue", "green"]).
#Use a for loop to print each color with a message like "I like [color]".
colors = ["red", "blue", "green"]  # Create a list of colors
for color in colors:
    print(f"I like {color}")  # Print a message for each color
#In this example, a for loop iterates over the list of colors and prints a message for each color.

#21. Write a for loop to iterate over numbers from 1 to 10.
#Use break to stop the loop at 6.
#Write another for loop to print numbers from 1 to 10 but use continue to skip 5
for i in range(1, 11):
    if i == 6:
        break  # Stop the loop at 6
    print(i)  # Print the current number
print("Loop stopped at 6.")
for i in range(1, 11):
    if i == 5:
        continue  # Skip the number 5
    print(i)  # Print the current number
#In this example, the first for loop iterates over numbers from 1 to 10 and stops when it reaches 6 using the break statement.
# The second for loop iterates over the same range but skips the number 5 using the continue statement.

#22. Create two lists: adjectives (e.g., ["big", "small"]) and nouns (e.g., ["cat", "dog"]).
#Use nested for loops to print all combinations, e.g., "big cat", "big dog", "small cat", "small dog".
adjectives = ["big", "small"]  # List of adjectives
nouns = ["cat", "dog"]  # List of nouns
for adj in adjectives:
    for noun in nouns:
        print(f"{adj} {noun}")  # Print the combination of adjective and noun
#In this example, nested for loops are used to iterate over the adjectives and nouns lists, printing all combinations of adjectives and nouns.

#23. Use range() in a for loop to:
#Print numbers from 5 to 15.
#Print even numbers from 10 to 20.
#Print numbers from 10 to 1 in reverse order.
for i in range(5, 16):
    print(i)  # Print numbers from 5 to 15
for i in range(10, 21, 2):
    print(i)  # Print even numbers from 10 to 20
for i in range(10, 0, -1):
    print(i)  # Print numbers from 10 to 1 in reverse order
#In this example, the range() function is used in a for loop to print numbers in different ranges and orders.

#24. Define a function say_hello(name) that takes a name as input and prints "Hello, [name]!".
#Call the function with two different names.
def say_hello(name):
    print(f"Hello, {name}!")  # Function to greet a person
#Example usage
say_hello("Alice")  # Output: Hello, Alice!
say_hello("Bob")  # Output: Hello, Bob!
#In this example, the function say_hello takes a name as input and prints a greeting message.

#25. Define a function square(number) that takes a number and returns its square.
#Call the function with different inputs (e.g., 4, 7) and print the results.
def square(number):
    return number ** 2  # Return the square of the number
#Example usage
print("Square of 4:", square(4))  # Output: 16
print("Square of 7:", square(7))  # Output: 49
#In this example, the function square takes a number as input and returns its square. The function is called with different inputs, and the results are printed.

#26. Write a recursive function sum_numbers(n) that calculates the sum of numbers from 1 to n.
#For example, sum_numbers(5) should return 1 + 2 + 3 + 4 + 5 = 15.
#Test the function with n=5 and n=3.
def sum_numbers(n):
    if n <= 0:
        return 0  # Base case: if n is 0 or negative, return 0
    else:
        return n + sum_numbers(n - 1)  # Recursive call to sum the numbers
#Example usage
print("Sum of numbers from 1 to 5:", sum_numbers(5))  # Output: 15
print("Sum of numbers from 1 to 3:", sum_numbers(3))  # Output: 6
#In this example, the function sum_numbers calculates the sum of numbers from 1 to n using recursion.
# The base case is when n is 0 or negative, returning 0. Otherwise, it adds n to the result of the recursive call with n - 1.

#27. Write a recursive function countdown(n) that prints numbers from n down to 1, then prints "Done!".
#Test with n=5.
def countdown(n):
    if n <= 0:
        print("Done!")  # Base case: when n is 0 or negative, print "Done!"
    else:
        print(n)  # Print the current number
        countdown(n - 1)  # Recursive call with n - 1
#Example usage
countdown(5)  # Output: 5, 4, 3, 2, 1, Done!
#In this example, the function countdown prints numbers from n down to 1 using recursion.
# The base case is when n is 0 or negative, at which point it prints "Done!". Otherwise, it prints the current number and calls itself with n - 1.

#28. Import the array module and create an array of integers (e.g., [1, 2, 3, 4]).
#Append a new number to the array.
#Print the array and its type.
import array as arr  # Importing the array module
my_array = arr.array('i', [1, 2, 3, 4])  # Create an array of integers
my_array.append(5)  # Append a new number to the array
print("Array:", my_array)  # Print the array
print("Type of array:", type(my_array))  # Print the type of the array
#In this example, the array module is imported, and an array of integers is created.
# A new number is appended to the array, and both the array and its type are printed.

#29. Create a file called greeting.txt and write "Hello, Python!" to it.
#Open the file in append mode and add another line: "I am learning file handling."
#Read and print the entire file content.
with open("greeting.txt", "w") as file:  # Create and open the file in write mode
    file.write("Hello, Python!\n")  # Write the first line to the file
with open("greeting.txt", "a") as file:  # Open the file in append mode
    file.write("I am learning file handling.\n")  # Append another line to the file
with open("greeting.txt", "r") as file:  # Open the file in read mode
    content = file.read()  # Read the entire file content
print("File content:\n", content)  # Print the content of the file
#In this example, a file named greeting.txt is created, and two lines are written to it.
# The file is then opened in read mode to read and print its content.

#30. Write a program to check if greeting.txt exists using os.path.exists().
#If it exists, delete it using os.remove() and print "File deleted."
#If it doesn’t exist, print "File not found."
import os  # Importing the os module
file_path = "greeting.txt"  # Path to the file
if os.path.exists(file_path):  # Check if the file exists
    os.remove(file_path)  # Delete the file
    print("File deleted.")
else:
    print("File not found.")
#In this example, the os module is used to check if the file greeting.txt exists.
# If it exists, the file is deleted, and a message is printed. If it doesn't exist, a different message is printed.

#31. Define a class Person with attributes name and age.
#Create a method introduce() that prints "Hi, I’m [name] and I’m [age] years old."
#Create two instances of the class and call the introduce() method for each.
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age  # Initialize the age attribute

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")  # Method to introduce the person
#Example usage
person1 = Person("Alice", 30)  # Create an instance of Person
person2 = Person("Bob", 25)  # Create another instance of Person
person1.introduce()  # Call the introduce method for person1
person2.introduce()  # Call the introduce method for person2
#In this example, a class Person is defined with attributes name and age, and a method introduce() that prints a message.
# Two instances of the class are created
# and the introduce() method is called for each instance to print their introductions.


#32. Define a base class Animal with a method sound() that uses pass.
#Create two subclasses Dog and Cat that override sound() to return "Woof!" and "Meow!", respectively.
#Create a list of Dog and Cat objects and loop through it to call sound() on each.
class Animal:
    def sound(self):
        pass  # Base method to be overridden by subclasses
class Dog(Animal):
    def sound(self):
        return "Woof!"  # Dog's implementation of sound method
class Cat(Animal):
    def sound(self):
        return "Meow!"  # Cat's implementation of sound method
#Example usage
animals = [Dog(), Cat()]  # Create a list of Dog and Cat objects
for animal in animals:
    print(animal.sound())  # Call the sound method for each animal
#In this example, a base class Animal is defined with a method sound() that uses pass.
# Two subclasses Dog and Cat are created that override the sound() method to return their respective sounds.
# A list of Dog and Cat objects is created, and the sound() method is called for each object in the list, printing their sounds.

#33. Import the random module.
#Generate and print a random integer between 1 and 100.
#Generate and print a random float between 0.0 and 1.0 using random.uniform().
import random  # Importing the random module
random_integer = random.randint(1, 100)  # Generate a random integer between 1 and 100
random_float = random.uniform(0.0, 1.0)  # Generate a random float between 0.0 and 1.0
print("Random integer:", random_integer)  # Print the random integer
print("Random float:", random_float)  # Print the random float
#In this example, the random module is imported, and a random integer between 1 and 100 is generated using randint().
# A random float between 0.0 and 1.0 is generated using uniform(), and both values are printed.

#34. Create a list of five activities (e.g., ["read", "code", "play", "sleep", "eat"]).
#Use random.choice() to select and print a random activity.

activities = ["read", "code", "play", "sleep", "eat"]  # List of activities
random_activity = random.choice(activities)  # Select a random activity from the list
print("Random activity:", random_activity)  # Print the selected random activity
#In this example, a list of activities is created, and random.choice() is used to select a random activity from the list, which is then printed.

#35. Write a function check_status(code) that takes an HTTP status code and uses a match statement to return:
#"Success" for code 200.
#"Not Found" for code 404.
#"Error" for code 500.
#"Unknown" for any other code.
#Test the function with codes 200, 404, 500, and 403.
def check_status(code):
    match code:
        case 200:
            return "Success"  # Return "Success" for code 200
        case 404:
            return "Not Found"  # Return "Not Found" for code 404
        case 500:
            return "Error"  # Return "Error" for code 500
        case _:
            return "Unknown"  # Return "Unknown" for any other code
#Example usage
print("Status code 200:", check_status(200))  # Output: Success
print("Status code 404:", check_status(404))  # Output: Not Found
print("Status code 500:", check_status(500))  # Output: Error
print("Status code 403:", check_status(403))  # Output: Unknown
#In this example, the function check_status takes an HTTP status code as input and uses a match statement to return a corresponding message based on the code.
# The function is tested with different status codes, and the results are printed.

#36. Ask the user to input a number from 1 to 7.
#Use a match statement to print the corresponding day of the week (e.g., 1 = Monday, 2 = Tuesday, etc.).
#Include a default case for invalid inputs.
def get_day_of_week(number):
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid input, please enter a number between 1 and 7."
#Example usage
try:
    user_input = int(input("Enter a number from 1 to 7: "))  # Ask the user for input
    day = get_day_of_week(user_input)  # Get the corresponding day of the week
    print("Day of the week:", day)  # Print the result
except ValueError:
    print("Invalid input, please enter a valid number.")
#In this example, the function get_day_of_week takes a number as input and uses a match statement to return the corresponding day of the week.
# If the input is not between 1 and 7, it returns an invalid input message.
# The user is prompted to enter a number, and the function is called with that input. If the input is not a valid integer, an error message is printed.

