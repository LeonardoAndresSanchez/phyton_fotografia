from django.urls import path
from .views import *


urlpatterns = [
	
		path('about/', vista_about),
		path('contacto/', vista_contacto),
		path('menu/', vista_menu),

		#Inicio
		path('',vista_inicio, name = 'vista_inicio'),
		#path('inicio.php',vista_inicio, name = 'vista_inicio'),

		#login and logout
		path('login/',vista_login, name = 'vista_login'),
		path('logout/',vista_logout, name = 'vista_logout'),

		#registro-Usuario
		path('register/', vista_registro, name = 'vista_registro'),

		#perfil
		path ('perfil/', vista_perfil, name = 'vista_perfil'),

		#Urls-Fotografo
		path('lista_fotografos/', vista_lista_fotografos, name = 'vista_lista_fotografos' ),
		path('agregar_fotografo/', vista_agregar_fotografo , name = 'vista_agregar_fotografo' ),
		path('ver_fotografo/<int:id_fotog>/', vista_ver_fotografo, name = 'vista_ver_fotografo'),
		path('editar_fotografo/<int:id_fotog>/', vista_editar_fotografo, name ='vista_editar_fotografo'),
		path('eliminar_fotografo/<int:id_fotog>/', vista_eliminar_fotografo, name = 'vista_eliminar_fotografo'),

		#Urls-Camara
		path('lista_camaras/', vista_lista_camaras, name = 'vista_lista_camaras'),
		path('agregar_camara/',vista_agregar_camara, name = 'vista_agregar_camara'),
		path('ver_camara/<int:id_cam>/', vista_ver_camara, name = 'vista_ver_camara'),
		path('editar_camara/<int:id_cam>/', vista_editar_camara, name = 'vista_editar_camara'),
		path('eliminar_camara/<int:id_cam>/', vista_eliminar_camara, name = 'vista_eliminar_camara'),

		#Urls-Marca
		#path('lista_marcas/', vista_lista_marcas, name = 'vista_lista_marcas'),
		#path('agregar_marca/',vista_agregar_marca, name = 'vista_agregar_marca'),
		#path('ver_marca/<int:id_mar>/', vista_ver_marca, name = 'vista_ver_marca'),
		#path('editar_marca/<int:id_mar>/', vista_editar_marca, name = 'vista_editar_marca'),
		#path('eliminar_marca/<int:id_mar>/', vista_eliminar_marca, name = 'vista_eliminar_marca'),

		#Urls-Tipo_camara

		#path('lista_tipo_camaras/', vista_lista_tipo_camaras, name = 'vista_lista_tipo_camaras'),
		#path('agregar_tipo_camara/',vista_agregar_tipo_camara, name = 'vista_agregar_tipo_camara'),
		#path('ver_tipo_camara/<int:id_tcam>/', vista_ver_tipo_camara, name = 'vista_ver_tipo_camara'),
		#path('editar_tipo_camara/<int:id_tcam>/', vista_editar_tipo_camara, name = 'vista_editar_tipo_camara'),
		#path('eliminar_tipo_camara/<int:id_tcam>/', vista_eliminar_tipo_camara, name = 'vista_eliminar_tipo_camara'),

		#Urls-Tipo_fotografia

		#path('lista_tipo_fotografias/', vista_lista_tipo_fotografias, name = 'vista_lista_tipo_fotografias'),
		#path('agregar_tipo_fotografia/',vista_agregar_tipo_fotografia, name = 'vista_agregar_tipo_fotografia'),
		#path('ver_tipo_fotografia/<int:id_cam>/', vista_ver_tipo_fotografia, name = 'vista_ver_tipo_fotografia'),
		#path('editar_tipo_fotografia/<int:id_cam>/', vista_editar_tipo_fotografia, name = 'vista_editar_tipo_fotografia'),
		#path('eliminar_tipo_fotografia/<int:id_cam>/', vista_eliminar_tipo_fotografia, name = 'vista_eliminar_tipo_fotografia'),

		#urls fotos
		path('agregar_fotos/',vista_agregar_fotos, name = 'vista_agregar_fotos'),



] 