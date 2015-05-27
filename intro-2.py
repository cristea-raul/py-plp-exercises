import sys

if len(sys.argv) != 2:
    print('Requires 1 argument, no more, no less.')
    exit()

no = 0
try:
    no = int(sys.argv[1])
except Exception:
    print('Must be an integer.')
    exit()

rev = 0
initial_no = no
while no > 0:
    digit = no % 10
    no //= 10

    rev = rev * 10 + digit

print('Number ' + str(initial_no) + ' is' + (' not' if initial_no != rev else '') + ' a palindrome.')