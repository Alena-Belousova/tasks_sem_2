     
    #Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и 
    # выведите на экран их сумму.
#    Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


numb= int(input('введите число '))
list={}
summ=0
for i in range(1,numb+1):
    formula=(1+1/i)**i
    list[i] =formula
    summ=summ+formula
print (list)  
print (summ) 
