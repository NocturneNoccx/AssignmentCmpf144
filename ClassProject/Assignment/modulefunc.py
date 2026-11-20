def GetUserChoice(min, max):
    Choice = input(f"Enter your choice {min}-{max}: ")
    if not Choice.isdigit():
         return(min - 1)
    return int(Choice)
    
def Repeat(var1, min, max):
    while var1 > max or var1 < min:
        print("Invalid Choice please try again \n")
        var1 = GetUserChoice(min, max)
    return var1

def UserChoice(min, max, var2=None, array=None, bool = None, primaryBool = None, secondaryBool= None, units = None):

    Choice =  GetUserChoice(min, max)
    ChoiceIndex = Choice

    if Choice > max or Choice < min:
        Choice = Repeat(Choice,min,max)
        var2 = array[Choice - 1]
        print(f"You've chosen {var2} \n")
        
    
    if isinstance(array, list):
            ChoiceIndex = Choice -1
            var2 = array[Choice - 1]
            print(f"You've chosen {var2} \n")
            
    
    elif isinstance(units, str):
            print(f"You've chosen {Choice} {units} \n")
            return Choice, ChoiceIndex
    
    if bool == True:
        if Choice >= min and Choice != max:
             print(primaryBool)
             Choice = primaryBool
             return Choice, ChoiceIndex
        else:
             print(secondaryBool)
             Choice = secondaryBool
             return Choice, ChoiceIndex
        
    print(f"You've chosen {Choice}")
    return Choice, ChoiceIndex
    
def CalculatePrice(Price, Nights):
    RoomPrice = int(Price * Nights)
    return int(RoomPrice)

def Display(**kwargs):
    for key, value in kwargs.items():
        info = key.replace("_", " ")
        print(f"{info}: {value} \n")

def UserPay(Price, Currency="RM", logo = None):
    while(Price > 0):
        print(f"Please Pay {Currency} {Price}")
        Balance = float(input("Please insert amount of payment:"))
        Price -= Balance

    print("Payment Completed")

    if logo != None:
        with open(str(logo), "r", encoding="ascii") as FileLogo:
            print(FileLogo.read(), end="") 
        

if __name__ == '__main__':
    print("Please continue your Payment")
    UserPay(1000, logo="logo.txt")