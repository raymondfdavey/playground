import time
def fibonacci(n):
  if n<2:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
var = 50


start = time.time()
fibonacci(var)
end = time.time()
print("test one")
print(end - start)

start = time.time()
fib(var)
end = time.time()
print("test two")
print(end - start)