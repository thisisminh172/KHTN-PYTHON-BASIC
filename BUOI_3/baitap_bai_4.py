# bai 1
# def getAbs(num):
#     return num if num > 0 else num * -1

# num = int(input('Nhap 1 so: '))
# print('so tuyet doi cua |{:,.0f}|la {:,.0f}'.format(num, getAbs(num)))

# bai 2
# listInput = input('nhap 4 so: ')
# a, b, c, d = eval(listInput)
list = [13, 6, 10, -8]
tempList = list
print(id(list), id(tempList))
so_min = 0
so_max = 0
for i in range(len(list) -1):
    if list[i] > list[i+1]:
        so_max = list[i]
        list[i] = list[i+1]
        list[i+1] = so_max
for j in range(len(list) -1):
    if list[j] < list[j+1]:
        so_min = list[j]
        list[j] = list[j+1]
        list[j+1] = so_min
print('min:', so_min)
print('max:', so_max)

