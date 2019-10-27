const request = require(`request`);

request('https://newmexicoconsortium.org/', function(error, response, body) {
	console.log(error);
	console.log("\n\n");
	console.log(`${body}`.split(`class="vc_custom_heading">`)[1].split("</h1>")[0]);
	console.log(`${body}`.split(`class="vc_custom_heading">`)[2].split("</h5>")[0]);
});