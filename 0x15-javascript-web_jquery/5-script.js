const newItem = '<li>Item</li>';
$('DIV#add_item').on('click', function (event) {
  $('UL.my_list').append(newItem);
});
