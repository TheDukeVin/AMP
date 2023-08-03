def umbrella_check():
    print("Checking the rain forecast...")
    raining_today = False
    if raining_today:
        print("Better bring an umbrella!")
    print("Have a lovely day!")

def get_temperature():
    temp = float(input("Enter the temperature in degrees Fahrenheit: "))
    return temp

def temperature_check(temperature):
    print("Checking temperature...")
    if temperature < 32:
        print("Brrr, it's freezing out!")
    elif temperature < 90:
        print("Ah, a comfortable temperature")
    else:
        print("Yikes! It's hot out")
    print("Make sure to dress appropriately for the weather!")


if __name__ == "__main__":
    umbrella_check()
    temperature_today = get_temperature()
    temperature_check(temperature_today)