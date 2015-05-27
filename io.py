import os
import urllib.request
from functions import all_primes, read_number


def read_file(fn):
    try:
        f = open(fn, 'r')
    except:
        print('What, no file? Eeh..')
        return False, None
    return True, f


# ex 1
def sum_file(fn):
    success, f = read_file(fn)
    if not success:
        return

    s = 0
    for line in f:
        n = 0
        try:
            n = int(line)
        except:
            pass
        s += n
    print(s)
    f.close()


# ex 2
def write_primes(fn, val):
    f = open(fn, 'w')

    primes = all_primes(val)
    for n in primes:
        print(str(n), file=f)
    f.close()


# ex 3
def find_words(fn):
    success, f = read_file(fn)
    if not success:
        return

    delimiters = ['.', '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']
    words = []
    dupes = ['']
    for line in f:
        split_line = line.split()
        for delim in delimiters:
            new_line = []
            for sequence in split_line:
                new_line += sequence.split(delim)
            split_line = new_line
        for x in split_line:
            if x not in dupes:
                if x in words:
                    words.remove(x)
                    dupes.append(x)
                else:
                    words.append(x)
    print(words)
    f.close()


def merge(array1, array2):
    result = []
    while array1 and array2:
        while array1 and array1[0] <= array2[0]:
            result.append(array1.pop(0))
        if not array1:
            break
        while array2 and array1[0] > array2[0]:
            result.append(array2.pop(0))
    result.extend(array1)
    result.extend(array2)
    return result


# ex 4
def sort(out_file, in_files):
    result = []
    for fn in in_files:
        success, f = read_file(fn)
        if not success:
            continue

        array = []
        for line in f:
            try:
                n = int(line)
            except:
                continue
            array += [n]
        print(array)
        result = merge(result, array)
        f.close()

    outf = open(out_file, 'w')

    for n in result:
        print(str(n), file=outf)
    outf.close()


# ex 5
def fetch_links(url):
    f = urllib.request.urlopen(url).read().decode('ascii', 'ignore')
    start = 0
    while True:
        start = f.find('http', start)
        if start == -1:
            # not found
            break

        k = start

        # ignore loose 'http:' or 'https' at the end of the file
        if k + 5 > len(f):
            break

        # not 'http:'
        if f[k + 4] != ':':
            # ignore loose 'https:' at the end of the file
            if k + 6 > len(f):
                break

            # not 'https:'
            if f[k + 4] != 's' or f[k + 5] != ':':
                start += 5
                continue

        delimiters = ['"', '\'', '<']
        link = ''
        while k < len(f) and f[k] not in delimiters:
            link += f[k]
            k += 1
        start += len(link)
        print(link)


def main():
    sum_file('io_tests/io_ex1')

    n, success = read_number('Insert a number:')

    if not success:
        return

    write_primes('io_tests/io_ex2_o', n)

    find_words('io_tests/io_ex3')
    ex4dir = 'io_tests/io_ex4'
    ex4files = [os.path.join(ex4dir, f) for f in os.listdir(ex4dir) if os.path.isfile(os.path.join(ex4dir, f))]
    sort('io_tests/io_ex4_o', ex4files)

    fetch_links('https://docs.python.org/2/tutorial/')

main()
