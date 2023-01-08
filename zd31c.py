x = input("Введите цифру: ")
str_x = str(x)
lst_str = list(str_x)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)


