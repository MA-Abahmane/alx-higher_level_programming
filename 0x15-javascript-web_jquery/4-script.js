/** Write a JavaScript script that toggles the class of the <header>
 *  element when the user clicks on the tag DIV#toggle_header:*/

$('4-main.html').ready(function() {
    $("#toggle_header").click(function() {
        $("header").toggleClass("red green");
    });
});