RoomChoice = ["Single Room","Double Room","Deluxe Room","Suite Room"]
UserChose = 0
UserRoom = 0
User_Status = 0
Student = 0
Nights = 0
Nights_Stayed = 0

def GetUserChoice(min, max):
    return int(input(f"Enter your choice {min}-{max}: "))

def Repeat(var1, min, max):
     while var1 > max or var1 < min:
        print("Invalid Choice please try again")
        var1 = GetUserChoice(min, max)  

def UserChoice(Choice1, min, max, var2=0, array=0, bool = False, primaryBool = None, secondaryBool= None, units = 0):

    Choice1 =  GetUserChoice(min + 1, max)
     
    if Choice1 > max or Choice1 < min:
        Repeat(Choice1,min,max)
    #Detect if it's an array
    elif isinstance(array, list):
            var2 = array[Choice1 - 1]
            print(f"You've chosen {var2}")
            return var2
    #Append Units
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
print("Welcome to Royal Park Hotel Room Rental System")
print("Types of Room\n 1.Single Room \n 2.Double Room \n 3.Deluxe Room \n 4.Suite Room \n")
UserRoom = UserChoice(UserChose, 0, 4,array=RoomChoice)
print(UserRoom)
print("Are you a Student or Public\n 1.Student\n 2.Public\n")
User_Status = UserChoice(Student,1,2, bool=True, primaryBool="Student", secondaryBool="Public")
Nights_Stayed = UserChoice(Nights, -365, 365, units="Nights")
Display(Room_type = UserRoom, Status = User_Status, Duration = (str(Nights_Stayed) + " Nights"))

