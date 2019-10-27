let sleep = require('sleep');

let numbersBeforeFoundList = [];
let averageNumbersBeforeFound = 0;

function main() {
	let unfound = true;
	let numbersBeforeFound = 0;

	while (unfound) {
		let randomNumber1 = Math.floor(Math.random() * 100);

		if (randomNumber1 == 0) {
			unfound = false;

			numbersBeforeFoundList.push(numbersBeforeFound);
			for (var i = 0; i < numbersBeforeFoundList.length; i++) {
				averageNumbersBeforeFound += numbersBeforeFoundList[i];
			}
			averageNumbersBeforeFound = averageNumbersBeforeFound / numbersBeforeFoundList.length;

			console.log(`\nNumbers before found: ${numbersBeforeFound}\nAverage: ${averageNumbersBeforeFound}`);
			main()
		}
		else {
			numbersBeforeFound++;
		}
	}
}

main();