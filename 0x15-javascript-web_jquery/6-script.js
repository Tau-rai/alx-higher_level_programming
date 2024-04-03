const newHeader = 'New Header!!!';
$('DIV#update_header').on('click', function (event) {
  $('header').text(newHeader);
});
