'''
                    Concurrency - LeetCode
'''

''' Concepts #1
 = Process v/s Thread: Applied Interchangeably, Not necessarily applies to processes running on
    independent CPU, but also to those interleaved onto the same CPU.
 = Goal: Enable multi-tasking in shared resources environment

Concurrency Issues can be categorized to 3 types:
-------------
 A) Race Condition:
        Program ends in undesirable state (output), due to mis-enforced execution sequences among processes.
 B) Deadlock:
        When concurrent processes end up waiting on mutual resources, resulting in none of them making progress.
        ex: B wants A to give resource to go-ahead, and A needs B to give resource for the next step.
 C) Resource Starvation:
        Concurrent processes are constantly denied access to resources to progress its work.

Race-Free Concurrency
-------------
Common Characteristics:
    - Multiple processes sharing common resources (ex: `balance` variable in bank API)
Solution:
    - Coordination of resources sharing to avoid concurrency problems.
    - By ensuring exclusivity of the critical code section, we avoid programs from running into
      inconsistent states, i.e., at a given time, only single thread can enter the critical section
    - 'Mechanism as a Lock': to restrict access to critical section

"Our Mechanism possess 2 capabilities":
    i) Access control on critical sections.
   ii) Notification on the 'blocked/waiting/sleeping' threads (notify of the access availability)

Task-1: Pair Synchronization (Execute in-order):
-------------
Shared Variables:
1) First Job Done: Enforce execution b/w first & second job.
2) Second Job Done: Enforce execution b/w second & third job.

Solutions: Barrier, Lock, Event, Semaphore, Condition

1. *Lock (Mutex): Abstraction used to enforce execution order. Controls single thread access to a given resource.
    Mutex: Mutual Exclusion. Special case of semaphore where n=1
2. Barrier: Once a barrier threshold is reached, every thread will be passed through: batched-processes.
3. Condition: More fine-grained control on after-events of releasing a lock.
4. *Semaphore: Framework to share resources among limited number of threads (Useful in chaining thread execution).
    When we allow only 'n' threads to concurrently access resources, and remaining should wait.
    Types: Binary Semaphore (0/1 resources) v/s Counting Semaphore (1+ resources)
5. Event: Equivalent to Barrier(1), that can be reset easily.
'''

##########################
#    Using lock          #
##########################
from threading import Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            printThird()

# Output: "firstsecondthird"

##########################
#    Using Semaphore     #
##########################
from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))

    def first(self, printFirst):
        printFirst()
        self.gates[0].release()

    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird):
        with self.gates[1]:
            printThird()

##########################
#    Using Barrier       #
##########################

from threading import Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2)
        self.second_barrier = Barrier(2)

    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird):
        self.second_barrier.wait()
        printThird()

##########################
#    Using Event         #
##########################

from threading import Event

class Foo:
    def __init__(self):
        self.done = (Event(),Event())

    def first(self, printFirst):
        printFirst()
        self.done[0].set()

    def second(self, printSecond):
        self.done[0].wait()
        printSecond()
        self.done[1].set()

    def third(self, printThird):
        self.done[1].wait()
        printThird()

##########################
#    Using Condition     #
##########################

from threading import Condition

class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()

'''
    Problem: Print FooBar Alternately
    Printing foobar alternately for a given 'n'
'''
# Using Semaphore

from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.gates = (Semaphore(1), Semaphore(0)) # default is 1, so Semaphore(1) = Semaphore()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.gates[0].acquire()
            printFoo()
            self.gates[1].release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.gates[1].acquire()
            printBar()
            self.gates[0].release()

# Using Lock
from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(), Lock())
        self.locks[1].acquire() # Note this is done in semaphore using 0/1

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.locks[0].acquire()
            printFoo()
            self.locks[1].release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.locks[1].acquire()
            printBar()
            self.locks[0].release()

'''
    Problem:  Traffic Light Controlled Intersection
    Design a deadlock-free traffic light controlled system at road intersection.
    Your answer is considered correct if it avoids cars deadlock in the intersection. Turning the light green on a road when it was already green is considered a wrong answer.
'''
from threading import Lock
class TrafficLight:
    def __init__(self):
        self._lock = Lock()
        self.roadInGreen = 1

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
        ) -> None:
        with self._lock:
            if roadId != self.roadInGreen:
                turnGreen()
                self.roadInGreen = roadId
            crossCar()


'''
    Problem: Print Zero Even Odd
    Suppose you are given the following code:

        class ZeroEvenOdd {
          public ZeroEvenOdd(int n) { ... }      // constructor
          public void zero(printNumber) { ... }  // only output 0's
          public void even(printNumber) { ... }  // only output even numbers
          public void odd(printNumber) { ... }   // only output odd numbers
        }
        The same instance of ZeroEvenOdd will be passed to three different threads: Thread A will call zero() which should only output 0's. Thread B will call even() which should only ouput even numbers. Thread C will call odd() which should only output odd numbers.Modify the given program to output the series 010203040506... where the length of the series must be 2n.
'''
from threading import Semaphore
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.semaphores = (Semaphore(), Semaphore(0), Semaphore(0))
        # Semaphore() = Semaphore(1) -> pass through

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.semaphores[0].acquire()
            printNumber(0)
            # Release lock for odd(), even() alternately
            (self.semaphores[1] if i%2 else self.semaphores[2]).release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.semaphores[1].acquire()
            printNumber(i)
            self.semaphores[0].release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.semaphores[2].acquire()
            printNumber(i)
            self.semaphores[0].release()

'''
    Problem:
'''

'''
    Problem:
'''

'''
    Problem:
'''


'''
    Problem:
'''


'''
    Problem:
'''


'''
    Problem:
'''

'''
    Problem:
'''

'''
    Problem:
'''
'''
    Problem:
'''

'''
    Problem:
'''
'''
    Problem:
'''
