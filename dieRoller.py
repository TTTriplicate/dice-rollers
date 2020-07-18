#!/usr/bin/python3

import re
import sys
import random
import random

if len(sys.argv) < 2:
    print("Roller require argument: d[die_size]+[modifier]")

for r in sys.argv[1:]:
    parts = re.match(r'^([1-9])d([0-9]*)\+([0-9]*)', r)
#    print("number of dice:", parts.group(1))
#    print("Die size:", parts.group(2))
#    print("Bonus:", parts.group(3))
#    print("Roll should be between ", 1+int(parts.group(3)), " and ", int(parts.group(2))+int(parts.group(3)))
    total = 0
    for i in range(int(parts.group(1))):
        total += (random.randint(1, int(parts.group(2))))
    print(total)
    print(total + int(parts.group(3)))
