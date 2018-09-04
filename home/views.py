from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
#from .models import *

# Create your views here.
def vista_about (request):
	return render(request,'about.html')

#vistan de inicio

def vista_inicio (request):
	return render(request, 'inicio.html')


#vista de contacto 

def vista_contacto (request):
	info_enviado = False
	nombre   = ""
	email    = ""
	telefono = ""
	text     = ""
	if request.method == "POST":
		fomulario = contacto_form(request.POST)
		if fomulario.is_valid():
			info_enviado = True
			nombre = fomulario.cleaned_data['nombre']
			email = fomulario.cleaned_data['correo']
			telefono = fomulario.cleaned_data['numero_telefono']
			text = fomulario.cleaned_data['texto']
		return render(request, 'gracias_por_registrar.html'.locals())
	else:
		formulario = contacto_form()
	return render(request, 'contacto.html', locals())

def vista_menu (request):
	return render(request, 'menu.html')

#Registro-usuario

def vista_registro(request):
	form_1 = agregar_fotografos_form()
	form_2 = register_form()
	if request.method == 'POST':
		form_1 = agregar_fotografos_form(request.POST)
		form_2 = register_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario = form_2.cleaned_data['username']
			correo = form_2.cleaned_data['email']
			password_1 = form_2.cleaned_data['password_1']
			password_2 = form_2.cleaned_data['password_2']
			u = User.objects.create_user(username = usuario, email = correo,password = password_1)
			u.save()
			z = form_1.save (commit =False)
			z.user = u
			z.save()
			return render(request, 'login.html', locals())
		else:
			return render(request, 'register.html',locals())
	return render(request,'register.html',locals())
	


	#formulario = register_form()
	#if request.method== 'POST':
		#formulario = register_form(request.POST)
		#if formulario.is_valid():
			#usuario = formulario.cleaned_data['username']
			#correo = formulario.cleaned_data['email']
			#password_1 = formulario.cleaned_data['password_1']
			#password_2 = formulario.cleaned_data['password_2']
			#u = User.objects.create_user(username=usuario,email=correo,password=password_1)
			#u.save()
			#return render(request, 'gracias_por_registrar.html', locals())
		#else:
			#return render (request, 'register.html', locals())
	#return render(request,'register.html', locals())


#Login and Logout

def vista_login (request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulariolg = login_form(request.POST)
		if formulariolg.is_valid():
			usu = formulariolg.cleaned_data['usuario']
			cla = formulariolg.cleaned_data['clave']
			usuario = authenticate(username = usu, password = cla)
			if usuario is not None and usuario.is_active:
				login(request,usuario)
				return redirect('/')
			else:
				msj = "usuario o clave incorrectos"
	formulariolg = login_form()
	return render(request, 'login.html', locals())

def vista_logout(request):
	logout(request)
	return redirect('/login/')

#vista perfil

def vista_perfil(request):
	perfil =  Fotografo.objects.get(user = request.user)
	img = Fotos.objects.filter(propietario = request.user)
	print (img)
	return	render(request,'perfil.html',locals())

	
#Fotografo

def vista_lista_fotografos (request):
	lista = Fotografo.objects.filter()
	return render(request, 'lista_fotografos.html', locals())

def vista_agregar_fotografo(request):
	if request.method == 'POST':
		formulariof =  agregar_fotografos_form(request.POST, request.FILES)
		if formulariof.is_valid:
			foto= formulariof.save(commit = False)
			foto.status = True
			foto.save()
			return redirect ('/lista_fotografos/')

	else:
		formulariof = agregar_fotografos_form()
	return render(request, 'vista_agregar_fotografo.html',  locals())

def vista_ver_fotografo(request, id_fotog):
	f = Fotografo.objects.get(id = id_fotog)
	return render (request, 'ver_fotografo.html', locals())

def vista_editar_fotografo(request,id_fotog):
	foto = Fotografo.objects.get(id=id_fotog)
	if request.method == "POST":
		formulariof = agregar_fotografos_form(request.POST, request.FILES, instance = foto)
		if formulariof.is_valid():
			foto = formulariof.save()
			return redirect ('/lista_fotografos/')
	else:
		formulariof = agregar_fotografos_form(instance = foto)
	return render (request, 'vista_agregar_fotografo.html', locals())

def vista_eliminar_fotografo(request,id_fotog):
	foto = Fotografo.objects.get(id=id_fotog)
	foto.delete()
	return redirect ('/lista_fotografos/')

#Camara
def vista_lista_camaras (request):
	listac = Camara.objects.filter()
	return render(request, 'lista_camaras.html', locals())

def vista_agregar_camara(request):
	if request.method =='POST':
		fomularioc = agregar_camaras_form(request.POST, request.FILES)
		if fomularioc.is_valid:
			camma = formularioc.save(commit = False)
			camma,status = True
			camma.save()
			return redirect ('/lista_camaras/')
	else:
		formularioc = agregar_camaras_form()
	return render(request, 'vista_agregar_camara.html', locals())

def vista_ver_camara(request):
	c = Camara.objects.get( id = id_cam)
	return render (request,'ver_camara.html', locals())

def vista_editar_camara(request,id_cam):
	if request.method == "POST":
		formularioc = agregar_camaras_form(request.POST, request.FILES, instance = camma)
		if formularioc.is_valid():
			camma = formularioc.save()
			return redirect('/listar_camaras/')
	else:
		fomularioc = agregar_camaras_form(instance = cam)
	return render(request, 'vista_agregar_camara.html',locals())

def vista_eliminar_camara(request,id_cam):
	camma = Camara.objects.get(id = id_cam)
	camma.delete()
	return redirect ('/lista_camaras/')


def vista_agregar_fotos(request):

	if request.method =='POST':
		form = agregar_fotos_form(request.POST, request.FILES)
		if form.is_valid():
			x = form.save(commit=False)
			x.propietario = request.user
			x.save()
			mensaje = "Image uploaded succesfully!"
			return redirect ('/perfil/')
	else:
		form = agregar_fotos_form()
	return render(request, 'vista_agregar_fotos.html', locals())

