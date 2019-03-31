const fs = require("fs"); //get filesystem
const sleep = require("sleep"); //get sleep

const readFile = fs.readFileSync(`./${process.argv[2]}`); //read the .toast file
let file = `${readFile}`; //make it a string
let splitFile = file.split("\n"); //split it by linebreak
let indentLevel = 0;

console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n"); //empty console

// for (var line of splitFile) { //for each line in the file
// 	if (line.startsWith("let")) { //if the line starts with let (its defining a variable)
// 		if (line.includes("be the result of the")) { //if the line includes "be the result of the"
// 			line = line.replace("be the result of the", "="); //replace "be the result of the" with "="
// 			line = line.replace(" function", ""); //replace " function" with ";"
// 		}
// 		else { //else (if doesnt include "be the result of the")
// 			line = line.replace("be the result of", "="); //replace "be the result of" with "="
// 			line = line.replace("be", "="); //replace "be" with "="
// 		}
// 		// line = line + ";";
// 	}
//
// 	if (line.startsWith("if" || "while")) { //if the line ends with a colon (its a function, if statement, while statement, wtv)
// 		indentLevel += 1;
// 		line = line.replace("if ", "if (");
// 		line = line.replace(":", ") {");
//
// 		line = line.replace(/and/g, "&&");
// 		line = line.replace(/or/g, "||");
// 		line = line.replace(/is exactly/g, "===");
// 		line = line.replace(/is/g, "==");
// 	}
//
// 	while (!(line.startsWith("\t")) && (indentLevel > 0)) {
// 		indentLevel--;
// 		line = line;
// 	}
//
// 	if (line.startsWith(("\t" * indentLevel) + "print")) {
// 		line = line.replace("print ", "console.log");
// 		line = line.replace(/(["'`].+["'`])/g, /($&);/);
// 	}
//
// 	// while (!(line.startsWith("\t" * indentLevel)) && (indentLevel > 0)) {
// 	// 	indentLevel--;
// 	// 	line = line + "\n}";
// 	// }
//
// 	console.log(`${indentLevel} ${line}`);
//
// 	sleep.msleep(250);
// }

// file = file.replace(/(["'`].+["'`])/g, /($&);/);
file = file.replace(/(if )(.+)(:\n)(.+)/g, /$1($2) {\n$4\n}/);
file = file.replace(/(print )(["'`].+["'`])/g, /console.log($2);/);

console.log(file);