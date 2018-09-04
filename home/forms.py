from django import forms
from .models import *
from django.contrib.auth.models import User
#from django import forms.TextInput

class contacto_form(forms.Form):
	nombre         = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control form-control-sm" }))
	correo         = forms.EmailField(widget = forms.TextInput(attrs = {"class" : "form-control form-control-sm" }))
	numero_telefono   = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control form-control-sm" }))
	texto          = forms.CharField(widget = forms.Textarea(attrs = {"class":"form-control form-control-sm" }))

#logoin andlogout

class login_form (forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs = {"class" : "form-control" }))
	clave   = forms.CharField(widget=forms.PasswordInput(render_value = False,attrs = {"class" : "form-control" }))

#Registro-usuario
class register_form (forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs = {"class" : "form-control form-control-sm" }))
	email = forms.EmailField(widget=forms.TextInput(attrs = {"class" : "form-control form-control-sm" }))
	password_1 = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False, attrs = {"class" : "form-control form-control-sm" }))
	password_2 = forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False,attrs = {"class" : "form-control form-control-sm" }))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ta existe')

	def clean_password_2(self):#se hace validacion del password_2
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']

		if password_1==password_2:
			pass
		else: 
			raise forms.ValidationError('Passwords no Coinciden')

#perfil
class perfil_form(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ['nombre','identificacion','Edad','foto']
		exclude = ['user']
		widgets = {
		'nombre' :forms.TextInput(attrs = {'class' :'form-control form-control-sm' }),
		'identificacion' :forms.TextInput(attrs = {'class' :'form-control form-control-sm' }),
		'Edad' :forms.TextInput(attrs = {'class' :'form-control form-control-sm' }),
		'foto' : forms.FileInput(attrs = {'class' :'form-control-file' })	
		}



#Formularios agregar
class agregar_fotografos_form(forms.ModelForm):
	class Meta:
		model = Fotografo
		fields =['nombre', 'direccion', 'telefono', 'camara','tipof','foto']
		exclude = ['user'] 
		widgets = {
		'nombre' :forms.TextInput(attrs = {'class' :'form-control form-control-sm' }),
		'direccion':forms.TextInput(attrs = {'class' :'form-control form-control-sm' }),
		'telefono':forms.TextInput(attrs = {'class' :'form-control form-control-sm' }),
		'camara':forms.Select(attrs = {'class' :'form-control ' }),
		'tipof':forms.Select(attrs = {'class' :'form-control ' }),
		'foto' : forms.FileInput(attrs = {'class' :'form-control-file' })
		}
#agregar imagenes
class agregar_fotos_form(forms.ModelForm):
	class Meta:
		model = Fotos
		fields = ['titulo','imagen']
		exclude = ['propietario']
		widget = {
		'titulo':forms.TextInput(attrs = {'class': 'form-control form-control-sm'}),
		'imagen': forms.FileInput(attrs = {'class' :'form-control-file' })

		}



class agregar_camaras_form(forms.ModelForm):
	class Meta:
		model = Camara
		fields = '__all__'

#class agregar_tipo_camara_form(forms.ModelForm):
	#class Meta:
		#model = Tipo_camara
		#fields = '__all__'

#class agregar_modelo_form(forms.ModelForm):
	#class Meta:
		#model =  Modelo
		#fileds = '__all__'

#class agregar_tipo_fotografia_form(forms.ModelForm):
	#class Meta:
		#model = Tipo_fotografia
		#fields = '__all__'


