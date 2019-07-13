#!/bin/env python 
#-*- coding: utf-8 -*-


alfabeto = "abcdefghijklmnopqrstuvwxyz "

def cifrar(palavra, chave):
	texto_cifrado = ''
	i=0
	for letra in palavra:
		total = alfabeto.find(letra) + alfabeto.find(chave[i % len(chave)])
		modulo = int(total) % len(alfabeto)
		texto_cifrado = texto_cifrado + str(alfabeto[modulo])
		i+=1

	return texto_cifrado

def decifrar(palavra, chave):
	texto_cifrado = ''
	i=0
	for letra in palavra:
		total = alfabeto.find(letra) - alfabeto.find(chave[i % len(chave)])
		modulo = int(total) % len(alfabeto)
		texto_cifrado = texto_cifrado + str(alfabeto[modulo])
		i+=1

	return texto_cifrado

if __name__ == '__main__':

	print("Cifrar")
	mensagem = input('Digite a mensagem: ').lower()
	chave = input('Digite a chave: ').lower()
	print(cifrar(mensagem, chave))


	print("Deciifrar")
	mensagem = input('Digite a mensagem: ').lower()
	chave = input('Digite a chave: ').lower()
	print(decifrar(mensagem, chave))