# Data Structures and Algorithms in Python

## Table of Contents

1. Introduction to Data Structures
   - Arrays
   - Linked Lists
   - Stacks
   - Queues
   - Hash Tables
   - Trees
   - Graphs
2. Algorithms Basics
   - Sorting Algorithms
   - Searching Algorithms
3. Advanced Algorithms
   - Dynamic Programming
   - Graph Algorithms
   - Greedy Algorithms
4. Capstone Project

---

## Chapter 1: Introduction to Data Structures

### Arrays

**Q1.1: Write a Python function that finds the maximum element in an array.**

**Answer:**

```python
def find_max(arr):
    if not arr:
        return None  # Handle empty array
    max_element = arr[0]  # Initialize max_element with the first element
    for num in arr:
        if num > max_element:
            max_element = num  # Update max_element if current number is greater
    return max_element

# Test the function
print(find_max([1, 2, 3, 4, 5]))  # Output: 5
print(find_max([-1, -2, -3, -4, -5]))  # Output: -1
```

**Explanation:**

- **Initial Check:** Handles the case where the array is empty.
- **Initialization:** Initializes `max_element` with the first element of the array.
- **For Loop:** Iterates through the array to find the maximum element.
- **Condition Check:** Updates `max_element` if the current element is greater.

### Linked Lists

**Q1.2: Implement a singly linked list in Python with methods to add, remove, and display elements.**

**Answer:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initialize next as None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def add(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, set head to the new node
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Set the next of the last node to the new node

    def remove(self, data):
        if not self.head:  # If the list is empty, return
            return
        if self.head.data == data:  # If the head node is to be removed, update head
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:  # Traverse to find the node to be removed
            current = current.next
        if current.next:  # If the node is found, update the next pointer
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:  # Traverse and print all elements
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Test the linked list
ll = SinglyLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
ll.remove(2)
ll.display()  # Output: 1 -> 3 -> None
```

**Explanation:**

- **Node Class:** Represents a node in the linked list with `data` and `next` attributes.
- **SinglyLinkedList Class:** Manages the linked list with methods to add, remove, and display elements.
- **Add Method:** Adds a new node to the end of the list.
- **Remove Method:** Removes the first occurrence of a node with the specified data.
- **Display Method:** Prints the elements of the list.

### Stacks

**Q1.3: Implement a stack in Python using a list with methods to push, pop, and peek elements.**

**Answer:**

```python
class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack elements

    def push(self, item):
        self.items.append(item)  # Append the item to the list

    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items.pop()  # Remove and return the top item
        return None

    def peek(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items[-1]  # Return the top item without removing it
        return None

    def is_empty(self):
        return len(self.items) == 0  # Return True if the stack is empty

    def display(self):
        print(self.items)  # Print the list representing the stack

# Test the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  # Output: [1, 2, 3]
print(stack.pop())  # Output: 3
stack.display()  # Output: [1, 2]
print(stack.peek())  # Output: 2
```

**Explanation:**

- **Stack Class:** Manages a stack with methods to push, pop, peek, and check if the stack is empty.
- **Push Method:** Adds an element to the top of the stack.
- **Pop Method:** Removes and returns the top element of the stack.
- **Peek Method:** Returns the top element without removing it.
- **Is_Empty Method:** Checks if the stack is empty.

### Queues

**Q1.4: Implement a queue in Python using a list with methods to enqueue, dequeue, and peek elements.**

**Answer:**

```python
class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to store queue elements

    def enqueue(self, item):
        self.items.append(item)  # Append the item to the list

    def dequeue(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.items.pop(0)  # Remove and return the front item
        return None

    def peek(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.items[0]  # Return the front item without removing it
        return None

    def is_empty(self):
        return len(self.items) == 0  # Return True if the queue is empty

    def display(self):
        print(self.items)  # Print the list representing the queue

# Test the queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Output: [1, 2, 3]
print(queue.dequeue())  # Output: 1
queue.display()  # Output: [2, 3]
print(queue.peek())  # Output: 2
```

**Explanation:**

- **Queue Class:** Manages a queue with methods to enqueue, dequeue, peek, and check if the queue is empty.
- **Enqueue Method:** Adds an element to the end of the queue.
- **Dequeue Method:** Removes and returns the front element of the queue.
- **Peek Method:** Returns the front element without removing it.
- **Is_Empty Method:** Checks if the queue is empty.

### Hash Tables

**Q1.5: Implement a hash table in Python with methods to insert, delete, and search for elements.**

**Answer:**

```python
class HashTable:
    def __init__(self, size):
        self.size = size  # Set the size of the hash table
        self.table = [[] for _ in range(size)]  # Initialize the table with empty lists

    def hash_function(self, key):
        return hash(key) % self.size  # Compute the index using a hash function

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:  # Check if the key already exists
            if pair[0] == key:
                pair[1] = value  # Update the value if key exists
                return
        self.table[index].append([key, value])  # Insert the new key-value pair

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)  # Remove the key-value pair
                return

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value if key is found
        return None

    def display(self):
        for i, pairs in enumerate(self.table):
            if pairs:
                print(f"Index {i}: {pairs}")  # Print the non-empty buckets

# Test the hash table
ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 30)
ht.display()
print(ht.search("name"))  # Output: Alice
ht.delete("name")
ht.display()
```

**Explanation:**

- **HashTable Class:** Manages a hash table with methods to insert, delete, and search for elements.
- **Hash

 Function:** Calculates the index for a key using Python's built-in `hash` function and modulo operation.
- **Insert Method:** Adds a key-value pair to the hash table.
- **Delete Method:** Removes a key-value pair from the hash table.
- **Search Method:** Searches for a key in the hash table and returns its value.

### Trees

**Q1.6: Implement a binary search tree (BST) in Python with methods to insert, search, and traverse elements in-order.**

**Answer:**

```python
class TreeNode:
    def __init__(self, key):
        self.left = None  # Initialize left child as None
        self.right = None  # Initialize right child as None
        self.val = key  # Set the value of the node

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize root as None

    def insert(self, key):
        if self.root is None:  # If the tree is empty, set root to the new node
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)  # Insert the new node as the left child
            else:
                self._insert(node.left, key)  # Recur to the left subtree
        else:
            if node.right is None:
                node.right = TreeNode(key)  # Insert the new node as the right child
            else:
                self._insert(node.right, key)  # Recur to the right subtree

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node  # Return the node if found
        if key < node.val:
            return self._search(node.left, key)  # Recur to the left subtree
        return self._search(node.right, key)  # Recur to the right subtree

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)  # Traverse the left subtree
            print(node.val, end=' ')  # Visit the node
            self.inorder_traversal(node.right)  # Traverse the right subtree

# Test the binary search tree
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.inorder_traversal(bst.root)  # Output: 2 5 10 15 20
print(bst.search(15))  # Output: <__main__.TreeNode object at ...>
print(bst.search(25))  # Output: None
```

**Explanation:**

- **TreeNode Class:** Represents a node in the binary search tree with `left`, `right`, and `val` attributes.
- **BinarySearchTree Class:** Manages the BST with methods to insert, search, and traverse elements.
- **Insert Method:** Adds a new node to the BST.
- **Search Method:** Searches for a key in the BST.
- **Inorder Traversal Method:** Traverses the BST in-order (left, root, right).

### Graphs

**Q1.7: Implement an undirected graph in Python using an adjacency list with methods to add vertices, add edges, and display the graph.**

**Answer:**

```python
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to store the graph

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []  # Add the vertex with an empty adjacency list

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)  # Add an edge from vertex1 to vertex2
            self.graph[vertex2].append(vertex1)  # Add an edge from vertex2 to vertex1

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")  # Print the adjacency list for each vertex

# Test the graph
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.display()  # Output: 1: [2], 2: [1, 3], 3: [2]
```

**Explanation:**

- **Graph Class:** Manages an undirected graph using an adjacency list.
- **Add Vertex Method:** Adds a new vertex to the graph.
- **Add Edge Method:** Adds an edge between two vertices.
- **Display Method:** Displays the graph as an adjacency list.

---

## Chapter 2: Algorithms Basics

### Sorting Algorithms

**Q2.1: Implement the bubble sort algorithm in Python.**

**Answer:**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if the element is greater than the next
    return arr

# Test the bubble sort
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**Explanation:**

- **Bubble Sort:** Repeatedly swaps adjacent elements if they are in the wrong order.
- **Time Complexity:** O(n^2) in the worst case.

### Searching Algorithms

**Q2.2: Implement the binary search algorithm in Python.**

**Answer:**

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            left = mid + 1  # Adjust the search range to the right half
        else:
            right = mid - 1  # Adjust the search range to the left half
    return -1  # Return -1 if the target is not found

# Test the binary search
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # Output: 4
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))  # Output: -1
```

**Explanation:**

- **Binary Search:** Searches for a target value in a sorted array by repeatedly dividing the search interval in half.
- **Time Complexity:** O(log n) in the worst case.

### Additional Sorting Algorithm: Quick Sort

**Q2.3: Implement the quick sort algorithm in Python.**

**Answer:**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Return the array if it has one or zero elements
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recur for left and right parts

# Test the quick sort
print(quick_sort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**Explanation:**

- **Quick Sort:** Uses divide-and-conquer to sort elements by selecting a pivot and partitioning the array into elements less than, equal to, and greater than the pivot.
- **Time Complexity:** O(n log n) on average.

---

## Chapter 3: Advanced Algorithms

### Dynamic Programming

**Q3.1: Implement the Fibonacci sequence using dynamic programming.**

**Answer:**

```python
def fibonacci_dp(n):
    fib = [0, 1]  # Initialize the base cases
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  # Append the sum of the last two Fibonacci numbers
    return fib[n]

# Test the dynamic programming Fibonacci
print(fibonacci_dp(10))  # Output: 55
```

**Explanation:**

- **Dynamic Programming:** Solves problems by breaking them down into simpler subproblems and storing the results to avoid redundant computations.
- **Fibonacci Sequence:** Uses a list to store Fibonacci numbers up to `n`.

### Graph Algorithms

**Q3.2: Implement Dijkstra's algorithm to find the shortest path in a graph.**

**Answer:**

```python
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]  #

 Initialize the heap with the start vertex
    distances = {vertex: float('inf') for vertex in graph}  # Initialize distances to infinity
    distances[start] = 0  # Distance to the start vertex is 0

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)  # Get the vertex with the smallest distance

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # Calculate the distance to the neighbor

            if distance < distances[neighbor]:  # If a shorter path is found
                distances[neighbor] = distance  # Update the distance
                heapq.heappush(heap, (distance, neighbor))  # Push the neighbor to the heap

    return distances

# Test Dijkstra's algorithm
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

**Explanation:**

- **Dijkstra's Algorithm:** Finds the shortest path from a starting vertex to all other vertices in a graph with non-negative weights.
- **Heap Queue:** Uses a priority queue to efficiently select the vertex with the smallest distance.
- **Distance Calculation:** Updates the shortest known distance to each vertex.

### Greedy Algorithms

**Q3.3: Implement the greedy algorithm for the fractional knapsack problem.**

**Answer:**

```python
def fractional_knapsack(weights, values, capacity):
    index = list(range(len(values)))
    ratio = [v / w for v, w in zip(values, weights)]  # Calculate value-to-weight ratios
    index.sort(key=lambda i: ratio[i], reverse=True)  # Sort items by ratio in descending order

    max_value = 0
    for i in index:
        if weights[i] <= capacity:
            max_value += values[i]  # Add the full value of the item
            capacity -= weights[i]  # Decrease the capacity
        else:
            max_value += values[i] * (capacity / weights[i])  # Add a fraction of the value
            break  # The knapsack is full

    return max_value

# Test the fractional knapsack
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(fractional_knapsack(weights, values, capacity))  # Output: 240.0
```

**Explanation:**

- **Greedy Algorithm:** Selects items based on the highest value-to-weight ratio.
- **Fractional Knapsack:** Allows taking fractions of items to maximize the total value within the given capacity.
- **Sorting:** Sorts items by their value-to-weight ratio in descending order.

---

## Chapter 4: Capstone Project

### Capstone Project: Implementing a Simple Search Engine

**Project Description:**

Implement a simple search engine that indexes a collection of documents and allows users to search for keywords. The search engine should rank documents based on the frequency of the search keywords.

**Steps:**

1. **Data Collection:** Load a collection of documents.
2. **Indexing:** Create an inverted index for the documents.
3. **Search:** Implement a search function that ranks documents based on keyword frequency.

### Step 1: Data Collection

**Q4.1: Write a Python function to load documents from a text file. Each line in the file represents a document.**

**Answer:**

```python
def load_documents(filename):
    with open(filename, 'r') as file:
        documents = file.readlines()  # Read all lines from the file
    return [doc.strip() for doc in documents]  # Remove leading/trailing whitespace

# Test the function (assuming 'documents.txt' exists with some content)
documents = load_documents('documents.txt')
print(documents)
```

**Explanation:**

- **File Handling:** Reads the file line by line and stores each line as a document.
- **Stripping Whitespace:** Removes leading and trailing whitespace from each document.

### Step 2: Indexing

**Q4.2: Write a Python function to create an inverted index from a list of documents. The index should map each word to the list of document IDs where it appears.**

**Answer:**

```python
from collections import defaultdict

def create_inverted_index(documents):
    index = defaultdict(list)  # Use defaultdict to handle missing keys automatically
    for doc_id, doc in enumerate(documents):  # Enumerate to get document ID
        for word in doc.split():  # Split the document into words
            index[word].append(doc_id)  # Append the document ID to the word's list
    return index

# Test the function
documents = ["the quick brown fox", "jumps over the lazy dog", "the quick blue fox"]
index = create_inverted_index(documents)
print(index)
```

**Explanation:**

- **Defaultdict:** Uses `defaultdict` to handle missing keys automatically.
- **Document ID:** Enumerates through documents to assign unique IDs.
- **Inverted Index:** Maps each word to the list of document IDs where it appears.

### Step 3: Search

**Q4.3: Write a Python function to search for keywords in the documents using the inverted index. Rank the documents based on the frequency of the keywords.**

**Answer:**

```python
def search_documents(keywords, index, documents):
    keyword_counts = defaultdict(int)  # Use defaultdict to count keyword occurrences
    for keyword in keywords.split():
        if keyword in index:
            for doc_id in index[keyword]:
                keyword_counts[doc_id] += 1  # Increment the count for each document ID

    sorted_docs = sorted(keyword_counts.items(), key=lambda item: item[1], reverse=True)  # Sort by frequency
    return [documents[doc_id] for doc_id, _ in sorted_docs]  # Return the ranked documents

# Test the function
keywords = "quick fox"
results = search_documents(keywords, index, documents)
print(results)
```

**Explanation:**

- **Keyword Counts:** Counts the frequency of each keyword in the documents.
- **Sorting:** Ranks documents based on keyword frequency.
- **Returning Results:** Returns the ranked list of documents.

### Capstone Project Completion

By completing this capstone project, students will gain hands-on experience in implementing a simple search engine. This project integrates data collection, indexing, and searching, making it a comprehensive challenge for understanding data structures and algorithms.
