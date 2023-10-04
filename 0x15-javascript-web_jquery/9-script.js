/** Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
 *  and displays the value of hello from that fetch in the HTML tag DIV#hello.*/


$('9-main.html').ready(function() {

    let URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

    // Using jQuery's $.get() method to make the AJAX request
    $.get(URL, function(data) {

        let helloVal = data.hello;

        $("#hello").text(helloVal);
    });
});
