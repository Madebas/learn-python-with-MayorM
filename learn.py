
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
