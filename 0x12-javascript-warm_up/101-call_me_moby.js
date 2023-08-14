#!/usr/bin/node
/* a function that executes x times a function. */

function MyFunc (x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}

/* Update function callMeMoby */
exports.callMeMoby = MyFunc;
