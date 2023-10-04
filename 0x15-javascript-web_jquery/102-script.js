/** Write a JavaScript script that fetches and prints how to say “Hello” depending on the language: */


$(document).ready(function() {
    // Add a click event listener to the "Translate" button
    $("#btn_translate").click(function() {
        // Get the language code entered by the user
        let lang = $("#language_code").val();

        // Define the API URL with the selected language code
        let apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;

        // Use jQuery's $.get() method to make the AJAX request
        $.get(apiUrl, function(data) {
            // Extract the translation of "Hello" from the fetched data
            let helloTranslation = data.hello;

            // Display the translation in the <div> with id "hello"
            $("#hello").text(helloTranslation);
        });
    });
});