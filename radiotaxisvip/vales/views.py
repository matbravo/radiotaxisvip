from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate , login , logout


# Create your views here.


#################################################
############ Helpers for  controllers ###########
#################################################

def user_check(user):
	return user.is_authenticated()

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
		        return redirect("/vales/administracion")
		        #login(request,user)
		        #redirect(request, "administracion")
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
######## Administracion controller ##############
#################################################

@user_passes_test(user_check, login_url='/vales/')
def administracion(request):
	context = {}
	return render(request, "administracion.html" , context)

#################################################
############# Locucion controller ###############
#################################################

@user_passes_test(user_check, login_url='/vales/')
def locucion(request):
	context = {}
	return render(request, "locucion.html" , context)

#################################################
########### Contabilidad controller #############
#################################################

@user_passes_test(user_check, login_url='/vales/')
def contabilidad(request):
	context = {}
	return render(request, "contabilidad.html" , context)

