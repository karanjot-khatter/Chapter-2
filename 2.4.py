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
#table which prints farhenheit temps every 10odegrees
def main():
     print('Celsius & Farenheit Chart')
     celsius = 0

     for i in range(10):
        celsius = celsius + 10
        fahrenheit = 9/5 * celsius + 32
        print('|',celsius, 'celsius | ', fahrenheit,'fahrenheit|')


main()
