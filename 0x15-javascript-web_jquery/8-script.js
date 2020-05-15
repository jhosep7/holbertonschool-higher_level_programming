$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (movs) {
  $.each(movs['results'], function(data, movies) {
    $("#list_movies").append('<li>' + movies['title'] + '</li>');
  }); }, 'json');
