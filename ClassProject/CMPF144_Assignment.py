def GetUserChoice(minValue, maxValue):
    while True:
        try:
            UserValue = int(input(f"Enter your choice {minValue}-{maxValue}: "))
        except ValueError:
            print("Please enter a number, not text.")
            continue
        if minValue <= UserValue and UserValue <= maxValue:
            return UserValue
        print(f"Please enter a number between {minValue} and {maxValue}.")


GetUserChoice(1,2)