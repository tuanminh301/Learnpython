# Import module random
import random
# Tao danh sach lua chon hop le
choice_lst = ['keo','bua','la']
# Tao bien tinh diem
score = 0
# Tao vong lap
while True:
    player = input('Chon keo, bua hoac la(hoac thoat de roi khoi tro choi): ')
    if player == 'thoat':
        print('Cam on ban da tham gia tro choi, so diem cua ban la: ', score)
        break 
    elif player not in choice_lst:
        print('Lua chon khong hop le, vui long nhap lai: ')
        continue
    com = random.choice(choice_lst)
    print('May tinh chon: ', com)
    if player == com:
        print('Hoa nhau')
    elif (player == 'keo' and com == 'la') or (player == 'bua' and com == 'keo') or (player == 'la' and com == 'bua'):
        print('Ban thang')
        score +=1
    else: 
        print('Ban thua')
        score -=1