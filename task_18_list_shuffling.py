# Реализуйте алгоритм перемешивания списка.
import random
numb= int(input('введите число '))
list=[]
for i in range(-numb,numb+1):
    list.append(i)
print(list) 
random.shuffle(list)
print (list)