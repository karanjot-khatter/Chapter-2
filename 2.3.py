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
#Converts celcius to farenhiet 5 times
def main():
    print("This program converts celsisus to fahrenheit, 5 times!")
    celcius = eval(input("What is celcius temp?"))
    for i in range(5):
        celcius = (9/5 * celcius + 32)
        print ( "The temp is: ", celcius, "degrees fahrenhiet" )

main()
