let hour = 0;
let minute = 0;
let second = 0;

var secondLoop = setInterval(function() {
	second++;

	if (second >= 100) {
		second = 0;
		minute++;
	}

	if (minute >= 100) {
		minute = 0;
		hour++;
	}

	let date = new Date();
	let time = date.toString().substring(16, 24);

	console.log(`\n\n${hour}:${minute}:${second} --- ${time}`);
}, 86.4);