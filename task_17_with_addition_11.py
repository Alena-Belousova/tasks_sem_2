#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
a= int(input('введите число '))
list=[]
for i in range(-a,a+1):
    list.append(i)
print(list)
with open('C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\7,09\\11.txt') as f:
        lines = f.readlines()
        result=1
        for i in lines:
            result=result*list[int (i)]
            print (result)
   
   
    