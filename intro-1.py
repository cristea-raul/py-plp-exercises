import sys

print(''.join([(arg[::-1]) + ' ' for arg in sys.argv[:0:-1]])[:-1])
