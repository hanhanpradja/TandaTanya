# Declare Variable
nama = input()
alamat = input()
acc = 0

# Accessing File
file = open('cek.txt', 'r+')
for line in file:
    line_split = line.split()
    if line_split[0]==nama and line_split[1]==alamat:
        acc = 1
        break
    else:
        continue
    
file.close()

# Set Condition
if acc == 1:
    print('akses diterima')
else:
    print('akses ditolak')    
