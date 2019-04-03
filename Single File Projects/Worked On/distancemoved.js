var distance = 0;
var seconds = 0;

var main = setInterval(function() {
	distance += 0.562402912544;
	console.log(Math.round(distance) + " km");
}, 0);