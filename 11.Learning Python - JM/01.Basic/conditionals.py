#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 100
  
  # conditional flow uses if, elif, else  
  if x < y:
    print("x is smaller than y")
  elif x == y:
    print("x has same value as y")
  else:
    print("x is larger than y")


  # conditional statements let you use "a if C else b"
  result = "x is less than y" if x < y else "x is same as or larger than y"
  print(result)
  

if __name__ == "__main__":
  main()
