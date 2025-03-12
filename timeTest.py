from asyncore import loop
import time

def testExecution(predicate, loops = 1_000_000):
    start = time.time_ns()
    for i in range(loops):
        predicate()

    elapsed = time.time_ns() - start
    print(f"Execution took {elapsed} ns, each iteration {elapsed/loops}ns")

mystr = "banana"

def test1():
    myit = iter(mystr)
    x = next(myit)
    x = next(myit)
    x = next(myit)
    x = next(myit)
    x = next(myit)
    x = next(myit)

def test2():
    for c in mystr:
        x = c

testExecution(test1)
testExecution(test2)