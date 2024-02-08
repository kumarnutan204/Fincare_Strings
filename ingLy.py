val = input("Enter and english word")
def ingOrLy(val):
    
    if(len(val)>3):
        if(val[-3:] == "ing"):
            val=val+("ly")
        else:
            val=val+("ing")
    
    print(val)

ingOrLy(val)
