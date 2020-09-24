import math
import os
import random
import re
import sys

def integer1(n):
    # odd 
    if(n % 2 != 0):
        print("Weird")
    # even and 2-5
    if((n%2 == 0) and (n >= 2) and (n <= 5)):
        print("Not Weird")
    # even and 6-20
    if((n%2 == 0) and (n >= 6) and (n <= 20)):
        print("Weird")
    # even and n>20
    if((n%2 == 0) and (n > 20)):
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    integer1(n)
