import math, random
from fractions import Fraction

pi = math.pi
tau = 2*pi
e = math.e
epsilon = 0.000000001
phi = (1+math.sqrt(5))/2
infinity = float("infinity")
euler = 0.5772156649

def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return list(result)

def prime_factors(x):
    i = 2
    factors = []
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            factors.append(i)
    if x > 1:
        factors.append(x)
    return factors

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def sieve(x):
    size = x//2
    prime_sieve = [1]*size
    limit = int(x**0.5)
    for i in range(1,limit):
        if prime_sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            prime_sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(prime_sieve) if v and i>0]

def prod(arr):
    product = 1
    for num in arr:
        product *= num

    return product

def is_prime(x):
    if( sum(factors(x)) == x+1 ):
        return True
    else:
        return False

def next_prime(x):
    prime = x+1
    while True:
        if( is_prime( (prime) ) ):
            break
        else:
            prime += 1

    return prime

def has_duplictaes(list):
    return (len(list) != len(set(list)))

def mobius(x):
    if( has_duplictaes( prime_factors(x) ) == True ):
        return 0
    elif ( x == 1 ):
        return 1
    else:
        return -1**len(prime_factors(x))

def mertens(x):
    add = []
    for i in range(1, x + 1):
        add.append(mobius(i))

    return add

def run_poly(poly, num):
    # [[coefficent, power],[coefficent, power],[coefficent, power]...]
    addition = 0
    for i in range(0, len(poly)):
        term = (num**poly[i][1])*poly[i][0]
        addition += term

    return addition


def derivative_poly(poly, order = 1):
    # [x,y] -> [xy, y-1]
    derivative = []
    for i in range(0, len(poly)):
        partOne = poly[i][0]*poly[i][1]
        partTwo = poly[i][1]-1

        if partOne < 0:
            partOne = 0

        if partTwo < 0:
            partTwo = 0

        derivative.append( [poly[i][0]*poly[i][1], poly[i][1]-1] )

    return derivative

def newton_root(poly, limit = 10000, guess = 2):
    derivative = derivative_poly(poly)
    previous = guess
    nextVal = 0

    for i in range(0, limit):
        nextVal = previous - ( run_poly(poly, previous) )/( run_poly(derivative_poly(poly), previous) )
        previous = nextVal

    return previous


def visual_root_find(poly, limit = 10000, guess = 2):
    root = newton_root(poly, limit, guess)
    polyStr = convert_polynomial_to_string(poly, False)
    check = polyStr.replace("x", "*" + str(root))

    print("Polynomial Enterered: " + polyStr)
    print("Root Found: " + str(root))
    print("Check: " + str(check) + " = " + str(run_poly(poly, root)))

def sum_multiples(limit, firstMultiple, secondMultiple):
    sum = 0
    for i in range(0, limit):
        if i % firstMultiple == 0 or i % secondMultiple == 0:
            sum += i

    return sum

def nth_fib(n):
    if n <= 1:
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2)

def sum_fib_under_x(x):
    sum = 0
    i = 1
    while True:
        print(i)
        if nth_fib(i) > x:
            break
        else:
            if nth_fib(i) % 2 == 0:
                sum += nth_fib(i)

        i += 1

    return sum


def largest_prime_factor(x):
    return max(prime_factors(x))

def is_palindrome(x):
    new = list( str(x) )[::-1]
    return new == list( str(x) )

def largest_palindrome_product(digits):
    allNums = []
    for i in range(10**(digits-1), (10**digits)-1):
        for j in range(10**(digits-1), (10**digits)-1):
            if is_palindrome(i*j):
                allNums.append(i*j)

    return max(allNums)

def difference_between_sum_squares_vs_square_sum(limit):
    numbers = []
    for i in range(1, limit+1):
        numbers.append(i)

    sum_squares = sum(map(lambda x: x**2, numbers))
    square_sum = sum(numbers)**2

    return square_sum - sum_squares


def can_be_divided(num, arr):
    count = 0
    for i in range(0, len(arr)):
        if num % arr[i] == 0:
            count += 1
        else:
            break

    return count == len(arr)

def nth_prime(x):
    i = 1
    count = 0
    while True:
        if(count == x):
            return i
        else:
            i = next_prime(i)
            count += 1

def collatz(x, count = 1):
    if x == 1:
        return count

    if x % 2 == 0:
        return collatz(x/2, count + 1)
    else:
        return collatz((3*x)+1, count + 1)

def longest_collatz_sequence(limit):
    numbers = range(1, limit + 1)
    cs = []

    for i in range(len(numbers)):
        c = collatz(i)
        print(c)
        cs.append(c)

    return max(cs)

def max_prime_factor(x):
    return max(prime_factors(x))

def digits(x):
    return [int(d) for d in str(x)]

def digit_product(x):
    product = 1
    x_digits = x
    for i in range(0, len(x_digits)):
        product *= x_digits[i]

    return product

def digits_to_num(arr):
    string = ""
    for i in range(0, len(arr)):
        string += str(arr[i])

    return int(string)

def largest_digit_product(x, bite):
    x_digits = digits(x)
    arr_of_digits = []
    products = []
    for i in range(0, len(x_digits) - bite):
        arr_of_digits.append( x_digits[i:i+bite] )

    print(arr_of_digits)
    for i in range(0, len(arr_of_digits)):
        products.append( digit_product(arr_of_digits[i]) )

    return max(products)

def is_pythagorean_triple(arr):
    return arr[0]**2 + arr[1]**2 == arr[2]**2

def sum_of_primes(limit):
    return sum(sieve(limit))

def totient(n):
    summation = 0
    for k in range(1, n+1):
        summation += gcd(k,n)*math.cos((tau*k)/n)

    return summation

def lambert_w(x, limit = 100):
    w = x
    while True:
        ew = math.exp(w)
        wNew = w - (w * ew - x) / (w * ew + ew)
        if abs(w - wNew) <= epsilon: break
        w = wNew
    return w

def sum_digits(x):
    return sum(digits(x))

def nth_tri(x):
    return (x*(x+1))/2

def first_triangle_with_x_divisors(x):
    i = 1
    leFin = 0
    while True:
        n = nth_tri(i)
        print(n, len(factors(n)))
        if len(factors(n)) >= x:
            leFin = i
            break


        i += 1

    return nth_tri(leFin)

def goldbach(x):
    for i in range(0, x):
        for j in range(0, x):
            if i+j == x and is_prime(i) and is_prime(j):
                return [i,j]

def calculate_limit(poly, value):
    leftSum = run_poly(poly, value - 10**(-10))
    rightSum = run_poly(poly, value + 10**(-10))

    return (leftSum+rightSum)/2

def number_length(x):
    return len(str(x).replace('.',''))

def length_of_decimal(x):
    return len(str(x).split("_", 1)[-1])

def add_fractions(frac_1, frac_2):
    frac_1 = frac_1.split("/")
    frac_2 = frac_2.split("/")

    numerator = [int(frac_1[0]), int(frac_2[0])]
    denominator = [int(frac_1[1]), int(frac_2[1])]

    top = numerator[0]*denominator[1] + denominator[0]*numerator[1]
    bottom = denominator[0] * denominator[1]

    gcdNum = gcd(top, bottom)
    top /= gcdNum
    bottom /= gcdNum

    return str(top) + "/" + str(bottom)

    # a/b + c/d = ad+bc/bd

def convert_to_fraction(x):
    return str(Fraction(x))


def continued_fraction(x, limit):
    expansion = []
    prev = x
    nxt = 0

    for i in range(0, limit):
        nxt = 1/(prev - math.floor(prev))
        expansion.append( int(math.floor(prev)))
        prev = nxt

    return expansion

def continued_fraction_at_point(x, limit, fraction = True):
    continued = continued_fraction(x, limit)
    summation = 0

    for i in range(1, limit):
        summation = 1/(continued[-i]+summation)

    if(fraction == True):
        return str(Fraction(summation + continued[0]))
    else:
        return summation + continued[0]

def gamma(x):
    return math.gamma(x)

def tetrarion(x, limit):
    if limit == infinity:
        if x < e**(1/e) and x > e**(-e) and x != 1:
            return (lambert_w( -math.log(x) ))/(-math.log(x))
        elif x == 1:
            return 1
        else:
            return infinity

    else:
        powers = x
        for i in range(0, limit):
            powers = powers**x

        return powers

def square_super_root(x):
    # Number y such that x^x = y
    return math.exp(lambert_w( math.log(x) ))

def eta(s, limit = 10000):
    summation = 0
    for k in range(1, limit+1):
        numerator = (-1)**(k-1)
        denominator = k**s

        summation += float(numerator)/float(denominator)

    return summation


def zeta(s, limit = 10000, etaOptim = True):
    if etaOptim  == True:
        return eta(s)/(1-(2**(1-s)))
    else:
        summation = 0
        for i in range(1, limit+1):
            summation += float(1)/float(i)**s

        return summation

def pi_prime_count(x):
    return len(sieve(x))

def is_perfect(x):
    return sum(factors(x))-x == x

def next_perfect(x):
    i = x+1
    while is_perfect(i) != True:
        i += 1

    return i

def nth_perfect(x):
    curr = 0
    for i in range(0, x):
        curr = next_perfect(curr)

    return curr

def three_numbers_that_sum_to_x(x):
    vals = []
    for i in range(1, x):
        for j in range(1, x):
            for k in range(1, x):
                if i+j+k == x:
                    vals.append([i,j,k])

    return vals

def pythagorean_triples_up_that_sum_to_x(x):
    vals = []
    partitions = three_numbers_that_sum_to_x(x)
    for i in range(0, len(partitions)):
        if is_pythagorean_triple(partitions[i]):
            vals.append(partitions[i])

    return vals

def navigate_grid(arr, row_length, curr, direction):
    # 1 = Down, -1 = Up
    # 2 = Forwards, -2 = Backwards
    # 3 = Diagonally Downwards, -3 = Diagonally Upwards.

    if row_length**2 != len(arr) or row_length < 2:
        print("The grid is to small or it isn't a square at that row_length.")
        return None

    if direction == 1:
        return arr[curr + row_length]
    elif direction == -1:
        return arr[curr - row_length]
    elif direction == 2:
        return arr[curr + 1]
    elif direction == -2:
        return arr[curr - 1]
    elif direction == 3:
        return arr[curr + (row_length + 1)]
    elif direction == -3:
        return arr[curr - (row_length - 1)]

def number_of_ways_through_n_by_n_grid(n):
    return (factorial(2*n))/(factorial(n)**2)

def nth_bernoulli(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fraction(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])

    return A[0]

def diagamma(x, limit = 10000):
    summation = 0
    for i in range(limit):
        summation += (x-1)/( (i+1)*(i+x) )

    return summation - euler

def prime_zeta(s, limit = 400):
    count = 0
    i = 2
    summation = 0

    while True:
        if count < limit:
            summation += 1.0/float(i**s)
        else:
            break

        count += 1
        i = next_prime(i)

    return summation

def convert_polynomial_to_string(poly, omit_ones = True):
    strings = []
    for i in range( len(poly) ):
        coe = (poly[i][0])
        power = (poly[i][1])

        if(abs(coe) == coe):
            if coe == 1 and power == 0:
                part = "1"

            elif coe == 1 and power == 1 and omit_ones == True:
                part = "x"

            elif coe == 1 and omit_ones == True:
                part = "x^" + str(power)

            elif power == 1:
                part = str(coe) + "x"

            else:
                part = str(coe) + "x^" + str(power)

        else:
            if coe == -1 and power == 0:
                part = "-1"

            elif coe == -1 and power == 1 and omit_ones == True:
                part = "-x"

            elif coe == -1  and omit_ones == True:
                part = "-x^" + str(power)

            elif power == 1:
                part = str(coe) + "x"

            else:
                part = str(coe) + "x^" + str(power)

        strings.append(part)

    final = ""
    for i in range( len(strings) ):
        if i == len(strings) - 1:
            final += strings[i]

        else:
            if( list(strings[i+1])[0] == "-" ):
                next_part = list(strings[i+1])
                del next_part[0]
                strings[i+1] = "".join(next_part)

                final += strings[i] + " - "

            else:
                final += strings[i] + " + "


    return final

def general_sum(n, x, func):
    summation = 0
    for i in range(x, n+1):
        summation += func(i)

    return summation

def general_product(n, x, func):
    product = 1
    for i in range(x, n+1):
        product *= func(i)

    return product

def ackerman(x, y):
    if x == 0:
        return y + 1

    elif y == 0:
        return ackerman(x - 1, 1)

    else:
        return ackerman( x - 1, ackerman( x, y - 1 ) )

def diagonal(x):
    return ackerman(x, x)

def evaluate_term(string):
    string = list(string)
    power = 0

    if "^" in string:
        temp = "".join(string).split("^")
        power = float(temp[-1])

    if "x" not in string and string[0] != "-":
        return [ float(string[0]), 0 ]

    elif "x" not in string and string[0] == "-":
        return [ -float(string[1]), 0 ]

    elif "^" not in string and string[0] != "-":
        return [ float(string[0]), 1 ]

    elif "^" not in string and string[0] == "-":
        return [ -float(string[1]), 1 ]

    elif string[0] == "x":
        return [1, power]

    elif string[0] == "-":
        return [-float(string[1]), power]

    else:
        return [float(string[0]), power]

def convert_string_into_polynomial(string):
    terms = string.split(" ")
    parts = []
    final = ""

    if(list(terms[0])[0] == "-"):
        terms.insert(0, "-")

    else:
        terms.insert(0, "+")

    iterator = 0
    while True:
        if iterator > len(terms)/2+1:
            break

        else:
            parts.append( terms[iterator] + terms[iterator + 1] )

        iterator += 2


    for i in range(len(parts)):
        parts[i] = parts[i].replace("+","")

    for i in range(len(parts)):
        parts[i] = evaluate_term(parts[i])

    return parts

def random_polynomial(order, pretty = False):
    polynomial = []
    for i in range( order ):
        polynomial.append( [ random.randint(1, 20), i ] )

    if pretty == True:
        return convert_polynomial_to_string(polynomial)

    else:
        return polynomial

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(str(l)), n):
        yield int(str(l)[i:i + n])

def grid_sum(l, n):
    return sum(list(chunks(l, n)))

def list_of_x_primes(x):
    primes = []
    curr = 2
    for i in range(1, x+1):
        primes.append(curr)
        curr = next_prime(curr)

    return primes
