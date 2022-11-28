from __future__ import print_function

def fib(unsigned long long int n):
    #Print the Fibonacci series up to n.
    cdef unsigned long long int a = 0
    cdef unsigned long long int b = 1

    while b < n:
        # print(b, end=' ')
        a, b = b, a + b

    return a

