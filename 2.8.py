#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     16/02/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#convedrts temp from farenhiet to celsius
def main():
    print("This program converts celcius into farheniet")
    celcius = eval(input("What is the temperture, in celcius"))
    farenheit = 9/4 * celcius + 32
    print("The tempeture in farheniet is:", farenheit)
main()
