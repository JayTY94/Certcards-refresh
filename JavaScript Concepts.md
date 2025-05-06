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



With Boolean(value) you can convert any value to a boolean. There is a fixed set of values, so called falsy values, that convert to false. Most importantly, false, 0, empty string, null, undefined and NaN are falsy.



Boolean(-1);
// => true

Boolean(0);
// => false

Boolean(' ');
// => true

Boolean('');
// => false


For arrays, the String function will apply the string conversion for each element and join the results with a comma. You can also apply the join method yourself, e.g. to customize the separator. Note that in these cases null and undefined will be converted to an empty string.

String([42, null, true, 'abc']);
// => '42,,true,abc'




For objects, by default String returns an unhelpful text.

String({ key: 'value' });
// => '[object Object]'



In certain contexts, JavaScript will automatically convert a value to another data type before it evaluates some statement. This implicit conversion is called type coercion.


Coercion to boolean commonly occurs for

the condition of an if statement
the first operand of the ternary operator ?
the operand of the logical NOT operator !
the operands of the logical AND && and OR || operators (the result of the expression is one of the operands, not necessarily a boolean)





If the addition operator + is used for primitive values and one operand is a string, the other one will be coerced into a string as well. The conversion logic is the same as when using the String function. Afterwards, the two strings are concatenated.

let name;
'hello ' + name;
// => 'hello undefined'




Many operators coerce the operands into numbers (if necessary) according to the logic of the Number function explained above.

Arithmetic operators: + (if no string is involved), -, *, /, %, **
Unary plus and unary negation operators: +, -
Relational operators (for non-string operands): >, >=, <, <=
Bitwise operators: |, &, ^, ~



NaN is not equal to itself (NaN !== NaN), so using case NaN: in a switch statement will not work.
Use the isNaN function to check for NaN values before the switch statement or within a switch statement using switch (true).




Ensure to use the comparison operator === instead of the assignment operator = when comparing values in switch cases. In an exercise, I had something like 
case converted_value = 0
instead of
case converted_value === 0
and that screwed up all of the following cases.




By default, all parameters defined in the function declaration are optional in JavaScript. If you provide fewer arguments than there are parameters, the missing arguments will be undefined inside the function, see Null and Undefined.




In many cases, it makes sense to assign a more appropriate default value than undefined. This can be done by specifying default parameters directly in the function definition.

function someName(param1 = defaultValue1, param2 = defaultValue2) {
  // ...
}



In JavaScript, you can only return exactly one value. If you want to pass more information, you need to combine it into one entity first, usually into an object, or an array.

function divide(a, b) {
  return {
    quotient: Math.floor(a / b),
    remainder: a % b,
  };
}


Callback functions are functions passed as arguments. This programming pattern creates a sequence of function calls in both synchronous and asynchronous programming. Writing a callback function is no different from writing a function; however, the callback function must match the signature defined by the calling function.



To create a deep copy of an object in JavaScript, you can use the JSON.parse(JSON.stringify(object)) method. This approach works well for simple objects, such as those with string:number pairs, and ensures that the original object remains unmodified.




JavaScript's array destructuring syntax is a concise way to extract values from an array and assign them to distinct variables. In this example, each value in the numberOfMoons array is assigned to its corresponding planet:

const numberOfMoons = [0, 2, 14];
const [venus, mars, neptune] = numberOfMoons;

neptune;
// => 14




When ... appears on the left-hand side of an assignment, those three dots are known as the rest operator. The three dots together with a variable name is called a rest element. It collects zero or more values, and stores them into a single array.

const [a, b, ...everythingElse] = [0, 1, 1, 2, 3, 5, 8];

everythingElse;
// => [1, 2, 3, 5, 8]





When ... appears on the right-hand side of an assignment, it's known as the spread operator. It expands an array into a list of elements. Unlike the rest element, it can appear anywhere in an array literal expression, and there can be more than one.

const oneToFive = [1, 2, 3, 4, 5];
const oneToTen = [...oneToFive, 6, 7, 8, 9, 10];

oneToTen;
// => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




The basic syntax for a string template in JavaScript uses backticks (`) and ${} for embedding expressions.
  const name = 'Jay';
  const greeting = `Hello, ${name}!`;
  console.log(greeting); // Output: Hello, Jay!





Front: How do you create multiline strings using string templates?
Back: String templates allow for multiline strings without the need for concatenation or escape characters.
  const multiline = `This is a string
  that spans multiple
  lines.`;
  console.log(multiline);


Front: Can you call functions within a string template?

Back: Yes, you can call functions within ${} in a string template.
  function getName() {
    return 'Jay';
  }
  const greeting = `Hello, ${getName()}!`;
  console.log(greeting); // Output: Hello, Jay!





Front: Can you nest string templates within each other?
Back: Yes, you can nest string templates within each other.
  const name = 'Jay';
  const nestedTemplate = `Hello, ${`dear ${name}`}!`;
  console.log(nestedTemplate); // Output: Hello, dear Jay!


Front: What are tagged templates and how do you use them?

Back: Tagged templates allow you to parse template literals with a function. The function receives the template string and the values as arguments.
  function tag(strings, ...values) {
  console.log(strings); // Array of string segments
  console.log(values);  // Array of values
  return 'Tagged template result';
}
const result = tag`Hello, ${name}!`;
console.log(result); // Output: Tagged template result


Front: How do you access the raw string content of a template literal?

Back: You can access the raw string content using the String.raw tag.
  const rawString = String.raw`Hello\nWorld`;
  console.log(rawString); // Output: Hello\nWorld


Syntax to convert an aray to a set and back again to remove duplicates
  export function removeDuplicates(playlist) { //playlist is an array of songs
    const play_set = new Set (playlist)
    return Array.from(play_set)
  }


Checks potentially very long playlsit for a specific track by converting to a set and using the Set.has() funciton.
  export function hasTrack(playlist, track) {
    const play_set = new Set (playlist)
    return play_set.has(track)
  }