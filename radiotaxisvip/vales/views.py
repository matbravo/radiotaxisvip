from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate , login , logout
from vales.models import Vale
from vales.models import ValeForm
from django.http import HttpResponse

# Create your views here.


#################################################
############ Helpers for  controllers ###########
#################################################

def user_check(user):
	return user.is_authenticated()

def user_agregar(user):
	return user.has_perm("vales.add_vale") and user.is_authenticated()

def user_modify(user):
	return user.has_perm("vales.modify_vale") and user.is_authenticated()

#################################################
############### Index controller ################
#################################################

def index(request):
	context = {}
	if request.method == 'POST':
		name = request.POST['name']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
		    # the password verified for the user
		    if user.is_active:
		        print("User is valid, active and authenticated")
		        login(request,user)
		        return redirect("/vales/home")
		    #else:
		        #print("The password is valid, but the account has been disabled!")
		#else:
		    # the authentication system was unable to verify the username and password
		    #print("The username and password were incorrect.")
	
	return render(request, "index.html" , context)

#################################################
############### Logout controller ###############
#################################################

def logout_user(request):
	logout(request)
	context = {}
	return render(request, "index.html" , context)

#################################################
######## Home controller ##############
#################################################

@user_passes_test(user_check, login_url='/vales/')
def home(request):
	vales = Vale.objects.all().reverse()
	vales_aceptados = vales.filter(estado="A",en_espera=False).count()
	vales_rechazados = vales.filter(estado="R",en_espera=False).count()
	vales_sin_observar = vales.filter(estado="S",en_espera=False).count()
	vales_en_espera = vales.filter(en_espera=True).count()
	context = { "vales" : vales ,
				"vales_aceptados" : vales_aceptados,
				"vales_rechazados" : vales_rechazados,
				"vales_sin_observar" : vales_sin_observar,
				"vales_en_espera" : vales_en_espera,
				}

	return render(request, "home.html" , context)

#################################################
############# Agregar controller ###############
#################################################

@user_passes_test(user_agregar, login_url='/vales/')
def agregar(request):
	if request.method == "POST":
		form = ValeForm(request.POST)
		if form.is_valid():
			vale = form.save(commit=False)
			vale.estado = 'S'
			vale.usuario = request.user
			vale.en_espera = True
			vale.distancia = "0"
			vale.costo = "0"
			vale.fecha_termino = vale.fecha_inicio
			vale.save()
			return redirect("/vales/agregar")

	vales = Vale.objects.all().reverse()
	vales_aceptados = vales.filter(estado="A",en_espera=False).count()
	vales_rechazados = vales.filter(estado="R",en_espera=False).count()
	vales_sin_observar = vales.filter(estado="S",en_espera=False).count()
	vales_en_espera = vales.filter(en_espera=True).count()
	context = { "vales" : vales ,
				"vales_aceptados" : vales_aceptados,
				"vales_rechazados" : vales_rechazados,
				"vales_sin_observar" : vales_sin_observar,
				"vales_en_espera" : vales_en_espera,
				}
	return render(request, "agregar.html" , context)

@user_passes_test(user_agregar, login_url='/vales/')
def agregar_mod(request):
	if request.method == "POST":
		vale = Vale.objects.get(pk=request.POST['vale-id'])
		vale.distancia = request.POST['distancia']
		vale.costo = request.POST['costo']
		vale.en_espera = False
		vale.save()
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=400)

#################################################
############# Cambiar estado controller #########
#################################################

@user_passes_test(user_modify, login_url='/vales/')
def cambiar_estado(request):
	if request.method == "POST":
		vale = Vale.objects.get(pk=request.POST['vale-id'])
		vale.estado = request.POST['vale-estado']
		vale.save()
		return redirect("/vales/cambiar_estado")
	vales = Vale.objects.all().reverse()
	vales_aceptados = vales.filter(estado="A",en_espera=False).count()
	vales_rechazados = vales.filter(estado="R",en_espera=False).count()
	vales_sin_observar = vales.filter(estado="S",en_espera=False).count()
	vales_en_espera = vales.filter(en_espera=True).count()
	context = { "vales" : vales ,
				"vales_aceptados" : vales_aceptados,
				"vales_rechazados" : vales_rechazados,
				"vales_sin_observar" : vales_sin_observar,
				"vales_en_espera" : vales_en_espera,
				}
	return render(request, "cambiar_estado.html" , context)

#################################################
############# Verificar controller #########
#################################################

@user_passes_test(user_check, login_url='/vales/')
def verificar(request):
	vales = Vale.objects.all().reverse()
	vales_aceptados = vales.filter(estado="A",en_espera=False).count()
	vales_rechazados = vales.filter(estado="R",en_espera=False).count()
	vales_sin_observar = vales.filter(estado="S",en_espera=False).count()
	vales_en_espera = vales.filter(en_espera=True).count()
	context = { "vales" : vales ,
				"vales_aceptados" : vales_aceptados,
				"vales_rechazados" : vales_rechazados,
				"vales_sin_observar" : vales_sin_observar,
				"vales_en_espera" : vales_en_espera,
				}
	return render(request, "verificar.html" , context)

@user_passes_test(user_check, login_url='/vales/')
def verificar_vale(request,vale_id):
	
	vales = Vale.objects.all()

	vales_aceptados = vales.filter(estado="A",en_espera=False).count()
	vales_rechazados = vales.filter(estado="R",en_espera=False).count()
	vales_sin_observar = vales.filter(estado="S",en_espera=False).count()
	vales_en_espera = vales.filter(en_espera=True).count()
	vales = vales.filter(pk=vale_id)
	context = { "vales" : vales ,
				"vales_aceptados" : vales_aceptados,
				"vales_rechazados" : vales_rechazados,
				"vales_sin_observar" : vales_sin_observar,
				"vales_en_espera" : vales_en_espera,
				}
	return render(request, "verificar.html" , context)





