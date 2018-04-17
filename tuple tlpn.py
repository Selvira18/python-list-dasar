A={'Nama1':'Jane Doe', 'Nama2':'jhon smith', 'Nama3':'Bob stone', 'telp1':'+27 555 5379', 'telp2':'+27 555 6254', 'telp3':'+27 555 5689'}
print ('=========================================')
print ('  Nama              |    Telephone Number       ')
print ('==========================================')
print ('',A['Nama1'],'          |   ',A['telp1'],'  ',)
print ('',A['Nama2'],'        |   ',A['telp2'],'  ',)
print ('',A['Nama3'],'         |   ' ,A['telp3'],' ',)


A['telp1'] = '+27 555 1024'

print('Ubah No Telp Jane Doe    ')



print('===========================================')
print ('  Name        |  Telephone Number        ')
print('===========================================')
print (' ',A['Nama1'],'   | ',A['telp1'],'  ')
print (' ',A['Nama2'],' | ',A['telp2'],'  ')
print (' ',A['Nama3'],'  |',A['telp3'],'  ')


A['Nama4'] = ('Anna Cooper')
A['telp4'] = '+27 555 3237'

print (' Menambah Data Baru ')
print (' Nama        |   Telephone Number       ')
print (' ',A['Nama1'],'  |  ',A['telp1'],' ')
print (' ',A['Nama2'],'  |  ',A['telp2'],' ')
print (' ',A['Nama3'],'   |  ',A['telp3'],' ')

print (' Cetak Nomor Telp Bob stone = ',A['telp3'],' ')

print ('Cetak Semua Key =',A.keys());

print ('Cetak Semua Value =',A.values());
