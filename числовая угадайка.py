import random
print("Добро пожаловать в числовую угадайку")
g = int(input("Введите правую границу рандомнго числа"))
def is_valid(num):
    if num.isdigit():
        num = int(num)
        if num <= g and num >=1:
            return True
        else:
            return False
    else:
        return False

flag = False
flag1 = "д"
count = 1
rand_num = random.randint(1, g)
while flag == False:
        num = input(f"Введите число от 1 до {g}")
        if is_valid(num) == True:
            num = int(num)
            if num < rand_num:
                print("Загадонное число больше, попробуйте еще разок")
                count = count + 1
            elif num > rand_num:
                print("Загадонное число меньше, попробуйте еще разок")
                count = count + 1
            else:
                num = input(f"Вы угадали за {count} попытки, поздравляем!, хотите заного сыграть ? д/н")
                if num == "н":
                    print("Спасибо за игру , приходите еще !")
                    flag = True
                else:
                    rand_num = random.randint(1, g)
                    count = 1

        else:
            print(f"А может быть все-таки введем целое число от 1 до {g}?")