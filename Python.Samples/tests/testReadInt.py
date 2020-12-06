from sys import path
path.append("..\\Samples")
import Samples.myFunctions as my

val = my.readint("Enter a number from -10 to 10: ", -10, +10)
if -10> val > 10:
    print("Error: the value is not within the valid range (-10, 10)")
else:
    print("The number is:", val)
