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

// let sleep_time = mmnt("22:00:00", timeFormat);
// let wake_time = mmnt("6:50:00", timeFormat);
// let wake_time = mmnt("7:50:00", timeFormat);
// let sleep_time = mmnt("14:35:00", timeFormat);
let timeFormat = "HH:mm:ss";
let x = 0;

// -----------------------------------------------------------------------------

while (true) {
	process.stdout.write("\x1b[2J");

	let wake_time = mmnt("7:50:00", timeFormat);
	let sleep_time = mmnt("14:35:00", timeFormat);
	let until_sleep = mmnt(sleep_time).fromNow();
	let after_wake, until_sleep_clean, after_wake_clean, statement, day_length, sleep_length, percent_left, percent_through;

	// -----------------------------------------------------------------------------

	if (!until_sleep.endsWith("seconds")) {
		until_sleep = mmnt(sleep_time).fromNow();
		after_wake = mmnt(wake_time.add(1, 'd')).fromNow();

		until_sleep_clean = parseInt(until_sleep.split(" ")[0]);
		after_wake_clean = parseInt(after_wake.split(" ")[1]);

		day_length = (until_sleep_clean + after_wake_clean);
		sleep_length = secs_in_day - day_length;

		percent_through = Math.round((until_sleep_clean / day_length) * 1000) / 10;
		percent_left = Math.round((after_wake_clean / day_length) * 1000) / 10;

		statement = `Percent of time until school starts left:     ${percent_left}%\nPercent through that time:                    ${percent_through}%`;
	}
	else {
		until_sleep = mmnt(sleep_time).fromNow();
		after_wake = mmnt(wake_time).toNow();

		until_sleep_clean = parseInt(until_sleep.split(" ")[1]);
		after_wake_clean = parseInt(after_wake.split(" ")[1]);

		day_length = (until_sleep_clean + after_wake_clean);
		sleep_length = secs_in_day - day_length;

		percent_left = Math.round((until_sleep_clean / day_length) * 1000) / 10;
		percent_through = Math.round((after_wake_clean / day_length) * 1000) / 10;

		statement = `Percent of school left:     ${percent_left}%\nPercent through school:     ${percent_through}%`;
	}

	// -----------------------------------------------------------------------------


	process.stdout.write(`\n\n${statement}\n`);
	for (var i = 0; i < 100; i++) {
		if (i < Math.round(percent_through)) {
			process.stdout.write('█');
		}
		else {
			process.stdout.write('░');
		}
	}


	// process.stdout.write('\n\n');
	// for (var i = 0; i < 7; i++) {
	// 	process.stdout.write(`\x1b[3${i}m`);
	// 	for (var o = 0; o < 100; o++) {
	// 		if (x == 115) {
	// 			x = 0;
	// 		}
	//
	// 		if (o < x - (i * i ^ i)) {
	// 			process.stdout.write('█');
	// 		}
	// 		else {
	// 			process.stdout.write('░');
	// 		}
	// 	}
	// 	process.stdout.write('\n');
	// }


	process.stdout.write(`\x1b[0m\n\n\nSchool end time:       ${until_sleep}\nSchool start time:     ${after_wake}\n\n`);

	// -----------------------------------------------------------------------------

	x++;
	s.msleep(500);
}