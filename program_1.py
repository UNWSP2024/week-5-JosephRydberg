#Kilometer Converter Joseph Rydberg 9/30/2024


def kilometer_conversion(kilometers):
    miles = kilometers * 0.6214

    return miles

if __name__ == '__main__':
    enterKilometers = float(input("Please Enter Kilometers"))
    miles = kilometer_conversion(enterKilometers)
    print(miles, "Miles")
