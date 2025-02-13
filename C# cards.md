



Flashcard 1: Basic Syntax Comparison
What is the basic syntax for declaring a variable in C#?

C#:
csharp
Copy
int x = 10;




Flashcard 2: Data Types
How do basic data types work in C#?

C#: Statically typed, types must be explicitly declared.
Example:
csharp
Copy
int x = 10;  
string y = "Hello";  




Flashcard 3: Conditionals
How do you write an if-statement in C#?

C#:
csharp
Copy
if (x > 10) {
    Console.WriteLine("x is greater than 10");
}




Flashcard 4: Loops
What is the syntax for a for loop in C#?

C#:
csharp
Copy
for (int i = 0; i < 5; i++) {
    Console.WriteLine(i);
}




Flashcard 5: Functions/Methods
How do you define a function in C#?

C#:
csharp
Copy
public int Add(int x, int y) {
    return x + y;
}




Flashcard 6: Classes and Object-Oriented Programming
How is a class defined in C#?

C#:
csharp
Copy
public class Dog {
    public string Name { get; set; }
    
    public Dog(string name) {
        Name = name;
    }
}




Flashcard 7: Access Modifiers
What are the key access modifiers in C#?

public: Accessible anywhere.
private: Accessible only within the same class.
protected: Accessible within the same class and derived classes.
internal: Accessible within the same assembly.




Flashcard 8: Exception Handling
How do you handle exceptions in C#?

C#:
csharp
Copy
try {
    int x = 1 / 0;
}
catch (DivideByZeroException) {
    Console.WriteLine("Cannot divide by zero");
}




Flashcard 9: LINQ
What is LINQ in C# and how is it used?

C#:
LINQ (Language Integrated Query) is used to query collections in a declarative way.
Example:
csharp
Copy
var squares = from x in Enumerable.Range(0, 5) select x * x;




Flashcard 10: Libraries and Frameworks
What are common libraries and frameworks in C#/.NET?

Web: ASP.NET, Blazor.
Data: LINQ, Entity Framework.
UI: Windows Forms, WPF.




Flashcard 11: Namespaces in C#
What is the role of namespaces in C#?

C#: Namespaces organize classes, structs, and other types into logical groups.
Example:
csharp
Copy
using System;
using System.Linq;




Flashcard 12: Properties in C#
What is the concept of properties in C#?

C#: Properties allow getting/setting fields with control.
Example:
csharp
Copy
public class Person {
    private string _name;
    public string Name {
        get { return _name; }
        set { _name = value; }
    }
}




Flashcard 13: Async/Await
How does asynchronous programming work in C#?

C#: Asynchronous programming is implemented using async and await.
Example:
csharp
Copy
public async Task<string> FetchData() {
    await Task.Delay(1000);
    return "Data fetched";
}




Flashcard 14: Delegates in C#
What are delegates in C#?

C#: Delegates are type-safe function pointers, allowing methods to be passed as parameters.
Example:
csharp
Copy
delegate void GreetDelegate();

GreetDelegate greet = () => Console.WriteLine("Hello!");
greet();




Flashcard 15: Garbage Collection
How does garbage collection work in C#?

C#: .NET uses a garbage collector that automatically manages memory. The GC.Collect() method can be called manually if needed, but generally not required.
This revised set focuses solely on C#/.NET concepts without the Python comparison, making it more focused on learning C# directly.




You said:
Fantastic. Can you make me some more of those?
ChatGPT said:
Sure! Here are additional 



Flashcards that cover more C#/.NET concepts:





Flashcard 16: Constructors in C#
How do constructors work in C#?

C#: A constructor is a special method used to initialize an object when it is created.
Example:
csharp
Copy
public class Car {
    public string Model { get; set; }
    
    public Car(string model) {
        Model = model;
    }
}




Flashcard 17: Inheritance
How is inheritance implemented in C#?

C#: Inheritance allows one class to inherit members (fields, properties, methods) from another class.
Example:
csharp
Copy
public class Animal {
    public void Speak() {
        Console.WriteLine("Animal speaks");
    }
}

public class Dog : Animal {
    public void Bark() {
        Console.WriteLine("Dog barks");
    }
}




Flashcard 18: Interfaces
What are interfaces in C#?

C#: An interface defines a contract that classes must implement. It can contain methods, properties, and events.
Example:
csharp
Copy
public interface IAnimal {
    void Speak();
}

public class Dog : IAnimal {
    public void Speak() {
        Console.WriteLine("Dog barks");
    }
}




Flashcard 19: Static Classes and Methods
What are static classes and methods in C#?

C#: A static class cannot be instantiated. Static members belong to the type itself, not an instance.
Example:
csharp
Copy
public static class MathUtils {
    public static int Add(int x, int y) {
        return x + y;
    }
}




Flashcard 20: Enums
How do enums work in C#?

C#: An enum is a distinct value type that defines a set of named constants.
Example:
csharp
Copy
public enum Day { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday }

Day today = Day.Monday;




Flashcard 21: Event Handling and Delegates
How do events and delegates work together in C#?

C#: Events use delegates to provide a way for a class to notify other classes when something happens.
Example:
csharp
Copy
public delegate void EventHandler();

public class Publisher {
    public event EventHandler Notify;
    
    public void RaiseEvent() {
        Notify?.Invoke();
    }
}

public class Subscriber {
    public void OnNotify() {
        Console.WriteLine("Event triggered!");
    }
}




Flashcard 22: Indexers
What are indexers in C#?

C#: Indexers allow objects to be indexed like arrays. They enable you to access elements in an object using the array-like syntax.
Example:
csharp
Copy
public class Student {
    private string[] grades = new string[3];

    public string this[int index] {
        get { return grades[index]; }
        set { grades[index] = value; }
    }
}




Flashcard 23: Delegates vs Events
What’s the difference between delegates and events in C#?

C#: A delegate is a type that holds references to methods, while an event is a special type of delegate that can only be invoked by the class that declares it, enforcing encapsulation.
Example:
csharp
Copy
public delegate void MyEvent();
public event MyEvent EventTriggered;




Flashcard 24: Nullable Types
How do nullable types work in C#?

C#: Nullable types allow value types (like int) to represent null in addition to their normal range of values.
Example:
csharp
Copy
int? x = null;




Flashcard 25: Tuples
What are tuples in C# and how are they used?

C#: Tuples allow grouping multiple values into a single object without defining a class.
Example:
csharp
Copy
var person = (Name: "John", Age: 30);
Console.WriteLine(person.Name);  // Output: John




Flashcard 26: Extension Methods
What are extension methods in C#?

C#: Extension methods allow you to add functionality to existing types without modifying their source code.
Example:
csharp
Copy
public static class StringExtensions {
    public static bool IsNullOrEmpty(this string str) {
        return string.IsNullOrEmpty(str);
    }
}




Flashcard 27: LINQ Methods (e.g., Select, Where, OrderBy)
How do you use LINQ methods like Select, Where, and OrderBy in C#?

C#: LINQ methods provide a concise way to query and manipulate collections.
Example:
csharp
Copy
var numbers = new List<int> { 1, 2, 3, 4, 5 };
var evenNumbers = numbers.Where(n => n % 2 == 0).OrderBy(n => n);




Flashcard 28: Generics
What are generics in C#?

C#: Generics allow you to define classes, methods, or data structures with type parameters, enabling type safety and reusability.
Example:
csharp
Copy
public class Box<T> {
    public T Value { get; set; }
}

var intBox = new Box<int> { Value = 10 };




Flashcard 29: Lambda Expressions
What are lambda expressions in C# and how are they used?

C#: Lambda expressions provide a concise way to represent anonymous methods.
Example:
csharp
Copy
Func<int, int, int> add = (x, y) => x + y;




Flashcard 30: Reflection
What is reflection in C#?

C#: Reflection allows you to inspect the metadata of types (classes, properties, methods, etc.) at runtime.
Example:
csharp
Copy
var type = typeof(String);
Console.WriteLine(type.FullName);  // Output: System.String