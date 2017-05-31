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
#program to compute the value of an investmenet - using a compounded period
#10 years into the future
def main():
    print("This program calculate the future value- using a compounded peiod of 10 years")
    principal = eval(input("Enter the intial principal:"))
    apr = eval(input("Enter the annual interest rate:"))
    years = eval(input("Enter the amount of years: "))
    periods = eval(input("Number of times interest is compounded each year"))
    for i in range(years * periods):
        principal = principal * (1+apr/periods)
    print("In period:",i+1, "you get:", principal)

# i = 8, + 1 to get 9th set
main()
