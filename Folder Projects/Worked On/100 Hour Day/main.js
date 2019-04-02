let hour = 0;
let minute = 0;
let second = 0;

let date = new Date();
let time = date.toString().substring(16, 24);


// for (var i = 0; i < 1440; i++) {
// 	if (14.24)
// }


var mainLoop = setInterval(function() {
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

	console.log(`\n\n${hour}:${minute}:${second}`);
}, 86.4);