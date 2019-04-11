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
	console.log(`\nNEW SERVER VISIBLE: ${guild.name}\nNEW USERS VISIBLE:  ${guild.memberCount}\n`);
});

client.on(`guildDelete`, guild => {
	console.log(`\nLOST VISIBILITY ON ${guild.name}\nUSERS LOST: ${guild.memberCoutn}`);
})

// -----------------------------------------------------------------------------

client.on(`message`, message => {
	if (message.author.bot) return;

	let content = message.content;
	let splitMessage = content.split(` `);
	let serverSettings;
	let serverPrefix;
	let serverRandom;
	let serverMarv;
	let serverIdeas;

	// -----------------------------------------------------------------------------

	client.commands = new Discord.Collection();
	const commandFiles = fs.readdirSync(`./commands`).filter(file => file.endsWith(`.js`));
	for (let file of commandFiles) {
		let command = require(`./commands/${file}`);
		client.commands.set(command.name, command);
	}

	// -----------------------------------------------------------------------------

	try {
		let autoResponses = fs.readFileSync(`./autoresponders/${message.guild.name}.json`, (err) => {
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
		serverSettings = fs.readFileSync(`./servers/${message.guild.name}Settings.json`, (err) => {
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
	}

	// -----------------------------------------------------------------------------

	if (!content.startsWith(serverPrefix)) return;

	// -----------------------------------------------------------------------------


});