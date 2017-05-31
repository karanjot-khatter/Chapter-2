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
    print("This program calculate future value of 10 year investment")
    principal = eval(input("Enter the intial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range(10):
        principal = principal * (1 + apr)
    print("The value in 10 years is:", principal)
main()