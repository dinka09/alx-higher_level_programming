#!/usr/bin/node
// print an argument checking if the argument can be converted to a number

if (isNaN(process.argv[2])) {
    console.log('Not a number');
} else {
    console.log('My number: ' +  parseInt(process.argv[2]));
};
