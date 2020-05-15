$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (titles) {
  $.each(titles['results'], function(data, movies) {
    $("#list_movies").append('<li>' + movies['title'] + '</li>');
  }); }, 'json');
