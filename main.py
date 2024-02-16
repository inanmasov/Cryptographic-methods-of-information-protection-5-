from Crypto.Random.random import randint
from Crypto.Util.number import isPrime, GCD, inverse
from math import log
from datetime import datetime
#from sympy import prime


def generate_params(n):
    while True:
        a = randint(int(0), int(n - 1))
        x = randint(int(0), int(n - 1))
        y = randint(int(0), int(n - 1))
        b = (y ** 2 - x ** 3 - a * x) % n
        g = GCD(n, 4 * a ** 3 + 27 * b ** 2)
        res = list()
        if g == n:
            continue
        if g > 1:
            res.append(g)
            return res
        res.append(a)
        res.append(b)
        res.append(x)
        res.append(y)
        return res


def lenstra_algorithm(n, m):
    point = list()
    curve = list()
    while True:
        temp = generate_params(int(n))
        if len(temp) == 1:
            return temp[0], 0
        curve.append(temp[0])
        curve.append(temp[1])
        point.append(temp[2])
        point.append(temp[3])
        i = 1
        Q = list([point[0], point[1]])
        while i <= m:
            pi = prime(i)
            r = int((log(n, 2) / log(pi, 2)) * (1 / 2))
            if r == 0:
                r = 1
            print("Elleptic curve: y^2 = x^3 + {} * x + {}".format(curve[0], curve[1]))
            print("Point: ({}; {})".format(point[0], point[1]))
            for counter in range(1, r):
                for j in range(1, pi):
                    if Q[0] == point[0] and Q[1] == point[1]:
                        chisl = (3 * Q[0] ** 2 + curve[0]) % n
                        try:
                            znam = inverse((2 * Q[1]), n)
                        except:
                            break
                        L = chisl * znam % n
                        if 1 < GCD(L, n) < n:
                            return GCD(L, n), counter
                        x3 = (L ** 2 - 2 * Q[0]) % n
                        y3 = (L * (Q[0] - x3) - Q[1]) % n
                        Q[1] = y3
                        Q[0] = x3
                    else:
                        chisl = (point[1] - Q[1]) % n
                        try:
                            znam = inverse((point[0] - Q[0]), n)
                        except:
                            break
                        L = chisl * znam % n
                        if 1 < GCD(L, n) < n:
                            return GCD(L, n), counter
                        x3 = (L ** 2 - Q[0] - point[0]) % n
                        y3 = (L * (Q[0] - x3) - Q[1]) % n
                        Q[1] = y3
                        Q[0] = x3




'''val = int(input("Print your number: "))
border = int(input("Print your base: "))
if not isPrime(val):
    start_time = datetime.now()
    p, count = lenstra_algorithm(val, border)
    finish_time = datetime.now() - start_time
    q = val // p
    print(" P({}) * Q({}) = n({})".format(p, q, val))
    print("P Length = {}".format(len(bin(p)) - 2))
    print("Q Length = {}".format(len(bin(q)) - 2))
    print("Iterations = {}".format(count))
    print("Worktime: {}".format(finish_time))
else:
    print("{} is prime number".format(val))'''
import gmpy2

def generate_large_prime(bits):
    num = gmpy2.mpz_random(gmpy2.random_state(), 2 ** bits)
    prime_number = gmpy2.next_prime(num)
    return prime_number

prime_number = generate_large_prime(2000)
print(prime_number)