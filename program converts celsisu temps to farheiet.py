#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     08/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#program to convert celcius temps to farenheit
def main():
    celsius = eval(input("What is the celcius temp?"))
    farhenhiet = 9/5 * celsius +32
    print("The temp is", farhenhiet, "degrees farenheit")

main()