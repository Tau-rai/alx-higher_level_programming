$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',

  success: function (result) {
    $.each(result.results, function (i, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
