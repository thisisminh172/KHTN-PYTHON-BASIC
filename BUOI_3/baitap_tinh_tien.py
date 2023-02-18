# so_luong = int(input('Nhap so luong: '))
# don_gia = int(input('Nhap don gia: '))
so_luong = 6
don_gia = 50000
total = so_luong * don_gia
discount = 0

if so_luong >= 5:
    discount = total * 0.1
total -= discount

print('Tam tinh: {:,}'.format(so_luong * don_gia))
print('Giam gia: {:,.0f}'.format(discount))
print('Thanh tien: {:,.0f}'.format(total))
