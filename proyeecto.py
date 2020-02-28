import os

class cocinar():
	harina_maiz = 2
	harina_leudante = 2
	huevo = 1
	azucar = 2
	sal = 1
	leche = 1
	agua= 1
	
	def indicaciones ():
		print ('Bienvenido al recetario de comidas simples, aquí le mostraremos cómo realizar las masas básicas para cocinar')
		print ('Recomendamos seguir paso a paso las instrucciones de cada receta, del caso contrario la masa podría verse afectada')
		print ('Para realizar cualquiera de las recetas necesitará:')
		print ('Harina de Maiz/Harina Leudante')
		print ('Azucar/sal')
		print ('Leche/agua/huevo')
		print ('')
		print ('Esperamos que disfrute de las recetas y mucha suerte cocinando!')
		print ('Recuerden apagar la ornilla al terminar =D')
		
	def recetario_panquecas ():
		print('Para realizar las panquecas será necesario:')
		print ('2 tazas de harina leudante')
		print ('2 tazas de azucar')
		print ('1 taza de leche')
		print ('1 huevo')
		
	def panquecas (self):
		print ('Paso 1: las tazas de harina leudante necesarias para una mezcla de panquecas son 2')
		h=0
		while h!=2:
			h=int(input('Ingrese las tazas de harina leudante: '))
			print ('')
			if h!=self.harina_leudante:
				print ('No puede realizar la mezcla con esa cantidad de harina,por favor intente de nuevo')
			else:
				print ('Son las tazas correctas!')
		print ('')
		print ('Paso 2: para darle gusto a la mezcla, son necesarias 2 tazas de azucar')
		a=0
		while a!=2:
			a= int(input('Ingrese las tazas de azucar necesarias: '))
			print ('')
			if a!=self.azucar:
				print ('No puede realizar la mezcla con esa cantidad de azucar, por favor intente de nuevo')
			else:
				print ('Su gusto es ideal!')
		print ('')
		print ('Paso 3: se necesita 1 taza de leche para eligerar la masa')
		b=0
		while b!=1:
			b= int(input('Ingrese la cantidad de tazas: '))
			print ('')
			if b!=self.leche:
				print ('No puede realizar la mezcla con esa cantidad de leche, por favor intente de nuevo')
			else:
				print ('Es la cantidad suficiente de leche!')
		print ('')
		print ('Paso 4: Es necesario agregar 1 huevo')
		l=0
		while l!=1:
			l= int(input('Ingrese el huevo necesario para la mezcla: '))
			print ('')
			if l!=self.huevo:
				print ('No puede realizar la mezcla con esa cantidad de huevo, por favor intente de nuevo')
			else:
				print ('Todos los ingredientes han sido agregados, proceda a mezclarlos y tendrá lista su mezcla lista para cocinar!')
				print ('')
				
	def recetario_arepita ():
		print('Para realizar la masa de las arepas será necesario:')
		print ('2 tazas de harina de maiz')
		print ('1 cucharada de sal')
		print ('1 taza de agua')
		
	def arepita (self):
		print ('Paso 1: para realizar la masa de las arepas, son necesarias 2 tazas')
		h=0
		while h!=2:
			h=int(input('Ingrese las tazas de harina de maiz: '))
			print ('')
			if h!=self.harina_maiz:
				print ('No puede realizar la mezcla con esa cantidad de harina,por favor intente de nuevo')
			else:
				print ('Son las tazas correctas!')
		print ('')
		print ('Paso 2: para agregarle un gusto leve a la mezcla, agregue 1 cucharada de sal')
		a=0
		while a!=1:
			a= int(input('Ingrese las tazas de azucar necesarias: '))
			print ('')
			if a!=self.sal:
				print ('No puede realizar la mezcla con esa cantidad de sal, por favor intente de nuevo')
			else:
				print ('La masa tendrá buen gusto!')
		print ('')
		print ('Paso 3: se necesita 1 taza de agua para darle consistencia a la masa')
		b=0
		while b!=1:
			b= int(input('Ingrese la cantidad de tazas: '))
			print ('')
			if b!=self.agua:
				print ('No puede realizar la mezcla con esa cantidad de agua, por favor intente de nuevo')
			else:
				print ('Es la cantidad suficiente de agua!')
		print ('Todos los ingredientes están listos, proceda a mezclar y la masa estará lista!')
		print ('')
	
	def recetario_empanadas ():
		print('Para realizar la masa de empanadas será necesario:')
		print ('2 tazas de harina leudante')
		print ('1 cucharada de sal')
		print ('1 taza de agua')
	
	def empanadas (self):
		print ('Paso 1: para realizar la masa de las empanadas, son necesarias 2 tazas de harina leudante')
		h=0
		while h!=2:
			h=int(input('Ingrese las tazas de harina de leudante: '))
			print ('')
			if h!=self.harina_leudante:
				print ('No puede realizar la mezcla con esa cantidad de harina,por favor intente de nuevo')
			else:
				print ('Son las tazas correctas!')
		print ('')
		print ('Paso 2: para agregarle un gusto leve a la mezcla, agregue 1 cucharada de sal')
		a=0
		while a!=1:
			a= int(input('Ingrese las tazas de azucar necesarias: '))
			print ('')
			if a!=self.sal:
				print ('No puede realizar la mezcla con esa cantidad de sal, por favor intente de nuevo')
			else:
				print ('La masa tendrá buen gusto!')
		print ('')
		print ('Paso 3: se necesita 1 taza de agua para darle consistencia a la masa')
		b=0
		while b!=1:
			b= int(input('Ingrese la cantidad de tazas: '))
			print ('')
			if b!=self.agua:
				print ('No puede realizar la mezcla con esa cantidad de agua, por favor intente de nuevo')
			else:
				print ('Es la cantidad suficiente de agua!')
		print ('Todos los ingredientes están listos, proceda a mezclar y la masa estará lista!')
		print ('')
		
coci = cocinar
opci=0
while opci !=4:
	print ('Recetario de comidas')
	print ('1. Indicaciones')
	print ('2. Panquecas')
	print ('3. Arepa')
	print ('4. Empanada')
	print ('0. Salir')
	opci= int(input ('Ingrese la opcion deseada: '))
	os.system ('cls')
	
	if opci==1:
		coci.indicaciones ()
		print ('')
		print ('Presione ENTER')
		a=input ()
		os.system ('cls')
		
	if opci==2:
		coci.recetario_panquecas ()
		print ('')
		print ('Presione ENTER para continuar')
		a=input ()
		os.system ('cls')
		coci.panquecas (coci)
		a=input ('Presione ENTER para volver al menu')
		os.system('cls')
	if opci==3:
		coci.recetario_arepita ()
		print ('')
		print ('Presione ENTER para continuar')
		a=input ()
		os.system ('cls')
		coci.arepita (coci)
		a=input ('Presione ENTER para volver al menu')
		os.system('cls')
		
	if opci==4:
		coci.recetario_empanadas ()
		print ('')
		print ('Presione ENTER para continuar')
		a=input ()
		os.system ('cls')
		coci.empanadas (coci)
		a=input ('Presione ENTER para volver al menu')
		os.system('cls')
		
	if opci==5:
		print ('Si desea volver a ver el menu, presione 5')
		opci=int(input())
		os.system ('cls')
	
	if opci==0:
		os.system ('cls')
		break
