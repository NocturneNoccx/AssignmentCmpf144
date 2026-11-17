#This is a rough outline of the code and the functions
#1/11/26
#Uploaded to git on 8/11/26
RoomChoice = ["Single Room","Double Room","Deluxe Room","Suite Room"]
StudentPrice = [50,75,100,150]
PublicPrice = [80,120,150,200]
UserPrice = 0

def GetUserChoice(min, max):
    Choice = input(f"Enter your choice {min}-{max}: ")
    if not Choice.isdigit():
         return(0)
    return int(Choice)
    
def Repeat(var1, min, max):
    while var1 > max or var1 < min:
        print("Invalid Choice please try again")
        var1 = GetUserChoice(min, max)
        return var1

#Flag Based Function System
def UserChoice(min, max, var2=None, array=None, bool = None, primaryBool = None, secondaryBool= None, units = None):

    Choice =  GetUserChoice(min, max)
    ChoiceIndex = Choice

    if Choice > max or Choice < min:
        Choice = Repeat(Choice,min,max)
        var2 = array[Choice - 1]
        print(f"You've chosen {var2}")
        return var2, ChoiceIndex
    
    elif isinstance(array, list):
            ChoiceIndex = Choice -1
            var2 = array[Choice - 1]
            print(f"You've chosen {var2}")
            return var2, ChoiceIndex
    elif isinstance(units, str):
            print(f"You've chosen {Choice} {units}")
            return Choice, ChoiceIndex
    elif bool == True:
        if Choice > min:
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

def UserPay(Price, UserBalance= 0):
    while(True):
        print(f"Please Pay {Price}")
        Current   
        pass

#Main
if __name__ == '__main__':
    print("Welcome to Royal Park Hotel Room Rental System")
    print("Types of Room\n 1.Single Room \n 2.Double Room \n 3.Deluxe Room \n 4.Suite Room \n")
    UserRoom, UserIndex = UserChoice(1, 4,array=RoomChoice)
    print(UserRoom)
    print("Are you a Student or Public\n 1.Student\n 2.Public\n")
    User_Status = UserChoice(1,2, bool=True, primaryBool="Student", secondaryBool="Public")

    if User_Status == "Public":
         UserPrice = PublicPrice[UserIndex]
    else:
         UserPrice = StudentPrice[UserIndex]

    Nights_Stayed = UserChoice(-365, 365, units="Nights")
    RoomPrice = CalculatePrice(UserPrice, Nights_Stayed[0])
    Display(Room_type = UserRoom, Status = User_Status[0], Duration = (str(Nights_Stayed[0]) + " Nights"), RoomPrice = ("RM"+str(RoomPrice)))
    
