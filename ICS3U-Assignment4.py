# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Assignment4.py File, Reviewing debug in python.

import math


def main():

    # input and variables
    package_mass = input("Input the mass of the package(kg): ")
    package_length = input("Input the length of the package(cm): ")
    package_width = input("Input the width of the package(cm): ")
    package_height = input("Input the height of the package(cm): ")

    # process and output
    print("")
    try:
        package_mass_asfloat = float(package_mass)
        package_length_asfloat = float(package_length)
        package_width_asfloat = float(package_width)
        package_height_asfloat = float(package_height)
        package_volume = (
            package_length_asfloat * package_width_asfloat * package_height_asfloat
        )
        if package_mass_asfloat > 27 and package_volume > 10000:
            print(
                "The package is not acceptable because it's either larger than 10,000 cm³ in volume, or heavier than 27 kg."
            )
        elif package_mass_asfloat <= 0 or package_volume <= 0:
            print("Please enter a valid number.")
        else:
            print("Your package is acceptable.")
    except ValueError:
        print("Invalid input, Please try again following the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
