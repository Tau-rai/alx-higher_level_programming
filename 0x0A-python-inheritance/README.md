**Python Class and Inheritance**
**Definitions**
Superclass/Baseclass/Parentclass: This is the class from which a subclass inherits features. It is also known as a base class or parent class.

Subclass: This is a class that inherits properties and methods from another class, called the superclass.

**Listing Attributes and Methods**
You can list all attributes and methods of a class or instance using the built-in dir() function.

**Instance Attributes**
An instance can have new attributes when they are added in the instance’s method or directly to the instance.

**Inheritance**
Inheritance is a way of creating a new class using details of an existing class without modifying it. The newly formed class is a derived class (or child class). The existing class is a base class (or parent class).

To inherit a class from another, you define a new class and put the name of the base class in parentheses.

**Default Class**
In Python, every class you create implicitly derives from the default object class.

**Overriding Methods and Attributes**
In Python, a subclass can provide a different implementation of a method that is already defined in its superclass. This is known as Method Overriding.

**Available Attributes and Methods**
In inheritance, the subclasses inherit the attributes and methods of the superclass.

**Purpose of Inheritance**
The main advantages of inheritance are code reusability and readability. When a child class inherits the properties and functionality of the parent class, we reuse the code functionality already defined in the parent class.

**Built-in Functions**
```isinstance()```: This function checks if an object is an instance of a class.
```issubclass()```: This function checks if a class is a subclass of another class.
```type()```: This function returns the type of the object.
```super()```: This function is used to call a method from a parent class