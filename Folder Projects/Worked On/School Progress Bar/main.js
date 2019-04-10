// School starts at 7:50
// School ends at 14:35
// School is 24300 seconds
// School is out for 62100 seconds

const s = require("sleep");
const mmnt = require("moment");


// let schoolStartTime = mmnt("7:50:00", "HH:mm:ss");
// let schoolCurrentTime = mmnt().format("HH:mm:ss");
let schoolEndTime = mmnt("14:35:00", "HH:mm:ss");
mmnt.relativeTimeThreshold("s", 1000000000000000000);
mmnt.relativeTimeThreshold("ss", 0);

while (1) {
	let output = schoolEndTime.fromNow();
	let percentOfTotal;
	let end;
	if (output.endsWith(" ago")) {
		percentOfTotal = output.split(" ")[0] / 621000;
		end = "Free Time:";
	}
	else {
		percentOfTotal = output.split(" ")[0] / 24300;
		end = "School:";
	}

	process.stdout.write(`\x1b[2J\x1b[1m\x1b[4m${end}\x1b[0m\n${Math.round(percentOfTotal * 100000) / 100000}%\n\n`);

	for (var i = 0; i < Math.floor(percentOfTotal); i++) {
		process.stdout.write('█');
	}

	process.stdout.write('\n\n');

	s.sleep(1);
}