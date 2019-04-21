const fs = require(`fs`);
const discord = require(`discord.js`);
const client = new discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
	console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
	console.log(`SILICON IS RUNNING\nVISIBLE USERS: ${client.users.size}\nVISIBLE SERVERS: ${client.guilds.size}\n`);
	client.user.setActivity(`si.help`);
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
	let commandName = splitMessage[0];
	let args = content.slice(commandName.length).split(`, `);
	let pic = `https://cdn.discordapp.com/attachments/203685947097874433/568563045249450047/Silicon.png`;
	let invite = `https://discordapp.com/api/oauth2/authorize?client_id=568569358004256769&permissions=8&scope=bot`;

	let author = message.author;
	let authorName = author.username;
	let channel = message.channel;
	let channelName = channel.name;
	let channelID = channel.id;
	let guild = message.guild;
	let guildName = guild.name;

	let date = new Date();
	let time = date.toString().substring(16, 24);

	let serverSettings;
	let serverPrefix;
	let serverRandom;
	let serverMarv;
	let serverDNDChannels;

	let final = new discord.RichEmbed()
		.setColor(`#383838`)
		.setAuthor(`Silicon`, pic, invite);



	// -----------------------------------------------------------------------------



	client.commands = new discord.Collection();
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
		serverDNDChannels = {
			inCharacter: [],
			outOfCharacter: []
		};

		serverSettings = {
			prefix: serverPrefix,
			random: serverRandom,
			marv: serverMarv,
			DNDChannels: serverDNDChannels
		}
	}



	// -----------------------------------------------------------------------------



	if (serverRandom) {
		let commands = message.client.commands.map(command => command);
		for (var i = 0; i < commands.length; i++) {
			if (commands[i].category == `random` && commands[i].autoExec) {
				commands[i].execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final);
			}
		}
	}

	if ((serverDNDChannels[`inCharacter`].includes(channelID) || serverDNDChannels[`outOfCharacter`].includes(channelID))) {
		let commands = message.client.commands.map(command => command);
		for (var i = 0; i < commands.length; i++) {
			if (commands[i].category == `dnd` && commands[i].autoExec) {
				commands[i].execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final);
			}
		}
	}



	// -----------------------------------------------------------------------------



	// console.log(content);
	if (!content.startsWith(serverPrefix)) return;
	commandName = commandName.slice(serverPrefix.length);
	if (!client.commands.has(commandName)) return;
	let command = client.commands.get(commandName);
	let finalDescription;



	if (command.args && (!args || args == ``)) {
		final.setTitle(`__**Whoops!**__`);
		finalDescription = [`You didn't provide any arguments.`];

		if (command.usage !== ``) {
			finalDescription.push(``);
			finalDescription.push(`__Usage:__`);
			finalDescription.push(`${serverPrefix}${commandName} ${command.usage}`);
		}

		final.setDescription(finalDescription.join("\n"));
		channel.send(final);
		return console.log(`[${time}] ${authorName} tried to use ${commandName} without any arguments.`);
	}

	if (command.guildOnly && channel.type !== `text`) {
		final.setTitle(`__**Whoops!**__`)
			.setDescription(`That command only works in servers!`);

		channel.send(final);
		return console.log(`[${time}] ${authorName} tried to use ${commandName} outside of a server.`);
	}

	if (command.category == `random` && !serverRandom && !command.passThrough) {
		final.setTitle(`__**Whoops!**__`)
			.setDescription(`That command is in the \`random\` category, which you don't have enabled!\nPlease enable the category to use the command.`);

		channel.send(final);
		return console.log(`[${time}] ${authorName} tried to use ${commandName} but didnt have the Random module enabled.`);
	}

	if (command.category == `marv` && !serverMarv && !command.passThrough) {
		final.setTitle(`__**Whoops!**__`)
			.setDescription(`That command is in the \`marv\` category, which you don't have enabled!\nPlease enable the category to use the command.`);

		channel.send(final);
		return console.log(`[${time}] ${authorName} tried to use ${commandName} but didnt have the Marv module enabled.`);
	}

	if (command.category == `dnd` && !serverDNDChannels[`inCharacter`].includes(channelID) && !serverDNDChannels[`outOfCharacter`].includes(channelID) && !command.passThrough) {
		final.setTitle(`__**Whoops!**__`)
			.setDescription(`That command is only available in channels with DND enabled!\nPlease make this channel a DND channel to use the command.`);

		channel.send(final);
		return console.log(`[${time}] ${authorName} tried to use ${commandName} outside of a DND channel.`);
	}



	// -----------------------------------------------------------------------------





	try {
		command.execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final);
	}
	catch (err) {
		final.setTitle(`__**Whoops!**__`)
			.setDescription(`There was an error executing that command!\nThe bot owner has been notified.`);

		channel.send(final);

		let client = message.channel.client;
		let toaster = client.fetchUser(`184474965859368960`).then(toaster => {
			toaster.send(`${message.author.username} got an error using the ${commandName} command. \nCheck console my guy!`);
		});
		throw err;
	}





	// -----------------------------------------------------------------------------
});


const token = fs.readFileSync(`H:/Misc/SiliconToken.txt`, (err) => {
	if (err) console.log(`Error reading token!\n$ {err}`);
});
client.login(token.toString());