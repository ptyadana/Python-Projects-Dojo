# Question: 
# Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is:
# To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively, and you should get the expected output.

# Expected output:
# 0.5

# Answer:
def get_acceleration(v1,v2,t1,t2):
    return ((v2-v1)/(t2-t1))

if __name__ == "__main__":
    result = get_acceleration(0, 10, 0, 20)
    print(result)

# Explanation (Python 3): 
# The first three lines are where we create the function. A function definition is like a like a blueprint. Then in the last line we're printing out the function output. The output is whatever is returned by the return  statement.