# Create a Timer with the Time module
import time

run = input("Start 10 seconds timer (yes) ? ")

if run.upper() == "YES":
    counter = 0
    while counter != 10:
        print("> ", counter)
        time.sleep(1)
        counter += 1
    print("> ", counter)