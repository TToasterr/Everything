const fs = require(`fs`);
const request = require(`request`);
const Discord = require(`discord.js`);
const client = new Discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
	console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
	console.log(`RADON IS LIVE\nOBSERVABLE USERS: ${client.users.size}\nOBSERVABLE CHANNELS: ${client.channels.size}\nOBSERVED SERVERS: ${client.guilds.size}\n`);
	client.user.setActivity(`rd.help`);
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



// -----------------------------------------------------------------------------



client.on(`message`, message => {
	if (message.author.bot) return;
	// time and final defining
	let entire = message.content.toLowerCase();
	// let date = new Date();
	// let time = date.toString().substring(16, 24);
	let final = new Discord.RichEmbed()
		.setColor(`#FF0000`);


	// -----------------------------------------------------------------------------


	// variable defining
	var command = entire.split(` `)[0];
	var args = entire.slice(command.length).split(`, `);
	var command;
	var prefix;
	// console.log(entire);
	// if (!client.defaultCommands.has(commandName) && !client.tCommands.has(commandName) && !client.jCommands.has(commandName) && !client.nCommands.has(commandName) && !client.lCommands.has(commandName)) return;


	// final.setAuthor(`Radon`, profPic, invLink);


	if (entire.startsWith(`pass the `) && (entire.includes(`juul`) || entire.includes(`joule`) || entire.includes(`jewel`))) {
		message.channel.send(`${message.author.username} passed the ${entire.split(' ')[2]} to ${entire.split(' ')[3]}`);
		console.log("juul passed");
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

	if (entire.startsWith(`rdn.latestvid`)) {
		request('https://www.youtube.com/channel/UCJMh6yv37R-1G_OyvFsr0MQ?', function(error, response, body) {
			console.log('error: ', error);
			console.log('body: ', `${body}`.split('<h3 class="yt-lockup-title ">')[1].split('href="')[1].split('"')[0]);
			message.channel.send('https://www.youtube.com' + `${body}`.split('<h3 class="yt-lockup-title ">')[1].split('href="')[1].split('"')[0]);
		});
		console.log("latest LTJN video gotten");
	}
});

client.on('error', console.error);



// -----------------------------------------------------------------------------



const token = fs.readFileSync(`H:/Misc/radontoken.txt`, (err) => {
	if (err) console.log(`Error reading token!\n$ {err}`);
});
client.login(token.toString());