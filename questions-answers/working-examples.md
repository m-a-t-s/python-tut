Sure, I can add more examples and provide more detailed explanations to further enhance the content.

---

## Basic Conditionals

**Q1.1: Write a Python function that checks if a number is positive, negative, or zero.**

**Answer:**

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test the function
print(check_number(10))  # Output: Positive
print(check_number(-5))  # Output: Negative
print(check_number(0))   # Output: Zero
```

**Explanation:**

- **If-elif-else Statement:** Checks the condition of the number being positive, negative, or zero.
- **Return Statements:** Returns the appropriate string based on the condition.

### Additional Example: Check If a Number is Even or Odd

**Q1.2: Write a Python function that checks if a number is even or odd.**

**Answer:**

```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd
```

**Explanation:**

- **Modulo Operator:** Checks if the number is divisible by 2 without a remainder.
- **Return Statements:** Returns "Even" if the number is divisible by 2, otherwise returns "Odd".

---

## Loops

**Q2.1: Write a Python function that prints the first 10 Fibonacci numbers using a for loop.**

**Answer:**

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Test the function
fibonacci(10)  # Output: 0 1 1 2 3 5 8 13 21 34
```

**Explanation:**

- **For Loop:** Iterates `n` times to print the Fibonacci sequence.
- **Tuple Assignment:** Updates the values of `a` and `b` in each iteration to generate the next number in the sequence.

### Additional Example: Sum of Numbers in a List

**Q2.2: Write a Python function that calculates the sum of all numbers in a list using a for loop.**

**Answer:**

```python
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
```

**Explanation:**

- **For Loop:** Iterates through each number in the list.
- **Accumulation:** Adds each number to the `total` variable.

---

## Functions

**Q3.1: Write a Python function that returns the factorial of a given number. Use recursion to solve the problem.**

**Answer:**

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120
```

**Explanation:**

- **Recursion:** The function calls itself with a reduced value until the base case (n == 0) is reached.
- **Base Case:** When `n` is 0, the function returns 1.

### Additional Example: Calculate Power of a Number

**Q3.2: Write a Python function that calculates the power of a number using recursion.**

**Answer:**

```python
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Test the function
print(power(2, 3))  # Output: 8
```

**Explanation:**

- **Recursion:** The function calls itself with a reduced exponent until the base case (exp == 0) is reached.
- **Base Case:** When `exp` is 0, the function returns 1.

---

## Data Structures

**Q4.1: Write a Python function that removes duplicates from a list and returns a new list.**

**Answer:**

```python
def remove_duplicates(lst):
    return list(set(lst))

# Test the function
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

**Explanation:**

- **Set Data Structure:** Converts the list to a set to remove duplicates.
- **List Conversion:** Converts the set back to a list.

### Additional Example: Count Frequency of Elements in a List

**Q4.2: Write a Python function that counts the frequency of each element in a list and returns a dictionary.**

**Answer:**

```python
def count_frequency(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

# Test the function
print(count_frequency([1, 2, 2, 3, 4, 4, 5]))  # Output: {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}
```

**Explanation:**

- **Dictionary:** Uses a dictionary to store the frequency of each element.
- **For Loop:** Iterates through each element and updates its frequency in the dictionary.

---

## File Handling

**Q5.1: Write a Python function that reads a file and prints its contents.**

**Answer:**

```python
def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)

# Test the function (assuming 'example.txt' exists with some content)
read_file('example.txt')
```

**Explanation:**

- **With Statement:** Ensures the file is properly closed after reading.
- **File Read:** Reads the contents of the file and prints it.

### Additional Example: Write a List to a File

**Q5.2: Write a Python function that writes a list of strings to a file, each on a new line.**

**Answer:**

```python
def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

# Test the function
write_list_to_file(["Line 1", "Line 2", "Line 3"], 'output.txt')
```

**Explanation:**

- **For Loop:** Iterates through each item in the list.
- **File Write:** Writes each item to the file followed by a newline character.

---

## Object-Oriented Programming (OOP)

**Q6.1: Create a class `Person` with attributes `name` and `age`. Include a method `greet` that prints a greeting message using the person's name.**

**Answer:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Test the class
person = Person("Alice", 30)
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

**Explanation:**

- **Class Definition:** Defines a `Person` class with `__init__` and `greet` methods.
- **Instance Attributes:** Initializes `name` and `age` attributes.
- **Method:** The `greet` method prints a greeting message using the `name` attribute.

### Additional Example: Inheritance in OOP

**Q6.2: Create a class `Student` that inherits from the `Person` class and adds a new attribute `student_id`. Override the `greet` method to include the student ID.**

**Answer:**

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")

# Test the class
student = Student("Bob", 20, "S12345")
student.greet()  # Output: Hello, my name is Bob, I am 20 years old, and my student ID is S12345.
```

**Explanation:**

- **Inheritance:** `Student` class inherits from `Person`.
- **Super():** Calls the parent class's `__init__` method to initialize inherited attributes.
- **Method Override:** Overrides the `greet` method to include the `student_id`.

---

## Decorators

**Q7.1: Write a decorator that logs the arguments and return value of a function.**

**Answer:**

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logger


def add(a, b):
    return a + b

# Test the decorator
print(add(5, 3))  # Output: Logs the call and return value, returns 8
```

**Explanation:**

- **Decorator Function:** Defines a decorator that logs function calls and their return values.
- **Wrapper Function:** Logs the arguments and return value before returning the result.

### Additional Example: Timing a Function

**Q7.2: Write a decorator that measures the execution time of a function.**

**Answer:**

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def add(a, b):
    time.sleep(1)  # Simulate a delay
    return a + b

# Test the decorator
print(add(5, 3))  # Output: Logs the execution time, returns 8
```

**Explanation:**

- **Time Module:** Uses the `time` module to measure execution time.
- **Wrapper Function:** Logs the time taken to execute the function.

---

## Generators

**Q8.1: Write a generator function that yields the first `n` prime numbers.**

**Answer:**

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    count, num = 0, 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Test the generator
for prime in prime_generator(10):
    print(prime, end=' ')  # Output: 2 3 5 7 11 13 17 19 23 29
```

**Explanation:**

- **Helper Function:** `is_prime` checks if a number is prime.
- **Generator Function:** `prime_generator` yields the first `n` prime numbers using the `is_prime` function.

### Additional Example: Infinite Sequence Generator

**Q8.2: Write a generator function that yields an infinite sequence of numbers starting from a given number.**

**Answer:**

```python
def infinite_sequence(start=0):
    num = start
    while True:
        yield num
        num += 1

# Test the generator
seq_gen = infinite_sequence(10)
for _ in range(5):
    print(next(seq_gen), end=' ')  # Output: 10 11 12 13 14
```

**Explanation:**

- **Infinite Loop:** The generator runs indefinitely, yielding numbers in sequence.
- **Yield:** The `yield` statement returns a value and pauses the generator.

---

## Context Managers

**Q9.1: Create a context manager that logs entering and exiting a context.**

**Answer:**

```python
class LoggingContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

# Test the context manager
with LoggingContextManager():
    print("Inside the context")
```

**Explanation:**

- **Context Manager Class:** Defines `__enter__` and `__exit__` methods to log entering and exiting the context.
- **With Statement:** Ensures the context manager's methods are called appropriately.

### Additional Example: Timer Context Manager

**Q9.2: Write a context manager that measures the execution time of a code block.**

**Answer:**

```python
import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Execution time: {self.end_time - self.start_time} seconds")

# Test the context manager
with TimerContextManager():
    time.sleep(1)  # Simulate a delay
```

**Explanation:**

- **Time Module:** Uses the `time` module to measure execution time.
- **Enter Method:** Records the start time.
- **Exit Method:** Records the end time and prints the execution duration.

---

## Concurrency and Parallelism

**Q10.1: Write a Python function that fetches data from multiple URLs concurrently using `asyncio`.**

**Answer:**

```python
import asyncio
import aiohttp

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        return await asyncio.gather(*tasks)

# Test the function
urls = ['http://example.com', 'http://example.org']
loop = asyncio.get_event_loop()
results = loop.run_until_complete(fetch_all(urls))
for result in results:
    print(result[:100])  # Print the first 100 characters of each result
```

**Explanation:**

- **Asyncio:** Uses `asyncio` for asynchronous programming.
- **Aiohttp:** Utilizes `aiohttp` for asynchronous HTTP requests.
- **Async Functions:** `fetch` and `fetch_all` are asynchronous functions that fetch data concurrently.

### Additional Example: Parallel Processing with `multiprocessing`

**Q10.2: Write a Python function that squares numbers in a list using multiple processes.**

**Answer:**

```python
import multiprocessing

def square(num):
    return num * num

def square_numbers(numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(square, numbers)
    return result

# Test the function
numbers = [1, 2, 3, 4, 5]
print(square_numbers(numbers))  # Output: [1, 4, 9, 16, 25]
```

**Explanation:**

- **Multiprocessing:** Uses the `multiprocessing` module to parallelize the computation.
- **Pool:** Creates a pool of worker processes to execute the `square` function on each number concurrently.

---

## Capstone Project: E-commerce Recommendation System

**Q11.1: Implement the `get_recommendations` function for the e-commerce recommendation system.**

**Answer:**

```python
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

# Dummy Data
import pandas as pd

data = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'product_id': [101, 102, 101, 103, 104, 105, 101, 106, 107, 108]
})

# Create a pivot table for user-item interactions
user_item_matrix = data.pivot_table(index='user_id', columns='product_id', aggfunc='size', fill_value=0)

# Convert the pivot table to a sparse matrix
user_item_sparse = csr_matrix(user_item_matrix.values)

# Fit the model using Nearest Neighbors
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(user_item_sparse)

# Function to get product recommendations
def get_recommendations(user_id, n_recommendations=5):
    if user_id not in user_item_matrix.index:
        return []

    user_index = user_item_matrix.index.get_loc(user_id)
    distances, indices = model.kneighbors(user_item_sparse[user_index], n_neighbors=n_recommendations + 1)
    recommended_items = []

    for i in range(1, len(distances.flatten())):
        recommended_items.append(user_item_matrix.columns[indices.flatten()[i]])

    return recommended_items

# Test the recommendation function
print(get_recommendations(1, 5))  # Output: List of recommended product IDs
```

**Explanation:**

- **Data Preparation:** Converts user-item interactions into a sparse matrix.
- **Model Training:** Uses Nearest Neighbors to find similar users/products.
- **Recommendation Function:** Retrieves product recommendations based on user similarity.

---

These questions and answers provide a comprehensive journey from basic to advanced Python concepts, each designed to deepen your understanding and skills.