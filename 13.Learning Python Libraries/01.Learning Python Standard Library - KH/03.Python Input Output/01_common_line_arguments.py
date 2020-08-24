# Command Line Arguments
import sys

# Print Arguments
print("number of arguments: ", len(sys.argv), " arguments.")
print("Arguments: ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0]) # remove the first argument which is path of program itself

print("Arguments: ", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        sum += int(arg)
    except Exception:
        print("bad input")
    
print("Sum: ", sum)
    