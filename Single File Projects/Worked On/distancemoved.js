var distance = 0;
var seconds = 0;

var main = setInterval(function() {
	distance += 0.562402912544;
	process.stdout.write(Math.round(distance) + " km\033[0G");
}, 0);