$(document).ready(function () {
  const newItem = '<li>Item</li>';

  $('DIV#add_item').on('click', function (event) {
    $('UL.my_list').append(newItem);
  });

  $('DIV#remove_item').on('click', function (event) {
    $('UL.my_list li:last').remove();
  });

  $('DIV#clear_list').on('click', function (event) {
    $('UL.my_list').empty();
  });
});
