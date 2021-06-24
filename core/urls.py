from django.urls import path
from .views import index, pelicula_mulan, pelicula_padrino, pelicula_lo_que_arde, peliculas, series, pag_proceso, listado_pelicula, nueva_pelicula, modificar_pelicula, eliminar_pelicula, login_page, logout_view



urlpatterns = [
    path('', index, name="index"),
    path('pelicula-mulan/', pelicula_mulan, name="pelicula_mulan"),
    path('pelicula-padrino/', pelicula_padrino, name="pelicula_padrino"),
    path('pelicula-lo-que-arde/', pelicula_lo_que_arde, name="pelicula_arde"),
    path('peliculas/', peliculas, name="peliculas"),
    path('series/', series, name="series"),
    path('paginas_proceso/', pag_proceso, name="paginasinproces"),
    path('listado_peliculas/', listado_pelicula, name="listado_peliculas"),
    path('nueva_pelicula/', nueva_pelicula, name="nueva_pelicula"),
    path('modificar_pelicula/<id>/', modificar_pelicula, name="modificar_pelicula"),
    path('eliminar_pelicula/<id>/', eliminar_pelicula, name="eliminar_pelicula"),
    path('login/', login_page, name="login" ),
    path('logout', logout_view, name="logout") ,
]
