#!/usr/bin/python3

import random

random.seed()
rolls = []
stats = []
labels = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
for i in range(24):
    rolls.append(random.randint(1, 6))
for i in range(4, 25, 4):
    stats.append(sum(rolls[i-4:i]) - min(rolls[i-4:i]))
for i in range(len(stats)):
    print(labels[i], stats[i])
