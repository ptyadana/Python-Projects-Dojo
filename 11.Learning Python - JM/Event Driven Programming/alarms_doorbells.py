import tkinter
import time

# handler alram event
def alarm():
    print("Calling the pizza company.")

# handler for rining doorbell
def doorbell():
    print("Ding Dong!")
    time.sleep(5) # I was watching TV, so a bit slow to response to doorbell
    print("Opening the door.")

# handler for phone rings
def phonecall():
    print("Answering the phone.") 
    
# create buttons and assign callbacks
root = tkinter.Tk()
tkinter.Button(root, text="Ring Doorbell", command = doorbell).pack()
tkinter.Button(root, text="Call Phone", command = phonecall).pack()

# set timer for 4 second
root.after(4000, alarm)

# start the event loop
root.mainloop()