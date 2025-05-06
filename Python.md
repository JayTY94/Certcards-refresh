Thread
A thread is an independent sequence of execution within a program. Multiple threads can run concurrently within the same process.

Global Interpreter Lock (GIL)
The GIL is a mutex in CPython that ensures only one thread executes Python bytecode at a time, affecting true parallel execution of threads.

Race Condition
A race condition occurs when multiple threads access and modify shared data concurrently, leading to unpredictable or incorrect results if not managed properly.

Lock (Mutex)
A lock is a synchronization primitive used to control access to a shared resource, ensuring that only one thread can access a specific block of code at a time.

Semaphore
A semaphore is a synchronization tool that limits the number of threads that can access a resource simultaneously, often used for managing a pool of resources.

Deadlock
Deadlock happens when two or more threads are waiting on each other to release locks, causing the program to become stuck with none of the threads progressing.

Thread Safety
Thread safety means that code or data structures function correctly when accessed by multiple threads simultaneously, usually achieved with proper synchronization.

Daemon Thread
Daemon threads are background threads that do not prevent the program from exiting; they automatically close when all non-daemon threads have finished.

Context Switching
Context switching is the process of storing and restoring the state of a thread so that execution can resume later, which can introduce performance overhead.

Thread Pool Executor
A thread pool executor, provided by the concurrent.futures module, is an abstraction that manages a pool of worker threads and simplifies scheduling and executing asynchronous tasks.



Coroutine
An async def function in Python that can pause at await expressions and resume later, enabling non-blocking asynchronous execution.

Coroutine Object
The result of calling an async def function; it must be awaited or scheduled with the event loop to execute.

await
A keyword that pauses an asynchronous Python function until the awaited coroutine or awaitable completes.

async
A keyword used in Python to declare an asynchronous function (async def), enabling the use of await inside it.

Event Loop
The core of Python’s asyncio system, which schedules and runs asynchronous tasks cooperatively on a single thread.

asyncio.run()
A high-level function in Python to start the event loop, run an async function, and close the loop automatically.

asyncio.create_task()
Schedules a coroutine to run concurrently as a Task in Python's event loop and starts it immediately.

Task
A wrapper around a coroutine in Python’s asyncio that is managed by the event loop and can be cancelled, awaited, or monitored.

asyncio.gather()
Runs multiple asynchronous Python tasks concurrently and waits for all to finish, optionally collecting exceptions.

asyncio.as_completed()
Runs multiple coroutines concurrently and yields their results in the order they complete, useful in Python for out-of-order processing.

asyncio.CancelledError
An exception in Python that is raised inside a coroutine when it’s cancelled, allowing it to perform cleanup.

asyncio.wait_for()
Runs a coroutine with a timeout in Python; raises TimeoutError if the coroutine doesn’t finish in time.

asyncio.shield()
Prevents a coroutine in Python from being cancelled even if the calling task is, ensuring it runs to completion.

asyncio.Semaphore
A concurrency control mechanism in Python’s asyncio used to limit how many coroutines run at once.

Blocking Code
Code like time.sleep() that halts the event loop and prevents other asynchronous Python tasks from running—should be avoided.

Non-blocking I/O
A key feature of async Python where I/O operations (e.g., file or network access) don’t block the event loop.

asyncio.to_thread()
Runs a blocking function in a background thread from an async Python function, allowing mixing of sync and async code.

Awaitable
Any object in Python that can be used with await, including coroutine objects, asyncio.Future, and some libraries’ types.

asyncio.Future
A low-level object representing a pending result in Python's asyncio; used internally by Tasks.

async with (async context manager)
Manages asynchronous resources in Python like network sessions or database connections with proper cleanup.

async for (async iterator)
Used to iterate over async sequences in Python, such as streaming data or asynchronous file lines.

Concurrency (Asyncio)
Running multiple asynchronous Python tasks in overlapping time, achieved cooperatively through the event loop.

Parallelism
Running code in true simultaneous execution on multiple cores; not directly supported by asyncio, which is single-threaded.

Cooperative Multitasking
The async model in Python where tasks yield control voluntarily (e.g., via await) instead of being preempted.

aiohttp
An asynchronous HTTP client/server library in Python used to make non-blocking web requests.

Race Condition
An issue in async Python code where multiple coroutines access shared data without proper coordination, leading to bugs.

Deadlock
A state in async Python where tasks wait on each other indefinitely, halting progress—usually due to poor coordination.

asyncio.Lock
An asynchronous lock in Python used to prevent multiple coroutines from accessing a shared resource at the same time.

asyncio.Queue
An async-safe queue in Python used for communication between producer and consumer coroutines.

Structured Concurrency
A design principle (used in Trio) ensuring all async Python tasks are scoped and cleaned up together, reducing leaks and bugs.

Timeouts
Techniques like asyncio.wait_for() used in Python to limit how long a coroutine can run before it's cancelled.

Throttling
Limiting concurrency in Python async code (e.g., with a Semaphore) to avoid overwhelming servers or APIs.

Backpressure
A condition in async Python where producers send data faster than consumers can process; addressed using queues or throttling.

Idle Task
An asynchronous Python coroutine that’s currently waiting (e.g., on I/O or sleep), allowing others to run in the meantime.

return_exceptions=True (in gather)
A parameter in Python's asyncio.gather() that returns exceptions as part of the results instead of cancelling all tasks on error.

pytest-asyncio
A Python testing plugin that allows you to write and run tests for asynchronous code using async def and await.