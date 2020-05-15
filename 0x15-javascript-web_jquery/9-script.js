$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (fish) {$('#hello').append(fish.hello); }
});
