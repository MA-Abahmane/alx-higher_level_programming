/** Write a JavaScript script that fetches and lists the title for all movies by using this URL:
*  https://swapi-api.alx-tools.com/api/films/?format=json */


$('8-main.html').ready(function() {

    let URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Using jQuery's $.get() method to make the AJAX request
    $.get(URL, function(data) {

        let movies = data.results;

        let ul = $("#list_movies");

        $.each(movies, function(idx, movies) {

            let list = $('<li>').text(movies.title);
            ul.append(list);
        });
    });
});
