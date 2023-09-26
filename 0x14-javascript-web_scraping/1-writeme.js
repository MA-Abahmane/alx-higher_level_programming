#!/usr/bin/node
/** A script that writes a string to a file. */

// import the fs module specialized in file manipulation
const Fs = require('fs');

// get the filename and file string then write the string to the file in utf-8
Fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (error) {

    // if an error occurred; return error message
    if (error)
    {
        console.log(error);
        return;
    }
});
