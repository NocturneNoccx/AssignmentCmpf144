#This is a rough outline of the code and the functions
#1/11/26
#Uploaded to git on 8/11/26
from modulefunc import *

RoomChoice = ["Single Room","Double Room","Deluxe Room","Suite Room"]
StudentPrice = [50,75,100,150]
PublicPrice = [80,120,150,200]
UserPrice = 0

#Main
if __name__ == '__main__':
    while True:
        heading("Welcome to Royal Park Hotel Room Rental System", symbol="-")
        UserName = input("Please Enter your Name:")
        heading("\n Types of Room")
        RoomTable(RoomChoice, StudentPrice, PublicPrice)
        UserRoom, UserIndex = UserChoice(1, 4,array=RoomChoice)
        heading("\n Are you a Student or Public\n 1.Student\n 2.Public\n")
        User_Status = UserChoice(1,2, bool=True, primaryBool="Student", secondaryBool="Public")

        if User_Status[0] == "Public":
            UserPrice = PublicPrice[UserIndex]
        else:
            UserPrice = StudentPrice[UserIndex]

        Nights_Stayed = UserChoice(1, 365, units="Nights")
        RoomPrice = CalculatePrice(UserPrice, Nights_Stayed[0])
        Display(Room_type = UserRoom, Status = User_Status[0], Duration = (str(Nights_Stayed[0]) + " Nights"), RoomPrice = ("RM"+str(RoomPrice)))
        Paid, Change = UserPay(RoomPrice, logo="logo.txt")
        Receipt(Title = "Royal Park Hotel", Footer = "Thank you for staying with us \n", Name = UserName, Room_type = UserRoom, Status = User_Status[0], Duration = (str(Nights_Stayed[0]) + " Nights"), Total_Price = ("RM"+str(RoomPrice)), Paid = ("RM"+str(Paid)), Change = ("RM"+str(Change)))
        print("Do you want to continue?\n 0.Yes, 1.No")
        LoopContinue = UserChoice(0,1, bool=True, primaryBool="Yes", secondaryBool="No")

        if LoopContinue[0] != "Yes":
            break 
    print("Thank you for using our service")

