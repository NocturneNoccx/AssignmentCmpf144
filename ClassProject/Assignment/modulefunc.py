def GetUserChoice(min, max):
    Choice = input(f"Enter your choice {min}-{max}: ")
    if not Choice.isdigit():
         return(min - 1)  
    return int(Choice)

def Repeat(var1, min, max):
    while var1 > max or var1 < min:
        print("Invalid Choice please try again")
        var1 = GetUserChoice(min, max)
    return var1  

def UserChoice(min, max, var2=None, array=None, bool = None, primaryBool = None, secondaryBool= None, units = None):

    Choice =  GetUserChoice(min, max)

    if Choice > max or Choice < min:
        Choice = Repeat(Choice,min,max)

    ChoiceIndex = Choice

    if isinstance(array, list):
            ChoiceIndex = Choice -1
            var2 = array[Choice - 1]
            print(f"You've chosen {var2}")
            return var2, ChoiceIndex

    elif isinstance(units, str):
            print(f"You've chosen {Choice} {units}")
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
        print(f"{info}: {value}")

def IsAmount(Text):
    if len(Text) == 0:
        return False
    Dots = 0
    Digits = 0
    i = 0
    while i < len(Text):
        if Text[i] == ".":
            Dots = Dots + 1
        elif Text[i] >= "0" and Text[i] <= "9":
            Digits = Digits + 1
        else:
            return False
        i = i + 1
    if Dots > 1 or Digits == 0:
        return False
    return True

def GetAmount():
    Amount = input("Please insert amount of payment:")
    while not IsAmount(Amount):
        print("Invalid amount please try again")
        Amount = input("Please insert amount of payment:")
    return float(Amount)

def UserPay(Price, UserBalance= 0, logo = None):
    while(Price > 0):
        print(f"Please Pay {Price}")
        Balance = GetAmount()
        Price -= Balance
    print("Payment Completed")

    if Price < 0:
        print(f"Your change is RM{round(-Price, 2)}")
    if logo != None:
        with open(str(logo), "r", encoding="ascii") as FileLogo:
            print(FileLogo.read(), end="")

#Debug
if __name__ == '__main__':
    print("Please continue your Payment")
    UserPay(1000, logo="logo.txt")
