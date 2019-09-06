"""

Purpose:in this program we prints windchill according to user input
author : sachin shrikant jadhav
version:3.7
since  : 22-08-2019

"""


def Wind_Chill():
    while True:
        try:
            temperature = int(input("enter temp"))
            wind_speed = int(input("enter wind_speed"))

            if 0 < temperature < 50 and 3 < wind_speed < 121:
                windchill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * wind_speed ** 0.16  #
                # wind_chill formula
                print("windchill= ", windchill)
                break
            else:
                print("please enter temp value between (1-50) or wind_speed (4-120)")
        except ValueError:
            print("please enter valid input")


if __name__ == '__main__':
    Wind_Chill()
