#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while x < 5:
    print(x)
    x += 1

  # define a for loop
  for x in range(5, 10):
    print(x)

  # use a for loop over a collection
  my_list = [100, 200, 300]
  for item in my_list:
    print(item)

 
  # use the break and continue statements
  for x in range(5, 10):
    if x == 7:
      break
    else:
      print(x)

  # for x in range(10):
    if x % 2 != 0:
      continue
    else:
      print(x)


  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  for idx, item in enumerate(days):
    print(idx, item)


if __name__ == "__main__":
  main()
