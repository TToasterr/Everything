// school starts at 7:50
// school ends at 14:35
// sleep starts at 10:00
// sleep ends at 6:45
// 86400 seconds in a day

const s = require("sleep");
const mmnt = require("moment");
const secs_in_day = 86400;

// -----------------------------------------------------------------------------

mmnt.relativeTimeThreshold("s", 1000000000000000000);
mmnt.relativeTimeThreshold("ss", 0);

let timeFormat = "HH:mm:ss";
let sleep_time = mmnt("22:00:00", timeFormat);
let wake_time = mmnt("6:50:00", timeFormat);
let school_start = mmnt("7:50:00", timeFormat);
let school_end = mmnt("14:35:00", timeFormat);

// -----------------------------------------------------------------------------

while (true) {

	process.stdout.write("\x1b[2J");

	let until_sleep = mmnt(sleep_time).fromNow();
	let after_wake = mmnt(wake_time).toNow().replace(/in (.+) seconds/g, "$1 seconds ago");

	let until_sleep_clean, after_wake_clean, statement, day_length, sleep_length, percent_left, percent_through;

	// -----------------------------------------------------------------------------

	if (!until_sleep.endsWith("seconds")) {
		until_sleep_clean = parseInt(until_sleep.split(" ")[0]);
		after_wake_clean = 0;

		let day_length = (until_sleep_clean + after_wake_clean);
		let sleep_length = secs_in_day - day_length;

		let percent_left = Math.round((until_sleep_clean / day_length) * 1000) / 10;
		let percent_through = Math.round((after_wake_clean / day_length) * 1000) / 10;

		statement = `You have ${percent_left}% left in the day, and\nYou are ${percent_through}% through the day.`;
	}
	else {
		until_sleep_clean = parseInt(until_sleep.split(" ")[1]);
		after_wake_clean = parseInt(after_wake.split(" ")[0]);

		let day_length = (until_sleep_clean + after_wake_clean);
		let sleep_length = secs_in_day - day_length;

		let percent_through = Math.round((until_sleep_clean / day_length) * 1000) / 10;
		let percent_left = Math.round((after_wake_clean / day_length) * 1000) / 10;

		statement = `You have ${percent_through}% left in the day, and\nYou are ${percent_left}% through the day.`;
	}

	// -----------------------------------------------------------------------------

	// console.log(`${day_length}\n${sleep_length}`);
	console.log(until_sleep);

	// -----------------------------------------------------------------------------


	process.stdout.write(`\n\n${statement}\n`);
	for (var i = 0; i < 100; i++) {
		if (i < Math.floor(percent_through)) {
			process.stdout.write('█');
		}
		else {
			process.stdout.write('░');
		}
	}


	process.stdout.write(`\n\n\nSchleemp Time is ${until_sleep}\nWaek Time was ${after_wake}\n\n`);
	console.log("\n\n\n");

	// -----------------------------------------------------------------------------

	s.sleep(1);
}