#import module
#print(module.counter)

#from module import suml, prodl

#zeroes = [0 for i in range(5)]
#ones = [1 for i in range(5)]
#print(suml(zeroes))
#print(prodl(ones))

from sys import path
path.append('..\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))