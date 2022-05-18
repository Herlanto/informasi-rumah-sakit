#Nama   : Herlanto Exaudi Sitompul 
#nim    : 14S19009
#prodi  : Electrical Enginering
#matkul : Programing 2/Python
#kampus : Institut Teknologi Del
import datetime

class RumahSakit:
    def __init__(self,name,add,numICU,numHCU,numICCU,numNICU,numPICU):
        self.name=name
        self.add=add
        self.numICU=numICU
        self.numHCU=numHCU
        self.numICCU=numICCU
        self.numNICU=numICU
        self.numPICU=numPICU
        self.pasegger=list()
        self.noicu=0
        self.nohcu=0
        self.nonicu=0
        self.nopicu=0
        self.noiccu=0
        
    def getNo_id(self,room):
        if room==1:
            self.noicu+=1
            return '001-'+'0'*(3-len(str(self.noicu)))+str(self.noicu)
        elif room==2:
            self.nohcu+=1
            return '002-'+'0'*(3-len(str(self.nohcu)))+str(self.nohcu)
        elif room==3:
            self.nonicu+=1
            return '003-'+'0'*(3-len(str(self.nonicu)))+str(self.nonicu)
        elif room==4:
            self.nopicu+=1
            return '004-'+'0'*(3-len(str(self.nopicu)))+str(self.nopicu)
        elif room==5:
            self.noiccu+=1
            return '005-'+'0'*(3-len(str(self.noiccu)))+str(self.noiccu)
    def appendPasegger(self,pasegger):
        self.pasegger.append(pasegger)
    
    def checkPasien(self,no_id):
        for _ in self.pasegger:
            if _.no_id==no_id:
                return _
        return False

    
    def getDataPasien(self,no_id):
        data=self.checkPasien(no_id)
        if data==False:
            return False
        else:
            print('Data Anda')
            print('Name :', data.name)
            print('Genre : ',data.genre)
            print('Age : ',data.age)
            print('No hp : ',data.nohp)
            print('Address : ',data.address)
            print('No Id : ',data.no_id)
            print('Tanggal Masuk : ',data.tgl_masuk)
            print('Tanggal Keluar : ',data.tgl_masuk)
            print('Penyakita yang di derita : ',data.penyakit)
    def getposisiAntrian(self,no_id):
        for _ in range(len(self.pasegger)):
            if self.pasegger[_].no_id ==no_id:
                return _
        return False
    def ubah_harga(self,price,no_urut):
        self.pasegger[no_urut].biayaobat(price)
            
class people:
    def __init__(self,Name,genre,age,address,nohp):
        self.name=Name
        self.genre=genre
        self.age=age
        self.address=address
        self.nohp=nohp
        
class Passegger(people):
    def __init__(self,name,genre,age,address,nohp,no_id,penyakit,tgl_masuk,tgl_keluar):
        super().__init__(name,genre,age,address,nohp)
        self.no_id=no_id
        self.penyakit=penyakit
        self.tgl_masuk=tgl_masuk
        self.tgl_keluar=tgl_keluar
        #self.price=
        self.price=self.getpriceRoom()
    
    def biayaobat(self,biaya):
        self.price=int(self.price)+int(biaya)
        
    def getpriceRoom(self):
        if self.tgl_masuk==self.tgl_keluar:
            return 0
        else:
            if self.no_id[:3]=='001':
                return int(str(self.tgl_keluar-self.tgl_masuk).split()[0])*350000
            elif self.no_id[:3]=='002':
                return int(str(self.tgl_keluar-self.tgl_masuk).split()[0])*400000
            elif self.no_id[:3]=='003':
                return int(str(self.tgl_keluar-self.tgl_masuk).split()[0])*450000
            elif self.no_id[:3]=='004':
                return int(str(self.tgl_keluar-self.tgl_masuk).split()[0])*500000
            elif self.no_id[:3]=='005':
                return int(str(self.tgl_keluar-self.tgl_masuk).split()[0])*550000

class Apoteker:
    def __init__(self,harga=0):
        self.harga=(20,25,25,25,30,30,50,50,70,70,110,110,110,110,110,110,110,120,120,140,140,140,140,140,140,14,15,170,50,40,30,20,90,90,
                    110,110,100,110,130,130,130,140,60,60,60,60)

    def get_obat(self):
        print("-------------------------------------------------------------------------")
        print("                      Apotek Hospotal")
        print("-------------------------------------------------------------------------")
        print("                      Menu Obat")
        print("-------------------------------------------------------------------------")
        print("----------------------------------    ")
        print("\n Obat Batuk/pilek/demam             26 minyak kayu putih 50ml...... 1400")
        print("----------------------------------    27 minyak kayu putih 100ml..... 1500")
        print(" 1 paracetamol............... 2000    28 minak kayu putih 120ml...... 17000")
        print(" 2 panadol biru.............. 2500")
        print(" 3 Panadol Flu Batuk......... 2500     Alkohol")
        print(" 4 inza...................... 2500     ----------------------------------")
        print(" 5 Oskadon................... 3000     29 Alkohol 100%............ 5000")
        print(" 6 mixagrip.................. 3000     30 Alkohol 70%............. 4000")
        print(" 7 napacin................... 5000     31 Alkohol 50%............. 3000")
        print(" 8 woods..................... 5000     32 Alkohol 30%............. 2000")
        print(" 9 OBH anak.................. 7000")
        print(" 10 OBH Batuk................ 7000          P3k")
        print("                                  ----------------------------------")
        print(" Obat salep                                 33 handsplast.......... 9000")
        print("----------------------------------------    34 betadin............. 9000")
        print(" 11 Balsem Lang 10 gr............ 11000    35 perban.............. 11000")
        print(" 12 Balsem Lang 20 gr............ 11000    36 benang jahit........ 11000")
        print(" 13 Balsem Geliga 10 gr.......... 11000")
        print(" 14 Balsem Geliga 20 gr.......... 11000    Obat Suntik")
        print(" 15 Balpirik merah............... 11000    ----------------------------------")
        print("                                           37 Xon-c............... 10000")
        print(" Minyak urut                               38 saridon............. 11000")
        print("----------------------------------         39 Masala Dosa......... 13000")
        print(" 16 fres Care........... 11000            40 Pulcracap........... 13000")
        print(" 17 safe care........... 11000            41 vitamin............. 13000")
        print(" 18 minyak kapak 10ml........... 12000    42 puyer 16............ 14000")
        print(" 19 minyak kapak 20ml........... 12000")
        print(" 20 minyak kapak 30ml........... 14000    obat tablet/kapsul")
        print(" 21 minyak tawon cc............. 14000    ----------------------------------")
        print(" 22 minyak tawon dd............. 14000    43 laxing.......... 6000")
        print(" 23 minyak tawon EE............. 14000    44 vitaminc........ 6000")
        print(" 24 Minyak Tekon 3 anak 60ml.... 14000    45 inzana.......... 6000")
        print(" 25 minyak telon 3 ankan 100ml.. 14000    46 hemaviton....... 6000")
        print("Press 0 -to end ")
        list_obat=list(map(int,input('List obat yang mau di beli (e.g 1 2 3 5) :').strip().split()))
        price=0
        for _ in list_obat:
            price+=self.harga[_-1]
        return price*100
    
def Insert():
    while True:
        name = input("Name: ")
        genre= input('Genre (male/female) : ')
        age=int(input('Age (e.g 18) : '))
        nphone = input("Phone No.: ")
        add= input("Address: ")
        sink=input("penyakit yang di derita :")
        
        #ambigu
        if name!="" and nphone!="" and add!="" and sink!="":
            break
                
        else:
            print("\tName, Phone no, Address. & penyakit yang diderita cannot be empty..!!")
        
    check=input('Do u want to get a room (y/n)?')
    if check=='y':
        cin=list(map(int,(input("Waktu masuk(dd/mm/yy): ").strip().split('/'))))
        cout=list(map(int,(input("Waktu masuk(dd/mm/yy): ").strip().split('/'))))
        timeStart=datetime.datetime(cin[2],cin[1],cin[0])
        timeOut=datetime.datetime(cout[2],cout[1],cout[0])
        while True:
            print("----SELECT ROOM TO PATIENT----")
            print(" 1. Intensive Care Unit (ICU)")
            print(" 2. High Care Unit (HCU)")
            print(" 3. Intensive Coronary Care Unit (ICCU)")
            print(" 4. Neonatal Intensive Care Unit (NICU)")
            print(" 5. Pediatric Intensive Care Unit (PICU)")
            ch=int(input("->"))
            if ch==1:
                room=1
                print('Intensive Care Unit (ICU)')
                print("Pasien Harus Cepat mendapatkan perawatan")
                print("rauangan dilengkapi peralatan canggih")
                #price.append(3500)
                print("Price per day- Rp.350000")
                break
            elif ch==2:
                room=2
                print('High Care Unit (HCU)')
                print("Untuk pasien rawat inap")
                print("ruangan dilengkapi peralatan canggih")
                #price.append(4000)
                print("Price per day - Rp.400000")
                break
            elif ch==3:
                room=3
                print('Intensive Coronary Care Unit (ICCU)')
                print("ruangan unutk penderita penyakit jantung")
                print("ruangan kedap suara dan hening")
                #price.append(4500)
                print("Price per day - Rp.450000")
                break
            elif ch==4:
                room=4
                print('Neonatal Intensive Care Unit (NICU)')
                print("ruangan untuk yang melahirkan")
                print("ruangan dilengkapi ruang tunggu orang tua")
                #price.append(5000)
                print("Price- 500000")
                break
            elif ch==5:
                room=5
                print('Pediatric Intensive Care Unit (PICU)')
                print("rauang untuk bayi dan 18 tahun")
                print("ruangan dilengkapi ruang tunggu orang tua")
                #price.append(5000)
                print("Price per day- Rp.500000")
                break
            else:
                print('Please enter the right choice')
        no_id=BaligeHostipal.getNo_id(room)
        passegger=Passegger(name,genre,age,add,nphone,no_id,sink,timeStart,timeOut)
        BaligeHostipal.appendPasegger(passegger)
        print('Terima kasih anda telah terdaftar sebagai pasien')
        print('No pasien anda : ', passegger.no_id)
        #print(("\t\tPress 0 for Apotek Room"))
    else: 
        time=datetime.datetime.now()
        #timeOut=datetime.datetime.now()
        passegger=Passegger(name,genre,age,add,nphone,None,sink,time,time)
        BaligeHostipal.appendPasegger(passegger)
        print('Terima kasih anda telah terdaftar sebagai pasien')
        print('No pasien anda : ', passegger.no_id)

        
def Rooms_Info():
    print("      ------  ROOMS INFO Hospital------")
    print("")
    print("Intensive Care Unit (ICU)")
    print("---------------------------------------------------------------")
    print("ICU adalh ruangan khusus bagi pasien kritis yang perlu perawatan intensif dan ")
    print("pengawasan terus menerus")
  
    print("High Care Unit (HCU)")
    print("---------------------------------------------------------------")
    print("HCU adalah pelayanan yang dikendalikan ke rauan rawat inap")
    print("ruangan ini di peruntukkan kepada pasien yang sudah kondisi membaik")
    print("namun masih perlu pengawasan ketat oleh tenaga medis\n")

    print("Intensive Coronary Care Unit (ICCU)")
    print("---------------------------------------------------------------")
    print("Ruangan ini cocok untuk penderita penyakit jantung.\n")
    
    print("Neonatal Intensive Care Unit (NICU)")
    print("---------------------------------------------------------------")
    print("Ruangan ini cocok untuk pelayanan bersalin/melahirkan,")

    print("Pediatric Intensive Care Unit (PICU)")
    print("---------------------------------------------------------------")
    print("Ruangan ini diperuntukkan bagi bayi yang tidak diambil NICU serta anak hingga 18 tahun,")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        return

        
        
def Payment(no_id):
    data=BaligeHostipal.getDataPasien(no_id)
    if data==False :
        print('Mohon maaf anda belum melakukan proses pendaftaran, Silahkan lakukan pendaftaran pada menu Insert')
    else:
        print(" Payment")
        print(" --------------------------------")
        print(" MODE OF PAYMENT")
        print('1. ATM')
        print('2. Cash\n')
        pilih_pay=input('- >')
        if pilih_pay=='1':
            print('Anda memilih menggunakan ATM')
        elif pilih_pay=='2':
            print('Anda memilih menggunakan sistem Cast')
        no_urut=BaligeHostipal.getposisiAntrian(no_id)
        price=BaligeHostipal.pasegger[no_urut].price
        BaligeHostipal.pasegger[no_urut].price=0
        print('Total biaya pengobatan anda sebesar Rp.',price)
        print('Silahkan lakukan proses pembayaran dan Terima kasih, Semoga lekas sembuh !!!\n\n\n')

def Record(no_id):
    data=BaligeHostipal.getDataPasien(no_id)
    if data==False :
        print('Mohon maaf anda belum melakukan proses pendaftaran, Silahkan lakukan pendaftaran pada menu Insert')

def Home():
    while True:
        print("\t\t\t\t\t\t Data Rumah Sakit\n")
        print("\t\t\t 1 Insert\n")
        print("\t\t\t 2 Rooms Info\n")
        print("\t\t\t 3 Apotek\n")
        print("\t\t\t 4 Payment\n")
        print("\t\t\t 5 Record\n")
        print("\t\t\t 0 Exit\n")

        ch=int(input("->"))
        if ch == 1:
            print(" ")
            Insert()
    
        elif ch == 2:
            print(" ")
            Rooms_Info()
    
        elif ch == 3:
            print(" ")
            price=Apotekbalige.get_obat()
            no_id=input('Silakan masukkan no_id anda :')
            data=BaligeHostipal.checkPasien(no_id)
            if data==False:
                print('Maaf anda belum mendaftarkan diri silahkan pergi ke menu insert untuk melakukan pendaftaran')
            else:
                BaligeHostipal.getDataPasien(no_id)
                no_urut=BaligeHostipal.getposisiAntrian(no_id)
                print(price)
                print(no_urut)
                BaligeHostipal.ubah_harga(price,no_urut)
                print( ' Harga obat yang harus anda bayar : Rp.',price)
                print('Thanks untuk pembelian nya semoga lekas sembuh, Silahkan melakukan pembayaran pada menu payment')
        elif ch == 4:
            print(" ")
            no_id=input('Silahkan masukkan no_id anda : ')
            Payment(no_id)
        elif ch == 5:
            print(" ")
            no_id=input('Silahkan masukkan no_id anda : ')
            Record(no_id)
        elif ch==0:
            print('Thank u, Get well soon')
            break
        else:
            print('Sorry, please enter the right number !!!')
    
BaligeHostipal=RumahSakit('Rumah Sakit Balige','Balige Tobasa',50,50,50,50,50)
Apotekbalige=Apoteker()
Home()
        