/** Write a JavaScript script that fetches the character name from this URL:
*  https://swapi-api.alx-tools.com/api/people/5/?format=json */

$('7-main.html').ready(function() {

    let URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

    // Using jQuery's $.get() method to make the AJAX request
    $.get(URL, function(data) {

        let chName = data.name;

        $("#character").text(chName);
    });
});