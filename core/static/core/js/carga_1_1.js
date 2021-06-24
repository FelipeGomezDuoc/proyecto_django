$('#submit-form').click(function(event) {

    event.preventDefault();
    var movie = $("#movie").val();

            
   $.ajax({
      url: 'http://www.omdbapi.com/?t='+movie+'&apikey=2f72185',
      data: {
         format: 'json'
      },
      error: function() {
         $('#info').html('<p>Un error ha ocurrido!!!!</p>');
      },
      dataType: 'json',
      success: function(data) {
         console.log(data);
         var $caratula = $("<p><img class='caratula' src='"+data.Poster+"'>");
         var $nombre_pelicula = $('<h1>').text(data.Title);
         var $lanzamiento = $('<p>').text(data.Released);
         var $duracion = $('<p>').text(data.Runtime);
         var $director = $('<p>').text(data.Director);
         var $escritor = $('<p>').text(data.Writer);
         var $actores = $('<p>').text(data.Actors);
         var $trama = $('<p>').text(data.Plot);
         var $premios = $('<p>').text(data.Awards);
         
         

        // para limpiar el contedor antes de desplegar
        $("#info").empty();
         $('#info')
            .append($caratula)
            .append($nombre_pelicula)
            .append($lanzamiento)
            .append($duracion)
            .append($director)
            .append($escritor)
            .append($actores)
            .append($trama)
            .append($premios);
            
      },
      type: 'GET'
   });
});

