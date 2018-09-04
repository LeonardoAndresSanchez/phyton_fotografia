from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.model import user
# Create your models here.
class Tipo_camara (models.Model):

	tipoc = models.CharField(max_length = 100)

	def __str__(self):
		return self.tipoc

class Modelo (models.Model):

	modeloc = models.CharField(max_length = 100)

	def __str__ (self):
		return self.modeloc

class Tipo_fotografia (models.Model):
	tipo      = models.CharField(max_length = 100)

	def __str__ (self):
		return self.tipo

class Camara(models.Model):

	camara = models.CharField(max_length =100)
	tipo  = models.ForeignKey(Tipo_camara, on_delete = models.CASCADE)
	modelo = models.ForeignKey(Modelo, on_delete = models.CASCADE)

	def __str__ (self):
		return self.camara + self.tipo.tipoc

class Fotos(models.Model):

	propietario = models.ForeignKey('auth.user', on_delete = models.CASCADE )
	titulo      = models.CharField(max_length=200)
	fecha       = models.DateField(auto_now_add = True)
	imagen      = models.ImageField(upload_to = 'Fotos_usuario',blank=True)

	def __str__(self):
		return self.propietario.username
		
class Fotografo(models.Model):
	nombre    = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 100)
	telefono  = models.IntegerField(max_length = 100)
	camara    = models.ForeignKey(Camara, on_delete = models.CASCADE)
	tipof     = models.ForeignKey(Tipo_fotografia, on_delete = models.CASCADE)
	foto      = models.ImageField(upload_to = 'fotografos', null = True, blank = True)
	user      = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

	def __str__ (self):
		return self.nombre

#perfil
class Perfil(models.Model):
	nombre = models.CharField(max_length = 100)
	identificacion = models.CharField(max_length = 100)
	Edad = models.CharField(max_length = 2)
	foto = models.ImageField(upload_to = 'perfiles', null = True, blank = True)
	user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.nombre
