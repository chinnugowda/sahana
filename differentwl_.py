i = 10
# While greater than zero.
while i >= 0:
    print(i)
    # End loop if evenly divisible by seven.
    if i % 7 == 0:
        break
    i -= 1

import random

# A while-true loop.
while True:
    n = random.randint(0, 100)
    print(n)
    # Break on even random number.
    if n % 2 == 0:
        break
list = ["cat", "dog", "panther", "parakeet"]

i = 0
while i < len(list):
    element = list[i]
    i += 1

    # Test for this element.
    if element == "panther":
        continue

    # Display element.
    print("Pet", element)
