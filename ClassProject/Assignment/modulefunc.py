import os
import datetime
#Ui
def ClearScreen():
    os.system("cls" if os.name == 'nt' else "clear")

def heading(text, symbol="-"):
    print(f"{text}")
    print(symbol * len(text))

def RoomTable(Rooms, StudentPrice, PublicPrice):
    print(f"{'No':<4}{'Room Type':<14}{'Student':<10}{'Public':<10}")
    i = 0
    while i < len(Rooms):
        print(f"{i + 1:<4}{Rooms[i]:<14}{'RM' + str(StudentPrice[i]):<10}{'RM' + str(PublicPrice[i]):<10}")
        i = i + 1
    print("Prices are per night")

def DisplayOption(array, i):
    for i, choice in enumerate(array, start=i):
        print(f"{i}:{choice}")

#Logic
def GetUserChoice(min, max):
    Choice = input(f"Enter your choice {min}-{max}: ")
    if not Choice.isdigit():
         return(min - 1)  
    return int(Choice)

def Repeat(var, min, max):
    while var > max or var < min:
        print("Invalid Choice please try again")
        var = GetUserChoice(min, max)
    return var  

def UserChoice(min, max, var2=None, array=None, bool = None, primaryBool = None, secondaryBool= None, units = None):

    Choice =  GetUserChoice(min, max)

    if Choice > max or Choice < min:
        Choice = Repeat(Choice,min,max)

    ChoiceIndex = Choice

    if isinstance(array, list):
            ChoiceIndex = Choice -1
            var2 = array[Choice - 1]
            print(f"You've chosen {var2} \n")
            return var2, ChoiceIndex

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

    print(f"You've chosen {Choice} \n")
    return Choice, ChoiceIndex

def CalculatePrice(Price, Nights):
    RoomPrice = int(Price * Nights)
    return int(RoomPrice)

def Display(**kwargs):
    for key, value in kwargs.items():
        info = key.replace("_", " ")
        print(f"{info}: {value}")

#Easier to valid if make separate function than just using repeat()
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

def UserPay(Price, logo = None):
    Paid = 0
    while(Price > 0):
        print(f"Please Pay RM{Price}")
        Balance = GetAmount()
        Paid += Balance
        Price -= Balance
    print("Payment Completed")

    Change = 0
    if Price < 0:
        Change = round(-Price, 2)
        print(f"Your change is RM{Change}")
    if logo != None:
        with open(str(logo), "r", encoding="ascii") as FileLogo:
            print(FileLogo.read(), end="")
    return Paid, Change


def Receipt(Title = None, Footer = None, **kwargs):
    print("\nReceipt:")
    if Title != None:
        print(Title)
    Display(**kwargs)
    if Footer != None:
        print(Footer)

#Debug
if __name__ == '__main__':
    heading("Hello world", symbol="*")