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
#This program calculates total amount of investment in chosen year

def main():

    principal = eval(input('Please enter your yearly investment: '))
    apr = eval(input('Please enter interest rate: '))
    years = eval(input('How many years to calculate: '))

    account = principal

    for i in range(years):

        total= account*(1+apr)
        print('Year:',i+1,'=',total)
        account = total+principal

main()
