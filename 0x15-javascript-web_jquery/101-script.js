/** Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks: */


$(document).ready(function() {

    let li = '<li>Item</li>';

    // add item to list
    $("#add_item").click(function() {
        $('.my_list').append(li);
    });

    // remove item from list
    $("#remove_item").click(function() {
        $('.my_list li:last-child').remove();
    });

    // clear list list from items
    $("#clear_list").click(function() {
        let li = '<li>Item</li>';
        $('.my_list').empty();
    });
});