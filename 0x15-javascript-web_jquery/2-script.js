/* global $ */
const divHeader = $('header');
$('DIV#red_header').on('click', function (event) {
  divHeader.css('color', '#FF0000');
});
