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
#program calculates future value in 10 years time
def main():
    print("program calculates future alue in 10 years time")
    principal = eval(input("Enter amount of value being invested:"))
    apr =eval(input("enter the annual interest rate:"))
    for i in range(10):
        principal = principal * (1+apr) # 1 + every year plus new principal
        print("Value in 10 years is:",principal)

main()