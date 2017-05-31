#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     09/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#program that transform weights in kilo to pounds'
def main():
    kilos = eval(input("Enter a weight in kilos: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is:", pounds)

main()