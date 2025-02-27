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