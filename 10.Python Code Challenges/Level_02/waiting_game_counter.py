import random
import time

def waiting_game_counter():
    target = random.randint(2,6)
    print(f"Your target time is {target} seconds.")
    print(f"--- How to play - Press Enter to Begin and press Enter again after {target} seconds. --- \n")

    input("--- Press Enter to Begin ---")
    start_time = time.perf_counter()
    
    input("--- Press Enter again to End ---")
    elapsed = time.perf_counter() - start_time
    
    print("Elapsed Time: {0:.3f} seconds".format(elapsed))
    
    if elapsed == target:
        print("Great Job! Right on time.")
    elif elapsed > target:
        print("{0:.3f} seconds too slow".format(elapsed - target))
    else:
        print("{0:.3f} seconds too fast".format(target - elapsed))

if __name__ == "__main__":
    waiting_game_counter()