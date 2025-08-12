
Event Loop
The engine that coordinates execution: it pulls tasks from the call stack and various queues (macrotasks & microtasks), ensuring non‑blocking behavior.

Call Stack
A LIFO stack of frames representing currently executing functions. When it’s empty, the event loop can pick up queued callbacks.

Macrotask (Task) Queue
Also called the “callback queue.” Holds callbacks from things like setTimeout, I/O events, and UI rendering.

Microtask Queue
Holds promise callbacks (.then, .catch, .finally) and process.nextTick in Node.js. Microtasks always run before the next macrotask.

Promise
An object representing the eventual outcome of an asynchronous operation:
  Pending – neither fulfilled nor rejected

  Fulfilled – operation succeeded, value available

  Rejected – operation failed, reason available

.then() / .catch() / .finally()
Methods on a Promise to handle its resolution (.then), rejection (.catch), or run code regardless of outcome (.finally).

Promise.all() / allSettled() / race() / any()
Utilities to coordinate multiple promises:

  all: wait for all to succeed (or fail-fast)

  allSettled: wait for all to settle, regardless of outcome

  race: settle as soon as one settles

  any: succeed as soon as one fulfills (rejects if all reject)


async function
Declares a function whose body can use await and which always returns a Promise:

  async function foo() { … }


await
Pauses execution of its enclosing async function until the given Promise settles, then returns its value (or throws its rejection).

setTimeout / setImmediate / process.nextTick
Node/browser scheduling APIs:

setTimeout(fn, 0): next macrotask

setImmediate(fn): “check” phase in Node (after I/O)

process.nextTick(fn): before the next event‑loop phase (Node only)

Callback Hell / Pyramid of Doom
Deeply nested callbacks that become hard to read and maintain. Promises and async/await help flatten this.

Fetch API
Modern browser API for HTTP requests, returning a Promise:

  fetch(url)
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));

    
Uncaught Promise Rejection
A Promise that rejects without any .catch() or try/catch(await). Can crash Node or trigger browser warnings.


A LIFO (Last-In, First-Out) stack is a way of organizing data so that the most recently added item is the first one you remove. Think of it like a stack of plates:

  You push a plate onto the top of the stack.

  You pop a plate off the top of the stack.



Use a private backing field for getter-only properties
  this._rows = …  
  get rows() { return this._rows }


Create N empty sub-arrays via Array.from
  let cols = Array.from({ length: n }, () => [])


Object literal { length: n } is just “array-like”: any object with a numeric .length can drive Array.from.
  let cols = Array.from({ length: n }, () => [])


Array.fill([]) shares the same array reference
  new Array(3).fill([])  
  // → [ref, ref, ref]


Generate distinct arrays with fill() + map()
  new Array(3).fill().map(() => [])  
  // → [[], [], []]


Split a string and convert parts to numbers
  "1 2 3".split(" ").map(Number)
