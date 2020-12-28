
# Slices

alpha = "abdefg"

print(alpha[1:3]) #bd
print(alpha[3:]) #efg
print(alpha[:3]) # abd
print(alpha[3:-2]) #e
print(alpha[-3:4]) #e
print(alpha[::2]) # adf
print(alpha[1::2]) #beg
print(alpha[-1:0:-1]) #gfedb
print(alpha[-2: 0]) #empty

# Demonstrating the split() method:
print("phi       chi\npsi")
print("phi       chi\npsi".split())

