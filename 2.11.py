#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     11/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("Interactive python calculator program")
    for i in range(100):
        expression = eval(input("Please type a mathematical expression:"))
        print("The result is", expression)
        print()
main()
