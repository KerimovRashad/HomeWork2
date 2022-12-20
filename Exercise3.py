# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
#  максимум использование библиотеки Random для и получения случайного int

from random import sample
 
if __name__ == '__main__':
 
    nums = range(10)
 
    l = sample(nums, len(nums))
    print(l)
