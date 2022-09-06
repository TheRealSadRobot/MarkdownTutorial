def titlePrint(text):
    print("[]###"+"#"*len(text)+"###[]\n #   "+ text + "   #\n[]###"+"#"*len(text)+"###[]")

def inputInt(message):
    try:
        returned = int(input(message+"\n-->"))
        return returned
    except:
        print("Invalid Entry")
        inputInt(message)
        
def inputIntInRange(message, minimum, maximum):
    try:
        returned = int(input(message+"\n-->"))
        if returned <= maximum and returned >= minimum:
            return returned
        else:
            print("Invalid Entry")
            inputIntInRange(message, minimum, maximum)
    except:
        print("Invalid Entry")
        inputIntInRange(message, minimum, maximum)
        
def inputFloat(message):
    try:
        returned = float(input(message+"\n-->"))
        return returned
    except:
        print("Invalid Entry")
        inputFloat(message)
        
def inputFloatInRange(message, minimum, maximum):
    try:
        returned = float(input(message+"\n-->"))
        if returned <= maximum and returned >= minimum:
            return returned
        else:
            print("Invalid Entry")
            inputFloatInRange(message, minimum, maximum)
    except:
        print("Invalid Entry")
        inputFloatInRange(message, minimum, maximum)

def AddToList(listToAddTo, thingtoadd):
    try:
        listToAddTo.append(float(thingtoadd))
    except:
            print("Invalid Entry")
            AddToList(listToAddTo, thingtoadd)
