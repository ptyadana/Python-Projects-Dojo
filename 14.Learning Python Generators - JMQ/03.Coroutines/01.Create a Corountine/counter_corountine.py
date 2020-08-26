# counting the number of subsequent strings whether they are part of ORIGINAL string

def counter(string):
    count = 0
    
    try:
        while True:
            item = yield    # when coroutinue see this yield, it pauses the flow start capturing the sent values. At this point: string = "California" and item will be passed values.
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print("It's a match: ", item)
                else:
                    print("No match")
            else:
                print ("Not a string")
                
    except GeneratorExit:
        print("Number of matches: ", count)
        
        
        
if __name__ == "__main__":
    c = counter("California")
    
    # this needs to be done to prime the coroutine by calling __next__() or by sending None value to it.
    # sometimes, we tends to forget it. so better way to avoid this is create and use decorator which call this line automatically
    c.__next__() 
    
    c.send("Cali")
    c.send("nia")
    
    c.send("Hawaii")
    c.send(1234)
    
    c.close()