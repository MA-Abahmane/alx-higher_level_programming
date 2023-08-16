#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */

const dict = require('./101-data.js').dict;

newDict = {};

/** for each key get its value and save it in 'newKey' */
for (const key in dict) {
  const newKey = dict[key];

  /** if 'newKey' is not present as a key in our dictionary; set it */
  if (!newDict[newKey]) {
    newDict[newKey] = [];
  }

  /** if exists, add the key of the given dict as a value for our dicts key */
  newDict[newKey].push(key);
}

console.log(newDict);
