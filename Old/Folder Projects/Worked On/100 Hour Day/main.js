let hour = 0;
let minute = 0;
let second = 0;


// for (var i = 0; i < 1440; i++) {
// 	if (14.24)
// }
// process.stdout.write('\033c');


var mainLoop = setInterval(function() {
	let date = new Date();
	let time = date.toString().substring(16, 24);

	second++;

	if (second >= 100) {
		second = 0;
		minute++;
	}

	if (minute >= 100) {
		minute = 0;
		hour++;
	}

	if (hour >= 100) {
		hour = 0;
	}

	secondOut = `${second}`;
	minuteOut = `${minute}`;
	hourOut = `${hour}`;

	if (second < 10) {
		secondOut = `0${second}`;
	}
	if (minute < 10) {
		minuteOut = `0${minute}`;
	}
	if (hour < 10) {
		hourOut = `0${hour}`
	}

	process.stdout.write(`\x1b[0m\x1b[2J\n\n\
\x1b[32m\
Custom Time:      \x1b[0m${hourOut}:${minuteOut}:${secondOut}\n\
\x1b[31m\
Real Time:        \x1b[0m${time}\n\n`);
}, 86.4);