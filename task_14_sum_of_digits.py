   # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#    Пример:
#- 6782 -> 23
#- 0,56 -> 11
numb= (input('введите число '))
numb = numb.replace('.', '')
numb=int(numb)
summ=0
while numb>0:
        digit=numb%10      
        summ=summ+digit
        numb=numb-digit
        numb=int (numb/10)      
print(summ)  
      



