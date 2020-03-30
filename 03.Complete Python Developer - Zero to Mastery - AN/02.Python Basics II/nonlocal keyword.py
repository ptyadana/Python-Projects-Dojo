def outer():
    x = "local"

    def inner():
        #by using nonlocal keyword, x variable is referenced from parent one
        nonlocal x

        #now the parent variable x got overwritten
        x = "nonlocal"
        
        print(f"inner: {x}")
    
    inner()
    print(f"outer: {x}")


outer()