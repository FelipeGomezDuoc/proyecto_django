function confirmarEliminacion(id) {
    Swal.fire({
        title: 'Estas seguro?',
        text: "no podras revertir esta accion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: 'cancelar',
        confirmButtonText: 'confirmar!'
    }).then((result) => {
        if (result.value) {
            //redirigir al usuario a la ruta eliminar
            window.location.href = "/eliminar_pelicula/" + id + "/";

        }
    })
}