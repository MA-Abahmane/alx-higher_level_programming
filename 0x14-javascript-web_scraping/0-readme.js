#!/usr/bin/node
/** A script that reads and prints the content of a file. */

// import the fs module specialized in file manipulation
const Fs = require('fs');

// Read the contents of a given file in utf-8
Fs.readFile(process.argv[2], 'utf-8', function (error, content) {

    // if an error occurred; return error message
    if (error)
    {
        console.log(error);
        return
    }
    // if all went well; print the contents read
    console.log(content);
});
