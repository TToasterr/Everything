const fs = require(`fs`);
const request = require(`request`);
const randomImage = require(`random-puppy`);
const Discord = require(`discord.js`);
const client = new Discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
	console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
	console.log(`RADON IS LIVE\nOBSERVABLE USERS: ${client.users.size}\nOBSERVABLE CHANNELS: ${client.channels.size}\nOBSERVED SERVERS: ${client.guilds.size}\n`);
	client.user.setActivity(`*hits my kids*`);
});

// -----------------------------------------------------------------------------

client.on(`guildCreate`, guild => {
	console.log(`\nNEW SERVER OBSERVED: ${guild.name}\nNEW USERS OBSERVABLE: ${guild.memberCount}\n`);
});

client.on(`guildDelete`, guild => {
	console.log(`\nLOST SIGHT OF ${guild.name}\nOBSERVABLE USERS LOST: ${guild.memberCount}`);
});



// -----------------------------------------------------------------------------



// reloadbot();
var profPic = `https://cdn.discordapp.com/attachments/539116623261466635/555604369068785664/600px-Radiation_warning_symbol.svg.png`;
var invLink = `https://discordapp.com/api/oauth2/authorize?client_id=555556786908954624&permissions=8&scope=bot`;

var lastJonathanMessage;
var lastToasterMessage;
var lastNateMessage;



// -----------------------------------------------------------------------------

//your mom xd

client.on(`message`, message => {
	if (message.author.bot) return;
	let entire = message.content.toLowerCase();
	let final = new Discord.RichEmbed()
		.setColor(`#FF0000`);


	// -----------------------------------------------------------------------------


	// variable defining
	var command = entire.split(` `)[0];
	var args = entire.slice(command.length).split(`, `);
	var command;
	var prefix;





	if ((/pass the (juul|joule|jewel) to (.+)/g).test(entire)) {
		message.delete();

		message.channel.send(`${message.author.username} passed the ${entire.split(' ')[2]} to ${entire.split(' ')[4]}`);
		console.log("juul passed");
	}

	else if ((/pass the (juul|joule|jewel) (.+)/g).test(entire)) {
		message.delete();

		message.channel.send(`${message.author.username} requested the ${entire.split(' ')[2]} from ${entire.split(' ')[3]}`);
		console.log("juul requested");
	}

	if ((/(hit|hits) the (juul|joule|jewel|jouuwel)/g).test(entire)) {
		message.delete();

		message.channel.send(`${message.author.username} took a massive hit of the ${entire.split(' ')[2]}.`);
		switch (entire.split(" ")[2]) {
			case "juul":
				message.channel.send(":dash::dash::dash:");
				break;
			case "joule":
				message.channel.send(":zap::zap::zap:");
				break;
			case "jewel":
				message.channel.send(":ring::ring::ring:");
				break;
			case "jouuwel":
				message.channel.send(":dash::zap::ring:");
				break;
		}
		console.log(`${entire.split(' ')[2]} hit`);
	}

	if (entire.includes("hits my kids")) {
		message.channel.send(`${message.author.username} took a massive hit from CPS.`);
	}



	if (entire.startsWith(`rdn.suggest`)) {
		let suggestion = entire.slice(`rd.suggest `.length);

		let toaster = client.fetchUser(`184474965859368960`).then(toaster => {
			toaster.send(`${message.author.username} suggests:\n\`${suggestion}\``);
		});
		console.log("suggestion made");
	}



	if (entire.startsWith('rdn.diceroll')) {
		let sides = entire.split(" ")[1];
		let roll = Math.floor(Math.random() * (parseInt(sides) - 1)) + 1;
		message.channel.send(roll);
		console.log(`${message.author.username} rolled a dice`);
	}



	if (entire.includes(`thank you `)) {
		message.channel.send('very cool');
		console.log("thank you [someone] very cool");
	}









	if (entire.startsWith('meme')) {
		message.delete();
		randomImage('dankmemes').then(url => {
			message.channel.send(url);
		});
	}

	if (entire.startsWith('cursedimage')) {
		message.delete();
		randomImage('cursedimages').then(url => {
			message.channel.send(url);
		});
	}

	if (entire.startsWith('eyebleach')) {
		message.delete();
		randomImage('eyebleach').then(url => {
			message.channel.send(url);
		});
	}









	if (entire.startsWith('google')) {
		message.channel.send("Oh god, what are you googling?").then(msg => {
			msg.delete(2000);
		}).catch(err => {
			console.log(err);
		});

		message.delete();

		let collector = new Discord.MessageCollector(message.channel, m => m.author.id == message.author.id, {
			time: 30000
		});

		collector.on('collect', message => {
			request(`https://www.google.com/search?&q=${message.content.replace(/( )/g, '+')}&tbm=isch`, function(error, response, body) {
				message.channel.send(`${body}`.split('" jsaction="load:str.tbn"')[0].split('src="')[1].split('" width="')[0]);
			});
			message.delete();
			collector.stop();
		});
	}









	if (entire.includes('oh god oh fuck')) {
		message.channel.send("*femur breaker noises start*").then(msg => {
			let i = 0;
			let editLoop = setInterval(function() {
				if (i <= 9) {
					msg.edit(`${msg.content}\n*femur breaker noises continue*`);
				}
				else {
					msg.edit(`${msg.content}\n*femur breaker noises stop*`);
					setTimeout(function() {
						message.channel.send(`**SCP-106 HAS BEEN RECONTAINED**`);
					}, 1250);
					msg.delete(5000);
					clearInterval(editLoop);
				}

				i++;
			}, 1250);
		});
	}



	// if (entire.includes(`jonk`)) {
	// 	message.channel.send(`jonk more like \'${lastJonathanMessage}\'`);
	// }
	//
	// if (entire.includes(`toaster`)) {
	// 	message.channel.send(`toaster more like '${lastToasterMessage}'`);
	// }
	//
	// if (entire.includes(`nate`)) {
	// 	message.channel.send(`nate more like '${lastNateMessage}'`);
	// }



	if (entire.startsWith(`rdn.latestvid`)) {
		request('https://www.youtube.com/channel/UCJMh6yv37R-1G_OyvFsr0MQ?', function(error, response, body) {
			// console.log('error: ', error);
			// console.log('body: ', `${body}`.split('<h3 class="yt-lockup-title ">')[1].split('href="')[1].split('"')[0]);
			message.channel.send('https://www.youtube.com' + `${body}`.split('<h3 class="yt-lockup-title ">')[1].split('href="')[1].split('"')[0]);
		});
		console.log("latest LTJN video gotten");
	}


	//if (entire.startsWith(`rdn.surprise`)) {
	//	message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
	//	console.log(`${message.author.username} was surprised.`);
	// }




	//JONK'S STUFF AHEAD
	//ABANDON ALL YE WHO ENTER HERE

	let randomNum = Math.floor(Math.random() * 250);
	if (randomNum == 0) {
		message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ');

		setTimeout(function() {
			message.channel.send('gottem xd');
		}, 500);

		console.log(`${message.author.username} was gotten.`);
	}

	if (entire.includes(`no no u`)) {
		message.channel.send(`__***:o***__`)
	}
	else if (entire.includes(`no u`)) {
		message.channel.send(`*:O*`)
	}





	// if (message.author.username == "JONKKKK") {
	// 	lastJonathanMessage = message.content;
	// }
	//
	// if (message.author.username == "Toaster") {
	// 	lastToasterMessage = message.content;
	// }
	//
	// if (message.author.username == "GoldenPot8o") {
	// 	lastNateMessage = message.content;
	// }

	// if ((/(wow )(.+)( is gay xd)/g).test(entire)) {
	// 	message.channel.send(`haha yes i agree ${entire.split(" ")[1]} is v homosexual`);
	// 	// console.log("aaaa");
	// }
});

client.on('error', console.error);



// -----------------------------------------------------------------------------



const token = fs.readFileSync(`H:/Misc/radontoken.txt`, (err) => {
	if (err) console.log(`Error reading token!\n$ {err}`);
});
client.login(token.toString());