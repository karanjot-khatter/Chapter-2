#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     08/02/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#program to convert celcius to farhenhiet
def main():
    print("This program is to convert celsius to fahrehiet")
    celsis = eval(input("What is the celcius temp?"))
    fahrenheit = 9/5 * celsis * 32
    print("The temp is", fahrenheit, "Degrees fahrenheit")

main()
