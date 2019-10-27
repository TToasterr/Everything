const fs = require("fs"); //get filesystem
const sleep = require("sleep"); //get sleep

const readFile = fs.readFileSync(`./${process.argv[2]}`); //read the .toast file
let file = `${readFile}`; //make it a string
let splitFile = file.split("\n"); //split it by linebreak
let indentLevel = 0;

console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n"); //empty console

file = file.replace(/\t/g, '');



// importing modules
file = file.replace(/(import )(.*)( as )(.*)/g, /let $4 = require('$2')/);
file = file.replace(/(import )(.*)/g, /let $2 = require($2)/);

// sleep, setinterval, functions
file = file.replace(/(sleep )(\d*)/g, /sleep.msleep($2)/);
file = file.replace(/([A-z]*\(\))( repeating with a delay of )(\d*)/g, /setInterval($1, $3)/);
file = file.replace(/([A-z]*\(\)):((\n\t.+)+)/g, /function $1 {$2\n}/);

// defining variables
file = file.replace(/ be /g, " = ");
file = file.replace(/ a /g, " ");
file = file.replace(/ the result of the /g, " ");
file = file.replace(/ function/g, "");

// conversion and substrings
file = file.replace(/(string)(\()(\w+)(\))/g, /$3.toString()/);
file = file.replace(/(\[)(\d+,\d+)(\])/g, /.substring($2)/);
file = file.replace(/(int)(\()(["'`]\w+["'`])(\))/g, /$3.parseInt()/);

// comparing variables, conditions
file = file.replace(/ is exactly /g, " === ");
file = file.replace(/ is not /g, " != ");
file = file.replace(/ is less than or equal to /g, " <= ");
file = file.replace(/ is greater than or equal to /g, " >= ");
file = file.replace(/ is less than /g, " < ");
file = file.replace(/ is greater than /g, " > ");
file = file.replace(/ is /g, " == ");
file = file.replace(/ and /g, " && ");
file = file.replace(/ or /g, " || ");

// if, while, for, print, and semicolons
// for (var i = 0; i < 500; i++) {
file = file.replace(/((if |while )(.+) ({))(((\r\n+).+)+\r\n})/g, /$2($3) $4$5/);
file = file.replace(/(for )([A-z])( in )(range\()(.+)(\)):((\r\n\t.+)+)/g, /$1(var $2 = 0; $2 < $5; $2\++) {$7/ + '\n' + /}/);
file = file.replace(/(print )(.+)/g, /console.log($2);/);
file = file.replace(/print/g, "console.log();")
file = file.replace(/[\w"'`\]\)]+$/gm, /$&;/);
// }

// clean up the / and \s
file = file.replace(/\//g, "");
file = file.replace(/\\/g, "");



console.log(file);

console.log("\n\n------------------------------------\n\n");

eval(file);