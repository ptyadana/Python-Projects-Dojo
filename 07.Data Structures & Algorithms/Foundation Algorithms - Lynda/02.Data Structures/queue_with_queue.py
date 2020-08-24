import queue

# create new queue object
q = queue.Queue() # queue with no limit
q_mini_fridge = queue.Queue(5) # queue with Limit: only hold 5 items

# queue empty or not?
print(q.empty())

# adding items to queue
q.put("bag1")
q.put("bag2")
q.put("bag3")


# geting items from queue (FIFO)
# until queue is empty
while not q.empty():
    print(q.get())
    
# putting items until it is full
# into the mini_fridge
count = 1
while not q_mini_fridge.full():
    q_mini_fridge.put(f"Milk Bottle {count}")
    count += 1
    
# getting items again from q2
while not q_mini_fridge.empty():
    print(q_mini_fridge.get())

