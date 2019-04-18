const fs = require(`fs`);
const Discord = require(`discord.js`);
const client = new Discord.Client();





// -----------------------------------------------------------------------------





client.once(`ready`, () => {
	console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
	console.log(`SILICON IS RUNNING\nVISIBLE USERS: ${client.users.size}\nVISIBLE SERVERS: ${client.guilds.size}\n`);
	client.user.setActivity(`slc.help`);
});





// -----------------------------------------------------------------------------





client.on(`guildCreate`, guild => {
	console.log(`\n${guild.name} HAS MADE CONTACT\nNEW USERS VISIBLE:  ${guild.memberCount}\n`);
});

client.on(`guildDelete`, guild => {
	console.log(`\nLOST CONTACT WITH ${guild.name}\nUSERS LOST: ${guild.memberCount}`);
})





// -----------------------------------------------------------------------------





client.on(`message`, message => {
	if (message.author.bot) return;

	let content = message.content;
	let splitMessage = content.split(` `);
	let channel = message.channel;
	let channelName = channel.name;
	let channelID = channel.id;
	let guild = message.guild;
	let guildName = guild.name;

	let serverSettings;
	let serverPrefix;
	let serverRandom;
	let serverMarv;
	let serverIdeas;
	let serverDNDChannels;





	// -----------------------------------------------------------------------------





	client.commands = new Discord.Collection();
	const commandFiles = fs.readdirSync(`./commands`).filter(file => file.endsWith(`.js`));
	for (let file of commandFiles) {
		let command = require(`./commands/${file}`);
		client.commands.set(command.name, command);
	}





	// -----------------------------------------------------------------------------





	try {
		let autoResponses = fs.readFileSync(`./autoresponders/${guildName}.json`, (err) => {
			if (err) throw err;
		});
		autoResponses = JSON.parse(autoResponses);
		let keys = Object.keys(autoresponses);
		for (let key of keys) {
			if (content.includes(key)) {
				message.channel.send(autoResponses[key]);
			}
		}
	}
	catch (err) {
		let nothing;
	}


	try {
		serverSettings = fs.readFileSync(`./servers/${guildName}Settings.json`, (err) => {
			if (err) throw err;
		});
		serverSettings = JSON.parse(serverSettings);

		try {
			serverPrefix = serverSettings[`prefix`];
		}
		catch (err) {
			serverPrefix = `si.`;
		}

		try {
			serverRandom = serverSettings[`random`];
		}
		catch (err) {
			serverRandom = false;
		}

		try {
			serverMarv = serverSettings[`marv`];
		}
		catch (err) {
			serverMarv = false;
		}

		try {
			serverDNDChannels = serverSettings[`DNDChannels`];
		}
		catch (err) {
			serverDNDChannels = [];
		}
	}
	catch (err) {
		serverPrefix = `si.`;
		serverRandom = false;
		serverMarv = false;
		serverDNDChannels = [];
	}





	// -----------------------------------------------------------------------------





	if (!content.startsWith(serverPrefix)) return;





	// -----------------------------------------------------------------------------







	// commands go here







	// -----------------------------------------------------------------------------





	serverSettings = JSON.stringify(serverSettings);
	fs.writeFileSync(`./servers/${guildName}Settings.json`, serverSettings, (err) => {
		if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
	});
});