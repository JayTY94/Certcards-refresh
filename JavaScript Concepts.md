Unique Names: All JavaScript variables must be identified with unique names, called identifiers. These names can be short (like x and y) or more descriptive (like age, sum, totalVolume). Identifiers can contain letters, digits, underscores, and dollar signs, but they must begin with a letter, underscore, or dollar sign1.

Case Sensitivity: JavaScript identifiers are case-sensitive. This means that y and Y are considered different variables. It's important to be consistent with the use of case to avoid errors in your code1.

Reserved Words: Identifiers cannot be the same as JavaScript reserved words (keywords). Reserved words are predefined in the language and have special meanings, such as var, let, const, function, and class. Using these as identifiers will result in syntax errors1.

Object Literals: The most common way to create an object is using object literals, which are a list of name-value pairs inside curly braces {}. For example:
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};

Key-Value Pairs: Objects in JavaScript are collections of key-value pairs. Each key is a string (or symbol) and each value can be any data type, including other objects2.

Prototype-Based Inheritance: JavaScript uses prototype-based inheritance, meaning objects can inherit properties and methods from other objects. This is achieved through the prototype chain3.

Built-In Methods: JavaScript objects come with built-in methods like Object.keys(), Object.values(), and Object.entries() which allow you to interact with the object's properties in various ways4.


Dot Notation: You can add a new key-value pair to an object using dot notation. This is useful when you know the name of the property.

const obj = { key1: "value1", key2: "value2" };
obj.key3 = "value3"; // Adds key3 with value3


Bracket Notation: You can also use bracket notation, which is useful when the property name is dynamically determined.

const obj = { key1: "value1", key2: "value2" };
obj["key3"] = "value3"; // Adds key3 with value3



Object.assign(): This method can be used to copy the values of all enumerable own properties from one or more source objects to a target object.

const obj = { key1: "value1", key2: "value2" };
Object.assign(obj, { key3: "value3" }); // Adds key3 with value3


Delete Operator: You can remove a key-value pair from an object using the delete operator.

const obj = { key1: "value1", key2: "value2", key3: "value3" };
delete obj.key3; // Removes key3



Using for...in Loop: The for...in loop is useful for iterating over all enumerable properties of an object, including inherited ones. To avoid iterating over inherited properties, use the hasOwnProperty method1.

Using Object.keys() with for...of Loop: The Object.keys() method returns an array of the object's own enumerable property names. You can then use the for...of loop to iterate over these keys1.

Using Object.entries(): The Object.entries() method returns an array of the object's own enumerable property [key, value] pairs. You can use the for...of loop to iterate over these pairs1.



