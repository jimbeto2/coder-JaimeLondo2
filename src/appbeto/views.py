from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
	print("Hola Pepito") #esto lo va a imprimir en consola
	return HttpResponse("Mensaje respuesta dede Django AppBeto!") #este mensaje se lo va a pasar a django
#y este lo que hace automaticamente con el httpresponse es generar un archivo html con esa info
#en algun lado de la pagina pero debo conocer como se le da formato a ese mensaje


#como opcion mejorada y alternativa es simplemente llamar a un archivo html que sea elaborado
#por un experto en front y listo eso lo vemos aca:
def inicio(request):
	return render(request, 'appbeto/inicio.html')

def jlvariables(request):
	datos = {
		'variable01' : 'hola, variable1',
		'variable02' : 'hola, variable2',
		'variable03' : 'hola, variable3',
	}
	return render(request, 'appbeto/inicio.html', context=datos)


# Create your views here.
