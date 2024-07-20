# Python 3 Tutorial: From Scratch to Mastery

## Table of Contents

1. Introduction to Python
   - What is Python?
   - Installing Python
   - Your First Python Program
   - Python Basics
   - Exercise: Basic Calculator
   - Project: Temperature Converter

2. Control Structures
   - Conditional Statements
   - Loops
   - Example: Guessing Game
   - Exercise: Multiplication Table
   - Project: Simple ATM

3. Functions
   - Defining Functions
   - Parameters and Return Values
   - Example: Factorial Function
   - Exercise: Fibonacci Sequence
   - Project: Simple To-Do List

4. Data Structures
   - Lists
   - Tuples
   - Dictionaries
   - Sets
   - Example: Student Grades
   - Exercise: Phonebook
   - Project: Shopping Cart

5. File Handling
   - Reading Files
   - Writing Files
   - Example: Read and Write
   - Exercise: Log System
   - Project: Simple Address Book

6. Object-Oriented Programming (OOP)
   - Introduction to OOP
   - Classes and Objects
   - Inheritance
   - Polymorphism
   - Encapsulation
   - Example: Bank Account
   - Exercise: Library System
   - Project: Student Management System

7. Modules and Packages
   - Introduction to Modules
   - Importing Modules
   - Packages
   - Example: Math Utilities Module
   - Exercise: String Utilities Module
   - Project: Personal Library

8. Exceptions and Error Handling
   - Introduction to Exceptions
   - Handling Exceptions
   - Raising Exceptions
   - Example: Calculator with Error Handling
   - Exercise: File Reader
   - Project: Bank Account with Error Handling

9. Working with APIs
   - Introduction to APIs
   - Using the Requests Library
   - Example: Weather API
   - Exercise: Currency Converter
   - Project: News Aggregator

10. Working with Databases
    - Introduction to Databases
    - SQLite
    - Example: Simple To-Do List with SQLite
    - Exercise: Simple Contacts Database
    - Project: Employee Management System

11. Working with Dates and Times
    - Introduction to the `datetime` Module
    - Getting the Current Date and Time
    - Formatting Dates and Times
    - Parsing Dates from Strings
    - Example: Date Difference Calculator
    - Exercise: Countdown Timer
    - Project: Event Scheduler

12. Web Scraping
    - Introduction to Web Scraping
    - Using BeautifulSoup
    - Example: News Headlines Scraper
    - Exercise: Wikipedia Scraper
    - Project: Price Tracker

13. Advanced Topics
    - Decorators
    - Generators
    - Context Managers
    - Example: Custom Context Manager
    - Exercise: Logging Decorator
    - Project: URL Shortener

14. Concurrency and Parallelism
    - Introduction to Concurrency and Parallelism
    - Using `threading` for Concurrency
    - Using `multiprocessing` for Parallelism
    - Example: Parallel Processing
    - Exercise: Concurrent File Downloader
    - Project: Web Crawler

15. GUI Programming with Tkinter
    - Introduction to Tkinter
    - Creating a Basic Window
    - Adding Widgets
    - Example: Simple Counter
    - Exercise: Basic Calculator
    - Project: To-Do List App

---

## Chapter 1: Introduction to Python

### 1.1 What is Python?

Python is a high-level, interpreted programming language known for its readability and simplicity. It is widely used in web development, data science, artificial intelligence, and more.

### 1.2 Installing Python

1. Download and install Python from the official [Python website](https://www.python.org/).
2. Verify the installation by running `python --version` in your command line or terminal.

### 1.3 Your First Python Program

```python
print("Hello, World!")
```

### 1.4 Python Basics

#### Variables and Data Types

```python
# Integer
a = 10
# Float
b = 20.5
# String
c = "Hello"
# Boolean
d = True
```

#### Basic Operations

```python
# Addition
print(a + b)
# Subtraction
print(a - b)
# Multiplication
print(a * b)
# Division
print(a / b)
```

#### Example: Simple Calculator

```python
def calculator(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        return x / y
    else:
        return "Invalid operation"

# Test the calculator
print(calculator(10, 5, 'add'))
print(calculator(10, 5, 'subtract'))
print(calculator(10, 5, 'multiply'))
print(calculator(10, 5, 'divide'))
```

### 1.5 Exercise: Basic Calculator

1. Write a program that asks the user for two numbers and an operation (add, subtract, multiply, divide).
2. Perform the operation and print the result.

### 1.6 Project: Temperature Converter

Create a program that converts temperatures between Celsius and Fahrenheit.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")

fahrenheit = 77
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is {celsius}°C")
```

---

## Chapter 2: Control Structures

### 2.1 Conditional Statements

#### If, Else, Elif

```python
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
```

### 2.2 Loops

#### For Loop

```python
for i in range(5):
    print(i)
```

#### While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 2.3 Example: Guessing Game

```python
import random

number_to_guess = random.randint(1, 10)
attempts = 0
guessed = False

while not guessed:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    if guess == number_to_guess:
        guessed = True
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
```

### 2.4 Exercise: Multiplication Table

Write a program that prints the multiplication table for a given number.

### 2.5 Project: Simple ATM

Create a program that simulates an ATM machine. The program should:

1. Allow the user to check their balance.
2. Deposit money.
3. Withdraw money.
4. Exit.

```python
balance = 1000

def atm():
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print(f"Your balance is: ${balance}")
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"${amount} deposited. New balance is: ${balance}")
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"${amount} withdrawn. New balance is: ${balance}")
            else:
                print("Insufficient funds!")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the ATM program
atm()
```

---

## Chapter 3: Functions

### 3.1 Defining Functions

```python
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
```

### 3.2 Parameters and Return Values

```python
def add(x, y):
    return x + y

result = add(5, 3)
print(result)
```

### 3.3 Example: Factorial Function

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))
```

### 3.4 Exercise: Fibonacci Sequence

Write a function that returns the Fibonacci sequence up to a given number of terms.

### 3.5 Project: Simple To-Do List

Create a program that allows the user to manage a to-do list. The program should:

1. Add a task.
2. Remove a task.
3. View all tasks.
4. Exit

.

```python
todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
    else:
        print("Task not found!")

def view_tasks():
    if todo_list:
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks in the list.")

def todo():
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            task = input("Enter task: ")
            add_task(task)
        elif choice == 2:
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the To-Do List program
todo()
```

---

## Chapter 4: Data Structures

### 4.1 Lists

#### Creating and Accessing Lists

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
```

#### Modifying Lists

```python
fruits.append("orange")
fruits.remove("banana")
print(fruits)
```

### 4.2 Tuples

```python
coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])
```

### 4.3 Dictionaries

```python
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Math", "Science"]
}

print(student["name"])
print(student["age"])
print(student["courses"])
```

### 4.4 Sets

```python
numbers = {1, 2, 3, 4, 5}
print(numbers)

numbers.add(6)
numbers.remove(2)
print(numbers)
```

### 4.5 Example: Student Grades

```python
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

for student, grade in grades.items():
    print(f"{student}: {grade}")
```

### 4.6 Exercise: Phonebook

Write a program that allows the user to manage a phonebook using a dictionary.

### 4.7 Project: Shopping Cart

Create a program that simulates a shopping cart. The program should:

1. Add an item to the cart.
2. Remove an item from the cart.
3. View the items in the cart.
4. Exit.

```python
cart = []

def add_item(item):
    cart.append(item)

def remove_item(item):
    if item in cart:
        cart.remove(item)
    else:
        print("Item not found!")

def view_cart():
    if cart:
        for item in cart:
            print(f"- {item}")
    else:
        print("The cart is empty.")

def shopping_cart():
    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            item = input("Enter item: ")
            add_item(item)
        elif choice == 2:
            item = input("Enter item to remove: ")
            remove_item(item)
        elif choice == 3:
            view_cart()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the Shopping Cart program
shopping_cart()
```

---

## Chapter 5: File Handling

### 5.1 Reading Files

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### 5.2 Writing Files

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

### 5.3 Example: Read and Write

```python
# Write to file
with open("data.txt", "w") as file:
    file.write("This is some data.")

# Read from file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### 5.4 Exercise: Log System

Write a program that logs user activities to a file.

### 5.5 Project: Simple Address Book

Create a program that manages an address book. The program should:

1. Add a contact.
2. Remove a contact.
3. View all contacts.
4. Save contacts to a file.
5. Load contacts from a file.
6. Exit.

```python
import json

address_book = {}

def add_contact(name, address):
    address_book[name] = address

def remove_contact(name):
    if name in address_book:
        del address_book[name]
    else:
        print("Contact not found!")

def view_contacts():
    if address_book:
        for name, address in address_book.items():
            print(f"{name}: {address}")
    else:
        print("No contacts in the address book.")

def save_contacts(filename):
    with open(filename, "w") as file:
        json.dump(address_book, file)
    print("Contacts saved!")

def load_contacts(filename):
    global address_book
    with open(filename, "r") as file:
        address_book = json.load(file)
    print("Contacts loaded!")

def address_book_program():
    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Save Contacts")
        print("5. Load Contacts")
        print("6. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            address = input("Enter address: ")
            add_contact(name, address)
        elif choice == 2:
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif choice == 3:
            view_contacts()
        elif choice == 4:
            filename = input("Enter filename: ")
            save_contacts(filename)
        elif choice == 5:
            filename = input("Enter filename: ")
            load_contacts(filename)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the Address Book program
address_book_program()
```

---

## Chapter 6: Object-Oriented Programming (OOP)

### 6.1 Introduction to OOP

Object-oriented programming is a programming paradigm based on the concept of objects, which can contain data and code to manipulate that data.

### 6.2 Classes and Objects

#### Defining a Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Create an object
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
```

### 6.3 Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())
```

### 6.4 Polymorphism

```python
class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says tweet!"

animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

for animal in animals:
    print(animal.speak())
```

### 6.5 Encapsulation

```python
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_info(self):
        return f"{self.__year} {self.__make} {self.__model}"

    def set_year(self, year):
        self.__year = year

# Create an object
my_car = Car("Toyota", "Corolla", 2010)
print(my_car.get_info())
my_car.set_year(2020)
print(my_car.get_info())
```

### 6.6 Example: Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds!"
        else:
            self.__balance -= amount
            return self.__balance

    def get_balance(self):
        return self.__balance

# Create an account
account = BankAccount("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
```

### 6.7 Exercise: Library System

Create a class `Book` with attributes title, author, and year. Create another class `

Library` that manages a collection of books with methods to add, remove, and list all books.

### 6.8 Project: Student Management System

Create a program that manages student records. The program should:

1. Add a student.
2. Remove a student.
3. View all students.
4. Exit.

Each student should have a name, ID, and a list of grades.

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def view_students(self):
        if self.students:
            for student in self.students:
                print(f"Name: {student.name}, ID: {student.student_id}, Average Grade: {student.get_average_grade():.2f}")
        else:
            print("No students in the system.")

def main():
    system = StudentManagementSystem()

    while True:
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. View Students")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            system.add_student(student)
        elif choice == 2:
            student_id = input("Enter student ID to remove: ")
            system.remove_student(student_id)
        elif choice == 3:
            system.view_students()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the Student Management System program
main()
```

---

## Chapter 7: Modules and Packages

### 7.1 Introduction to Modules

Modules are Python files that contain functions, classes, and variables. They allow you to organize your code into separate files for better readability and reusability.

### 7.2 Importing Modules

#### Standard Library Modules

```python
import math

print(math.sqrt(16))
print(math.pi)
```

#### Custom Modules

Create a file named `mymodule.py` with the following content:

```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

Import and use the custom module:

```python
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.add(5, 3))
```

### 7.3 Packages

Packages are directories containing multiple modules. They allow for a hierarchical structuring of the module namespace.

Create a package structure:

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

`module1.py`:

```python
def function1():
    return "Function 1 from module 1"
```

`module2.py`:

```python
def function2():
    return "Function 2 from module 2"
```

Import and use the package:

```python
from mypackage import module1, module2

print(module1.function1())
print(module2.function2())
```

### 7.4 Example: Math Utilities Module

Create a module named `math_utils.py` with functions for addition, subtraction, multiplication, and division.

```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is undefined"
```

Import and use the module:

```python
import math_utils

print(math_utils.add(10, 5))
print(math_utils.subtract(10, 5))
print(math_utils.multiply(10, 5))
print(math_utils.divide(10, 5))
```

### 7.5 Exercise: String Utilities Module

Create a module named `string_utils.py` with functions to reverse a string, count the number of vowels, and check if a string is a palindrome.

### 7.6 Project: Personal Library

Create a program that manages a personal library. The program should:

1. Add a book.
2. Remove a book.
3. View all books.
4. Search for a book by title.
5. Save the library to a file.
6. Load the library from a file.
7. Exit.

Each book should have a title, author, and year.

```python
import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def view_books(self):
        if self.books:
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print("No books in the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
                return
        print("Book not found.")

    def save_library(self, filename):
        with open(filename, "w") as file:
            json.dump([book.__dict__ for book in self.books], file)
        print("Library saved!")

    def load_library(self, filename):
        with open(filename, "r") as file:
            self.books = [Book(**book) for book in json.load(file)]
        print("Library loaded!")

def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Search Book")
        print("5. Save Library")
        print("6. Load Library")
        print("7. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book year: "))
            book = Book(title, author, year)
            library.add_book(book)
        elif choice == 2:
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == 3:
            library.view_books()
        elif choice == 4:
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == 5:
            filename = input("Enter filename: ")
            library.save_library(filename)
        elif choice == 6:
            filename = input("Enter filename: ")
            library.load_library(filename)
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the Personal Library program
main()
```

---

## Chapter 8: Exceptions and Error Handling

### 8.1 Introduction to Exceptions

Exceptions are errors detected during execution. They disrupt the normal flow of a program.

### 8.2 Handling Exceptions

#### Try and Except

```python
try:
    x = int(input("Enter a number: "))
    print(f"The number is {x}")
except ValueError:
    print("Invalid input! Please enter a number.")
```

#### Multiple Except Blocks

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print(f"The result is {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
```

#### Finally

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    if file:
        file.close()
```

### 8.3 Raising Exceptions

```python
def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed!")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
```

### 8.4 Example: Calculator with Error Handling

```python
def calculator(x, y, operation):
    try:
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        elif operation == 'multiply':
            return x * y
        elif operation == 'divide':
            if y == 0:
                raise ValueError("Division by zero is not allowed!")
            return x / y
        else:
            return "Invalid operation"
    except ValueError as e:
        return str(e)

# Test the calculator
print(calculator(10, 5, 'add'))
print(calculator(10,

 5, 'subtract'))
print(calculator(10, 5, 'multiply'))
print(calculator(10, 0, 'divide'))
```

### 8.5 Exercise: File Reader

Write a program that reads a file and handles the following exceptions:

1. FileNotFoundError
2. IOError

### 8.6 Project: Bank Account with Error Handling

Extend the Bank Account project from Chapter 6 to handle exceptions for invalid operations such as withdrawing more money than available or entering invalid inputs.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            return self.__balance

    def get_balance(self):
        return self.__balance

def main():
    account = BankAccount("Alice", 1000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        try:
            if choice == 1:
                amount = float(input("Enter amount to deposit: "))
                print(f"New balance: ${account.deposit(amount)}")
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                print(f"New balance: ${account.withdraw(amount)}")
            elif choice == 3:
                print(f"Current balance: ${account.get_balance()}")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError as e:
            print(e)

# Start the Bank Account program with error handling
main()
```

---

## Chapter 9: Working with APIs

### 9.1 Introduction to APIs

APIs (Application Programming Interfaces) allow different software applications to communicate with each other. Python provides several libraries to interact with APIs.

### 9.2 Using the Requests Library

#### Installing Requests

```sh
pip install requests
```

#### Making a GET Request

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
```

#### Making a POST Request

```python
import requests

data = {
    "name": "test-repo",
    "description": "This is a test repository",
    "private": False
}

response = requests.post(
    "https://api.github.com/user/repos",
    json=data,
    headers={"Authorization": "token YOUR_GITHUB_TOKEN"}
)
print(response.status_code)
print(response.json())
```

### 9.3 Example: Weather API

```python
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city} is {data['weather'][0]['description']} with a temperature of {data['main']['temp']}°C"
    else:
        return "City not found!"

# Test the function
print(get_weather("Sydney"))
```

### 9.4 Exercise: Currency Converter

Write a program that converts currency using an API. The program should:

1. Ask the user for the amount and currency to convert from and to.
2. Fetch the conversion rate from an API.
3. Display the converted amount.

### 9.5 Project: News Aggregator

Create a program that fetches and displays the latest news headlines from an API. The program should:

1. Fetch news from a news API.
2. Display the headlines.
3. Allow the user to search for news by keyword.

```python
import requests

def fetch_news(api_key, keyword=None):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": api_key
    }
    if keyword:
        params["q"] = keyword
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()["articles"]
    else:
        return []

def display_news(articles):
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print()

def main():
    api_key = "YOUR_NEWS_API_KEY"

    while True:
        print("\n1. Fetch Latest News")
        print("2. Search News by Keyword")
        print("3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            articles = fetch_news(api_key)
            display_news(articles)
        elif choice == 2:
            keyword = input("Enter keyword: ")
            articles = fetch_news(api_key, keyword)
            display_news(articles)
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the News Aggregator program
main()
```

---

## Chapter 10: Working with Databases

### 10.1 Introduction to Databases

Databases are used to store and manage data. Python provides several libraries to interact with databases, such as SQLite, MySQL, and PostgreSQL.

### 10.2 SQLite

#### Installing SQLite

SQLite is included with Python, so no installation is required.

#### Creating a Database

```python
import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
connection.commit()
connection.close()
```

#### Inserting Data

```python
import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
connection.commit()
connection.close()
```

#### Querying Data

```python
import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
```

### 10.3 Example: Simple To-Do List with SQLite

```python
import sqlite3

def create_table():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")
    connection.commit()
    connection.close()

def add_task(task):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    connection.commit()
    connection.close()

def remove_task(task_id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    connection.commit()
    connection.close()

def view_tasks():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    connection.close()
    return rows

def main():
    create_table()

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            task = input("Enter task: ")
            add_task(task)
        elif choice == 2:
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == 3:
            tasks = view_tasks()
            for task in tasks:
                print(f"{task[0]}: {task[1]}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the To-Do List program with SQLite
main()
```

### 10.4 Exercise: Simple Contacts Database

Create a program that manages contacts using SQLite. The program should:

1. Add a contact (name, phone, email).
2. Remove a contact.
3. View all contacts.
4. Exit.

### 10.5 Project: Employee Management System

Create a program that manages employee records using SQLite. The program should:

1. Add an employee (name, position, salary).
2. Remove an employee.
3. View all employees.
4. Search for an employee by name.
5. Exit.

```python
import sqlite3

def create_table():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)")
    connection.commit()
    connection.close()

def add_employee(name, position, salary):
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    connection.commit()
    connection.close()

def remove_employee(employee_id

):
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    connection.commit()
    connection.close()

def view_employees():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search_employee(name):
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    connection.close()
    return rows

def main():
    create_table()

    while True:
        print("\n1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. Search Employee")
        print("5. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            add_employee(name, position, salary)
        elif choice == 2:
            employee_id = int(input("Enter employee ID to remove: "))
            remove_employee(employee_id)
        elif choice == 3:
            employees = view_employees()
            for employee in employees:
                print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}")
        elif choice == 4:
            name = input("Enter employee name to search: ")
            employees = search_employee(name)
            for employee in employees:
                print(f"ID: {employee[0]}, Name: {employee[1]}, Position: {employee[2]}, Salary: {employee[3]}")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Start the Employee Management System program
main()
```

---

## Chapter 11: Working with Dates and Times

### 11.1 Introduction to the `datetime` Module

The `datetime` module supplies classes for manipulating dates and times.

### 11.2 Getting the Current Date and Time

```python
import datetime

now = datetime.datetime.now()
print(now)
```

### 11.3 Formatting Dates and Times

```python
import datetime

now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
```

### 11.4 Parsing Dates from Strings

```python
import datetime

date_string = "2024-07-20 15:30:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)
```

### 11.5 Example: Date Difference Calculator

```python
import datetime

date1 = datetime.datetime(2024, 7, 20)
date2 = datetime.datetime(2023, 7, 20)

difference = date1 - date2
print(f"The difference is {difference.days} days.")
```

### 11.6 Exercise: Countdown Timer

Write a program that takes a future date as input and displays the number of days, hours, minutes, and seconds until that date.

### 11.7 Project: Event Scheduler

Create a program that allows users to schedule events with dates and times. The program should:

1. Add an event.
2. Remove an event.
3. View all events.
4. Display upcoming events.

---

## Chapter 12: Web Scraping

### 12.1 Introduction to Web Scraping

Web scraping is the process of extracting data from websites.

### 12.2 Using BeautifulSoup

#### Installing BeautifulSoup and Requests

```sh
pip install beautifulsoup4 requests
```

#### Fetching a Web Page

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
```

### 12.3 Extracting Data

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
```

### 12.4 Example: News Headlines Scraper

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for item in soup.find_all('a', class_='storylink'):
    print(item.text)
```

### 12.5 Exercise: Wikipedia Scraper

Write a program that scrapes the titles of the "In the news" section from the Wikipedia homepage.

### 12.6 Project: Price Tracker

Create a program that tracks the price of a product on an e-commerce website and sends an email notification when the price drops below a certain threshold.

---

## Chapter 13: Advanced Topics

### 13.1 Decorators

Decorators are a way to modify the behavior of a function or class method.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### 13.2 Generators

Generators are functions that return an iterable set of items, one at a time, in a special way.

```python
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
```

### 13.3 Context Managers

Context managers allow you to allocate and release resources precisely when you want to.

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

### 13.4 Example: Custom Context Manager

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with MyContextManager():
    print("Inside the context")
```

### 13.5 Exercise: Logging Decorator

Write a decorator that logs the arguments and return value of a function.

### 13.6 Project: URL Shortener

Create a URL shortener service using Flask and SQLite. The program should:

1. Shorten a given URL.
2. Redirect shortened URLs to the original URLs.
3. Display statistics for shortened URLs.

---

## Chapter 14: Concurrency and Parallelism

### 14.1 Introduction to Concurrency and Parallelism

Concurrency and parallelism allow you to run multiple tasks simultaneously to improve performance.

### 14.2 Using `threading` for Concurrency

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

### 14.3 Using `multiprocessing` for Parallelism

```python
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()
```

### 14.4 Example: Parallel Processing

```python
import multiprocessing

def square_number(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
with multiprocessing.Pool() as pool:
    results = pool.map(square_number, numbers)

print(results)
```

### 14.5 Exercise: Concurrent File Downloader

Write a program that downloads multiple files concurrently using `threading`.

### 14.6 Project: Web Crawler

Create a web crawler that visits a website and its links concurrently. The program should:

1. Crawl a website starting from a given URL.
2. Extract and print all the URLs found.
3. Save the URLs to a file.

---

## Chapter 15: GUI Programming with Tkinter

### 15.1 Introduction to Tkinter

Tkinter is the standard GUI library for Python.

### 15.2 Creating a Basic Window

```python
import tkinter as tk

window = tk.Tk()
window.title("My App")
window.mainloop()
```

### 15.3 Adding Widgets

```python
import tkinter as tk

window = tk.Tk()
window.title("My App")

label = tk.Label(window, text="Hello, World!")
label.pack()

button = tk.Button(window, text="Click Me", command=lambda: print("Button Clicked"))
button.pack()

window.mainloop()
```

### 15.4 Example: Simple Counter

```python
import tkinter as tk

counter = 0

def increment():
    global counter
    counter += 1
    label.config(text=str(counter))

window = tk.Tk()
window.title("Counter")

label = tk.Label(window, text=str(counter))
label.pack()

button = tk.Button(window, text="Increment", command=increment)
button.pack()

window.mainloop()
```

### 15.5 Exercise: Basic Calculator

Write a program that creates a basic calculator GUI with Tkinter.

### 15.6 Project: To-Do List App

Create a to-do list application using Tkinter. The program should:

1. Add tasks.
2. Remove tasks.
3. Mark tasks as completed.
4. Save tasks to a

 file.
5. Load tasks from a file.
