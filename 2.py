# Задача 1

# x = input("Введите трехзначное число - ")


# result = int(x[0]) + int(x[1]) + int(x[2])
# print (result)


# задача 2

# j = int(input("Введите число журавликов - "))
# k = j // 3 *2
# s = p =j // 3 // 2

# print (k, s, p)


# Задача 3

# number = input("Введите счастливое число - ")

# number1 = int(number[0]) + int (number[1]) + int (number[2])
# number2 = int(number[3]) + int (number[4]) + int (number[5])
# if number1 == number2:
#     print ("Lucky number")
# else:
#     print ("Unlucky, try again")


# Задача 4

n = int(input ("Веедите длину - "))
m = int(input ("Веедите ширину - "))
k = int(input ("Веедите количество плиток - "))
if k <= n * m:
    if k % n == 0 or k % m == 0:
        print ("Разделить можно")
else:
    print ("Разделить нельзя")
