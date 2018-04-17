

nm = []
n = []
tgs = []
uts = []
uas = []
stop = False
no = 0
while (not stop) :
    nama      = input("\tMasukan Nama :")
    nm.append(nama)
    nim       = int(input("\tNIM          : "))
    n.append(nim)
    Tugas     = int(input("\tTUGAS        : "))
    tgs.append(Tugas)
    Nilai_UTS = int(input("\tUTS          : "))
    uts.append(Nilai_UTS)
    Nilai_UAS = int(input("\tUAS          : "))
    uas.append(Nilai_UAS)
    data = input("Tambah Data (Y/T)?")
    if (data == "T"):
        stop = True
    akhir=(Tugas+Nilai_UTS+Nilai_UAS)/3
    no +=1
print("====================================================================== ")
print("  No.| Nama| Nim| Tugas| Nilai UTS| Nilai UAS| Akhir|")
print("=======================================================================")
print("" ,no," | ",nama,"| ",nim, "| ",Tugas, "| ",Nilai_UTS, "| ",Nilai_UAS,
      "| " ,akhir)
print("=========================================================================")


