from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm
from .forms import LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def pelicula_mulan(request):
    return render(request, 'core/pelicula_mulan.html')

def pelicula_padrino(request):
    return render(request, 'core/pelicula_padrino.html')

def pelicula_lo_que_arde(request):
    return render(request, 'core/pelicula_lo_que_arde.html')

def peliculas(request):
    return render(request, 'core/peliculas.html')

def series(request):
    return render(request, 'core/series.html')

def pag_proceso(request):
    return render(request, 'core/paginasinproces.html')

def listado_pelicula(request):
    peliculas = Pelicula.objects.all()
    data ={
        'peliculas':peliculas
    }
    return render (request, 'core/listado_peliculas.html', data)

@login_required
def nueva_pelicula(request):
    data ={
        'form':PeliculaForm()
    }

    if request.method =='POST':
        formulario = PeliculaForm(request.POST, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
        data['form'] = formulario

    return render(request, 'core/nueva_pelicula.html', data)

@login_required
def modificar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    data = {
        'form': PeliculaForm(instance=pelicula)
    }

    if request.method == 'POST':
        formulario = PeliculaForm(data=request.POST, instance=pelicula)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificacion correcta"
            data['form'] = formulario

    return render(request, 'core/modificar_pelicula.html', data)

@login_required
def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()

    return redirect(to='listado_peliculas')


def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                    return render(request,'index.html', {'message': message, 'form':form})
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()
    return render(request,'login.html', {'message': message, 'form':form}
                            )
    
def index(request):
    return render(request,'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

