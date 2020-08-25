from contextlib import contextmanager

HEADER = "this is pre-defined header \n"
FOOTER = "\nthis is pre-defined footer \n"

@contextmanager
def new_log_file(name):
    try:
        logname = name
        f = open(logname, "w")
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print("log file created.")
        f.close()
        
        
if __name__ == "__main__":
    with new_log_file("text_log") as file:
        file.write("This is body.")
    
        