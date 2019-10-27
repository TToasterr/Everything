// School starts at 7:50
// School ends at 14:35
// School is 24300 seconds
// School is out for 62100 seconds

const s = require("sleep");
const mmnt = require("moment");


// let schoolStartTime = mmnt("7:50:00", "HH:mm:ss");
// let schoolCurrentTime = mmnt().format("HH:mm:ss");
let schoolEndTime = mmnt("14:35:00", "HH:mm:ss"); //get when school ends
mmnt.relativeTimeThreshold("s", 1000000000000000000);
mmnt.relativeTimeThreshold("ss", 0);

while (1) {
	let output = schoolEndTime.fromNow(); //output is the time when school ends compared to now
	let percentOfTotal;
	let end;
	let end2;
	if (output.endsWith(" ago")) { //if school has ended
		percentOfTotal = output.split(" ")[0] / 621000 * 1000;
		percentOfSecond = output.split(" ")[0] / 28500 * 100;
		end = "Free Time:";
		end2 = "Awake Time:"
	}
	else {
		percentOfTotal = output.split(" ")[1] / 24300 * 1000;
		percentOfSecond = 0;
		end = "School:";
		end2 = "N/A"
	}

	process.stdout.write(`\x1b[2J\x1b[1m\x1b[4m\n\n\n\n${end}\x1b[0m\n${Math.round(percentOfTotal * 100000) / 100000}%\n\n`);

	for (var i = 0; i < 100; i++) {
		if (i < Math.floor(percentOfTotal)) {
			process.stdout.write('█');
		}
		else {
			process.stdout.write('░');
		}
	}

	process.stdout.write(`\n\n\n\x1b[1m\x1b[4m${end2}\x1b[0m\n${Math.round(percentOfSecond * 100000) / 100000}%\n\n`);

	for (var i = 0; i < 100; i++) {
		if (i < Math.floor(percentOfSecond)) {
			process.stdout.write('█');
		}
		else {
			process.stdout.write('░');
		}
	}

	console.log("\n\n\n\n" + percentOfTotal);
	console.log(percentOfSecond);
	console.log(output);

	s.sleep(1);
}