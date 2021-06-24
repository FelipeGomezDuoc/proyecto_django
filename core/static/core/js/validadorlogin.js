$(document).ready(function() {
    $("#login-form").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 4
            
            },
            contrasena: {
                required: true,
                minlength: 5
            }
        },
            messages: {
                nombre: {
                    minlength: "El nombre debe tener al menos 4 caracteres"
                },
                contrasena: {
                    contrasena: "Debe tener al menos 5 caracteres"
                }
            }
        });
    });

const formulario =  document.getElementById("#login-form");

formulario.addEventListener("submit", function(event){
    event.preventDefault();
})
