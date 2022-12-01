#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing size');
  } else {
    for (let i = 0; i < x; i++) {
      stringSquare = "";
    for(let j = 0; j < x; j++)
      stringSquare += "x"
    console.log(stringSquare);
  }
}
