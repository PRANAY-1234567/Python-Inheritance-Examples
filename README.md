# Python Inheritance Examples

## 📌 Overview

This project demonstrates **Inheritance in Python** using two practical examples: a Product Management System and a Hospital Billing System.

Inheritance allows a child class to reuse attributes and methods from a parent class. It helps organize code, reduce duplication, and extend existing functionality.

Both examples demonstrate how a child class can inherit a parent class's constructor, add new attributes, and override a method to display additional information.

## 🎯 Concepts Covered

* Classes and Objects
* Single Inheritance
* Constructors (`__init__`)
* The `super()` Function
* Method Overriding
* Instance Variables
* Code Reusability

## 📂 Examples Included

### 1. Product Management System

This example demonstrates inheritance using product information.

**Class: `Product`**

The parent class stores and displays:

* Product name
* Brand name
* Price

The `Data()` method displays the basic product information.

**Class: `Product_Data`**

The child class inherits from `Product` and adds:

* Total number of products
* Current location

It uses `super().__init__()` to initialize the attributes inherited from the parent class.

The `Data()` method is overridden to display both the original product details and the additional information.

**Example:**

```python
e = Product_Data("Laptop", "ASUS", 60000, 123, "Yavatmal")
e.Data()
```

**Sample Output:**

```text
Product Name Laptop
Brand Name ASUS
Total Amount 60000
Total Product 123
Current location is Yavatmal
```

### 2. Hospital Billing System

This example demonstrates inheritance using hospital and billing information.

**Class: `Hospital`**

The parent class stores and displays:

* Hospital name
* Patient name
* Doctor name

The `Hospital_Data()` method displays the hospital and patient details.

**Class: `Hospital_Bill`**

The child class inherits from `Hospital` and adds:

* ICU bill
* Normal bill
* Total bill

It uses `super().__init__()` to initialize the hospital, patient, and doctor information.

The `Hospital_Data()` method is overridden to display the original hospital details along with the billing information.

**Example:**

```python
h = Hospital_Bill("ABC", "Parag", "Harsh", 123432, 6000, 1200000)
h.Hospital_Data()
```

**Sample Output:**

```text
Hospital Name is ABC
Patient Name is Parag
Doctor Name is Harsh
Total Hospital is 1200000
Total Normal Bill 6000
Total ICU Bill 123432
```

## 🔑 Important Concepts Explained

### 1. Inheritance

Inheritance allows a child class to access functionality from a parent class.

For example:

```python
class Product_Data(Product):
    pass
```

Here, `Product_Data` inherits from `Product`.

### 2. The `super()` Function

The `super()` function allows a child class to call methods defined in its parent class.

For example:

```python
super().__init__(Product_name, Brand, Price)
```

This calls the parent constructor to initialize the product name, brand, and price.

Similarly:

```python
super().Data()
```

This calls the parent class's `Data()` method before displaying additional product information.

### 3. Method Overriding

Method overriding occurs when a child class defines a method with the same name as a method in its parent class.

In this project:

* `Product_Data` overrides `Data()`.
* `Hospital_Bill` overrides `Hospital_Data()`.

Each child class first calls the parent method using `super()` and then displays its additional information.

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Copy the code into a Python file.
3. Save the file as `inheritance_examples.py`.
4. Open a terminal in the directory containing the file.
5. Run the following command:

```bash
python inheritance_examples.py
```

**Note:** Your examples are enclosed in triple quotes, so Python treats them as strings rather than executing them. Remove the outer triple quotes from the example you want to run.

## 📚 Learning Outcomes

After completing this project, you should understand:

* How inheritance works in Python.
* How a child class reuses a parent class's attributes and methods.
* How to initialize parent attributes using `super()`.
* How to extend a parent class with additional attributes.
* How method overriding works.
* How to organize related data using object-oriented programming.

## 👨‍💻 Author

**Pranay Jadhao**

Learning Python, Object-Oriented Programming, and software development.

