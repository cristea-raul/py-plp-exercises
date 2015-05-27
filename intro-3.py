import sys

if len(sys.argv) != 2:
    print('Requires 1 argument, no more, no less.')
    exit()

try:
    no = int(sys.argv[1])
except Exception:
    print('Must be an integer.')
    exit()


def gen_odd(k):
    return k * 10**(len(str(k))-1) + int(str(k//10)[::-1])


def gen_even(k):
    return k * 10**(len(str(k))) + int(str(k)[::-1])


def main():
    gen = 0
    k = 0
    even = False
    result = []

    while gen < no:
        result.append(gen)
        last = k % 10
        if last == 9:
            if even:
                even = False
                k += 1
            else:
                even = True
                k -= 9
        k += 1

        gen = gen_even(k) if even else gen_odd(k)

    print(result)

main()