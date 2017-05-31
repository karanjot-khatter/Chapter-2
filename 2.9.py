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
    print("This program converts distances measured in kilomaters to miles")
    kilo= eval(input("Enter a value in kilometers?"))
    miles = kilo * 0.62
    print ("The conversion in kilometers entered:", kilo, "to miles is:", miles)
main()