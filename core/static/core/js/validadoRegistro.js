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
            },
            email: {
                required: true
                
            }
        },
            messages: {
                nombre: {
                    minlength: "El nombre debe tener al menos 4 caracteres"
                },
                contrasena: {
                    contrasena: "Debe tener al menos 5 caracteres"
                },
                mail: {
                    email: "Por favor, escriba una dirección de correo válida."
                }
            }
        });
    });