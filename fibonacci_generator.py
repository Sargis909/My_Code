def fibonacci_generator():
    a = b = 1  #Start number
    while True:
        yield a
        a , b = b , a + b 
fib = fibonacci_generator()
for i in fib:
    if i > 100: #End number
        break
    else:
        print('Generated: ' , i )
