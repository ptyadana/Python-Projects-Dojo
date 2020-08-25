class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "This {} is {}!".format(self.device, self.problem)
    
class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "This {} is {}!".format(self.device, self.problem)
    

    
    
def cause_error(error_type):
    if error_type == "electrical":
        raise ElectricalError("circuit breaker", "overloaded")
    elif error_type == "plumbing":
        raise PlumbingError("dish washer", "spraying water")
    else:
        raise Exception("general household problems.")
    
    
if __name__ == "__main__":
    try:
        cause_error("electrical")
        # cause_error("plumbing")
        # cause_error("plants")
    except ElectricalError as e:
        print(e)
        print("fix it by myself.")
    except PlumbingError as e:
        print(e)
        print("have to call plumber.")
    except Exception as e:
        print(e)
        print("have to call landlord.")