#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     21/02/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program will convert milometers to center meters")
    milometers = eval(input("Enter the amount of milometers:"))
    cm = milometers * 10
    print("Conversion from the milometers entered:", milometers, "is:", cm)
main()
