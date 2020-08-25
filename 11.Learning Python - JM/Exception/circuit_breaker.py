class CircuitBreaker():
    def __init__(self):
        self.capacity = 20
        self.load = 0
        
    def connect(self, amp):
        if self.load + amp > self.capacity:
            raise Exception("connect will cause positive overload.")
        elif self.load + amp < 0:
            raise Exception("connect will cause negative load.")
        else:
            self.load += amp
            
if __name__ == "__main__":
    cb = CircuitBreaker()
    print(cb.load)
    
    # cb.connect(30)
    # cb.connect(-10)
    
    cb.connect(10)
    cb.connect(5)
    cb.connect(5)
    print(cb.load)