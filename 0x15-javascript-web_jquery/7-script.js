$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (myJson) {
    $('#character').append(myJson.name);
    console.log(myJson.name);
  }
});
