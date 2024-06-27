# membuat fungsi

def cetak(nama):
    print('hello ' + nama + ' kamu sehat?') 
    
cetak('ucup')
    
anggota_boyband=["rijal","fahmi","zaenal","ilham"]

for list_nama in anggota_boyband:
    print('yang terhormat '+list_nama)
    

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print("Oii apa kabar " + peserta)

say_hi(anggota_boyband)
print ('===============')
print (' ')
print (' ')

def kuadrat(masukan):
    hasil = masukan**2
    return hasil

y = kuadrat(5)
print(y)

#default argument 

def say_hello(nama):
    print('hallio ' + nama)
    
say_hello('boy')