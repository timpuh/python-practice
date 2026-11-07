# write a program to print even and odd list elements with their indexes 
# first in ascending order then descending 
# Use two ways: 1) with += 2 and -= 2, 2) with %
            
         #0   #1   #2   #3   #4   #5   #6   #7
items = ["a", "b", "c", "d", "e", "f", "g", "h"]

print()
print(" ___way 1: += 2 and -= 2___ ")
print()

print("even indexes (ascending):")
i = 0
while i < len(items): # do whats inside while index i is less than the list length (which is 8)
    print(f"{i}: {items[i]}")
    i = i+2
print()

print("odd indexes (ascending):")
i = 1
while i < len(items):
    print(f"{i}: {items[i]}")
    i = i+2
print()

print("even indexes (descending):")
i = len(items)-2
while i >= 0:
    print(f"{i}: {items[i]}")
    i = i-2
print()

print("odd indexes (descending):")
i = len(items)-1
while i >= 0:
    print(f"{i}: {items[i]}")
    i = i-2
print()

print()

print(" ___way 2: remainder %___ ")
print()

print("even indexes (ascending):")
for i in range(len(items)):
    if i % 2 == 0:
        print(f"{i}: {items[i]}")
print()

print("odd indexes  (ascending):")
for i in range(len(items)):
    if i % 2 != 0:
        print(f"{i}: {items[i]}")
print()

print("even indexes (descending):")
for i in range(len(items) -1, -1, -1): # len(items) - 1 -- Start -1 -- Stop -1 -- Step
    if i % 2 == 0:
        print(f"{i}: {items[i]}")
print()

print("odd indexes (descending):")
for i in range(len(items) - 1, -1, -1):
    if i % 2 != 0:
        print(f"{i}: {items[i]}")
print()