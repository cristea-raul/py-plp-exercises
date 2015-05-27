import math
from random import sample
import time


# ex 11
def stopwatch(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret = f(*args, **kwargs)
        t2 = time.time()
        print('<Function "%s" executed in %0.3f ms>' % (f.__name__, (t2-t1)*1000))
        return ret
    return wrapper


# ex 12
def stopwatch_all(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret = f(*args, **kwargs)
        t2 = time.time()

        try:
            stopwatch_all.names.append(f.__name__)
        except:
            stopwatch_all.names = [f.__name__]

        try:
            stopwatch_all.total += t2-t1
        except:
            stopwatch_all.total = t2-t1

        return ret
    return wrapper


def read_number(msg='n='):
    try:
        no = int(input(msg))
    except ValueError:
        return 0, False
    return no, True


# ex 1
def is_prime(n):
    if n < 2:
        return False
    dlist = [d for d in range(2, int(math.sqrt(n)) + 1) if n % d == 0]
    return len(dlist) == 0


@stopwatch_all
# ex 3a
def fibo_i(n):
    if n < 1:
        return []

    if n == 1:
        return [0]

    ret = [0]
    last = 1
    while last < n:
        ret.append(last)
        last += ret[-2:][0]
    return ret


# ex 13
def memoize_is_an_ugly_word(f):
    memo_map = {}

    def wrapper(*args):
        i = args[0]
        if i not in memo_map:
            memo_map[i] = f(*args)
        return memo_map[i]
    return wrapper


# ex 3b
@memoize_is_an_ugly_word
@stopwatch_all
def fibo_r(n, result=None):
    if n < 1:
        return []

    if n == 1:
        return [0]

    if not result:
        result = [0, 1]

    s = result[-2:][0] + result[-1:][0]
    if s < n:
        result.append(s)
        return fibo_r(n, result)
    else:
        return result


# ex 4
def map2(func, iterable):
    return [func(x) for x in iterable]


# ex 5
def filter2(func, iterable):
    return [x for x in iterable if func(x)]


# ex 6
def reduce2(func, iterable, initializer):
    acc = initializer
    for x in iterable:
        acc = func(acc, x)
    return acc


@stopwatch_all
# ex 2
def all_primes(n):
    return filter2(is_prime, range(2, n))


@stopwatch
# ex 7
def custom_sum(val):
    array = [x for x in range(val)]
    array = filter2(lambda n: (n*n-1) % 3 == 0, array)
    print('7. For val = ' + str(val))
    print('Numbers that match the constraint are: ' + str(array))
    print('Sum is: ' + str(reduce2(lambda x, y: x+y, array, 0)))


# ex 8
def merge_sort(array):
    if len(array) < 2:
        return array

    left = array[:len(array)//2]
    right = array[len(array)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


@stopwatch_all
# ex 9
def search_dei(array, val):
    if len(array) == 1:
        return array[0] == val

    midpoint = len(array)//2
    return search_dei(array[:midpoint], val) if val < array[midpoint] else search_dei(array[midpoint:], val)


# ex 10
def a():
    try:
        a.n += 1
    except:
        a.n = 0
    return a.n


def main():
    res, success = read_number('Insert a number:\n')
    if success:
        print('It is ' + ('not ' if not is_prime(res) else '') + 'a prime.')
        print('Primes up to this number: ' + str(all_primes(res)))
        print('Fibo up to this number (itr): ' + str(fibo_i(res)))
        print('Fibo up to this number (rec): ' + str(fibo_r(res)))

        print('Squares: ' + str(map2(lambda x: x*x, range(res + 1))))

        custom_sum(res)

        randoms = sample(range(0, res), res)
        print('random: ' + str(randoms))
        sorted_arr = merge_sort(randoms)
        print('sorted: ' + str(sorted_arr))

        src, success = read_number('Search a number:\n')
        if success:
            if search_dei(sorted_arr, src):
                print('The number is in the array.')
            else:
                print('The number is not in the array.')

        print(str(a()) + ' ' + str(a()) + ' ' + str(a()))

        print('Functions: ' + str(stopwatch_all.names))
        print('Execution time: %0.3f ms.' % (stopwatch_all.total*1000))

        print('Memo-smth test:')
        stopwatch_all.names = []
        stopwatch_all.total = 0

        def test_fibo():
            fibo_r(1000000000000000)
            print('Functions: ' + str(stopwatch_all.names))
            print('Execution time: %0.3f ms.' % (stopwatch_all.total*1000))
            stopwatch_all.names = []
            stopwatch_all.total = 0

        test_fibo()

        test_fibo()

        test_fibo()
    else:
        print('A number would be preferable.')

if __name__ == "__main__":
    main()
