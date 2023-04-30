
nama = input()
alamat = input()
acc = 0

file = open('cek.txt', 'r+')
lines = file.readlines() 
if  lines == []:
    acc = 1
else:
    for line in lines: 
        line_split = line.split()
        if line_split[0]==nama:
            acc = 0
            break
        else:
            acc = 1
file.close()

file = open('cek.txt', 'a')
if acc == 0:
    print('username already taken')
else:
    print('Berhasil mendaftar!')
    file.write(f'{nama} {alamat} \n')

file.close()