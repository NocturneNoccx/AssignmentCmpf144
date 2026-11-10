#This is a rough outline of the code and the functions
# 1/11/26
#Uploaded to git on 8/11/26
RoomChoice = ["Single Room","Double Room","Deluxe Room","Suite Room"]

def GetUserChoice(min, max):
    return int(input(f"Enter your choice {min}-{max}: "))

def Repeat(var1, min, max):
    while var1 > max or var1 < min:
        print("Invalid Choice please try again")
        var1 = GetUserChoice(min, max)
        return var1
    return var1

def UserChoice(min, max, var2=None, array=None, bool = None, primaryBool = None, secondaryBool= None, units = None):

    Choice1 =  GetUserChoice(min, max)
    
    if Choice1 > max or Choice1 < min:
        Choice1 = Repeat(Choice1,min,max)
        var2 = array[Choice1 - 1]
        print(f"You've chosen {var2}")
        return var2
    elif isinstance(array, list):
            var2 = array[Choice1 - 1]
            print(f"You've chosen {var2}")
            return var2
    elif isinstance(units, str):
            print(f"You've chosen {Choice1} {units}")
            return Choice1
    elif bool == True:
        if Choice1 > min:
             print(primaryBool)
             Choice1 = primaryBool
             return Choice1
        else:
             print(secondaryBool)
             Choice1 = secondaryBool
             return Choice1
    else:
         print(f"You've chosen {Choice1}")
         return Choice1
    
def Display(**kwargs):
    for key, value in kwargs.items():
        info = key.replace("_", " ")
        print(f"{info}: {value}")
  
#Main
if __name__ == '__main__':
    print("Welcome to Royal Park Hotel Room Rental System")
    print("Types of Room\n 1.Single Room \n 2.Double Room \n 3.Deluxe Room \n 4.Suite Room \n")
    UserRoom = UserChoice(1, 4,array=RoomChoice)
    print(UserRoom)
    print("Are you a Student or Public\n 1.Student\n 2.Public\n")
    User_Status = UserChoice(1,2, bool=True, primaryBool="Student", secondaryBool="Public")
    Nights_Stayed = UserChoice(-365, 365, units="Nights")
    Display(Room_type = UserRoom, Status = User_Status, Duration = (str(Nights_Stayed) + " Nights"))

