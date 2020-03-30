import configparser

def main():

    print("***** Welcome to Your Weights on differnt Planets ***** ")
    
    user_answer = 'Y'

    try:
        while user_answer == "Y":
            weight = input("\nPlease enter your weight(lbs) on EARTH : ")
            if weight != "":
                weight_converter(int(weight))
                user_answer = input("\nWould you like to try again (Y/N)? ")

    except Exception as err:
        print(f"\nYou have provided an invalid input. The program will quit now !")


def weight_converter(weight):
    """convert earth weight to 9 different planets weights""" 
    config = configparser.RawConfigParser()
    config.read("planets.properties")

    print(f"Your weight on MERCURY is {round(float(config.get('WeightsSection','MERCURY')) * weight,2)}")
    print(f"Your weight on VENUS is {round(float(config.get('WeightsSection','VENUS')) * weight,2)}")
    print(f"Your weight on MOON is {round(float(config.get('WeightsSection','MOON')) * weight,2)}")
    print(f"Your weight on MARS is {round(float(config.get('WeightsSection','MARS')) * weight,2)}")
    print(f"Your weight on JUPITER is {round(float(config.get('WeightsSection','JUPITER')) * weight,2)}")
    print(f"Your weight on SATURN is {round(float(config.get('WeightsSection','SATURN')) * weight,2)}")
    print(f"Your weight on URANUS is {round(float(config.get('WeightsSection','URANUS')) * weight,2)}")
    print(f"Your weight on NEPTUNE is {round(float(config.get('WeightsSection','NEPTUNE')) * weight,2)}")
    print(f"Your weight on PLUTO is {round(float(config.get('WeightsSection','PLUTO')) * weight,2)}")


if __name__ == "__main__":
    main()