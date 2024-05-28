from random import randint
import sys

# Generate a random number between 0 and the value passed as first parameter
max = int(sys.argv[1]) if len(sys.argv) > 1 else 100
min = int(sys.argv[2]) if len(sys.argv) > 2 else 0
print('Your rolled {}'.format(randint(min, max)))
