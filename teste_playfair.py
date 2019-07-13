from playfair import Playfair

# O código playfair.py, precisa do arquivo cipher.py

versao = sys.version_info[0]
  
if versao == 2:
	leitura = raw_input
elif versao == 3:
	leitura = input
 
txt_in = leitura('Texto a ser cifrado: ')
password = leitura('Senha: ')
 
cifra = Playfair()
cifrado = cifra.encrypt(txt_in, password)
print(cifrado)
print(cifra.decrypt(cifrado, password))