const sleep = require("sleep");

let l1000 = 0;
let g1000 = 0;

while (true) {
	let coef = Math.round((0.01 + 0.99 / (1 - Math.random())) * 100) / 100;
	let coef2 = Math.round(coef * 100);

	if (coef2 < 1500) {
		l1000++;
	}
	else {
		g1000++;
	}

	console.log("\n-----------\n");
	console.log(coef);
	console.log(coef2);
	console.log();
	console.log(l1000);
	console.log(g1000);
	console.log(l1000 / g1000);
	sleep.msleep(50);
}