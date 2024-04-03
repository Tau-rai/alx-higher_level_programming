const divHeader = $('header');
$('DIV#toggle_header').on('click', function (event) {
  if (divHeader.hasClass('red')) {
    divHeader.toggleClass('green red');
  } else if (divHeader.hasClass('green')) {
    divHeader.toggleClass('green red');
  } else {
    divHeader.addClass('red');
  }
});
