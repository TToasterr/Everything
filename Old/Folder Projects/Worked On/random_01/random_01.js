const sleep = require("sleep");

let l1000 = 0;
let g1000 = 0;

while (true) {
	let coef = Math.round((0.01 + 0.99 / (1 - Math.random())) * 100) / 100;
	let coef2 = Math.round(coef * 100);
	let testNum = 20000;
	let color;

	if (coef2 < testNum) {
		l1000++;
		color = '\x1b[31m';
	}
	else {
		g1000++;
		color = '\x1b[32m';
	}

	process.stdout.write(`\x1b[0m\x1b[2J\n\n\
${color}\
${coef}\n\
${coef2}\n\
\n\
\x1b[31m\
${l1000} less than ${testNum/1000}\n\
\x1b[32m\
${g1000} greater than ${testNum/1000}\n\
\n\
\x1b[36m\
${Math.round(l1000 / g1000)} \
\x1b[31m\
Less than ${testNum/1000} \
\x1b[0m\
per \
\x1b[36m\
1 \
\x1b[32m\
Greater than ${testNum/1000}\n\
\x1b[0m\
(Roughly)\n\
\n`);
	// sleep.msleep(50);
}