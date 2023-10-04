/** Write a JavaScript script that adds a <li>
*  element to a list when the user clicks on the tag DIV#add_item:*/

$('5-main.html').ready(function() {
    $("#add_item").click(function() {
        let list = $('<li>Item</li>');

        $(".my_list").append(list);
    });
});