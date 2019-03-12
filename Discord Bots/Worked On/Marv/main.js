const fs = require(`fs`);
const Discord = require(`discord.js`);
const hrtime = require('process');
const client = new Discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
	console.log(`\n\n\n\n\n\n\n`);
	console.log(`Bot has started! \nUSERS: ${client.users.size} \nCHANNELS: ${client.channels.size} \nSERVERS: ${client.guilds.size}\n`);
	client.user.setActivity('marv.help');
})



// -----------------------------------------------------------------------------



client.on(`guildCreate`, guild => {
	console.log(`\n-----------------------------\nNew server joined! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}\n-----------------------------\n`);
});

client.on(`guildDelete`, guild => {
	console.log(`\n-----------------------------\nRemoved from server! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}\n-----------------------------\n`);
});



// -----------------------------------------------------------------------------



client.on(`message`, message => {
	if (message.author.bot) return;

	console.log(`${message.guild.name}  ██  #${message.channel.name}  ██  ${message.author.username}: ${message.content}`);

	var sent = [];
	var serverSettings;
	var includesSCP = false;
	var includesCommand = false;
	var splitMessage = message.content.split(" ");
	var finalDesc = [];
	var object = {};
	var done = false;
	let final = new Discord.RichEmbed()
	.setColor(`#000000`)
	.setAuthor(`Marv`, `https://images.discordapp.net/avatars/538173713162567690/07187402dab82f0fd34348a0a5202ecc.png?size=512`, `https://discordapp.com/api/oauth2/authorize?client_id=554490018752626708&permissions=8&scope=bot`);

	try {
		serverSettings = fs.readFileSync(`./settings/${message.guild.name}.json`, (err) => {
	        	if (err) throw err;
	        });
		serverSettings = JSON.parse(serverSettings);
	}
	catch(err) {
		serverSettings = { SCPPrefix: true };
	}

	// -----------------------------------------------------------------------------

	if (message.content.startsWith("marv.help")) {
		includesCommand = true;
		final.setTitle('__**Here are all of my commands!**__')
	        .setDescription('*Arguments must be seperated with a comma and space or it will return an error.*')
	        .addField('General', '```\nhelp\ntoggleprefix\nstats```');
	}

	else if (message.content.startsWith("marv.toggleprefix")) {
		includesCommand = true;
		if (serverSettings.SCPPrefix == true) {
			serverSettings["SCPPrefix"] = false;
			final.setTitle('__**The prefix has been turned off!**__')
			.setDescription('Marv will now pick up on only numbers, (001) instead of numbers with the prefix (SCP-001).\nTales still require the \'TALE-\' prefix to work.');
		}
		else {
			serverSettings.SCPPrefix = true;
			final.setTitle('__**The prefix has been turned on!**__')
			.setDescription('Marv will now only pick up on numbers with a prefix (SCP-001).');
		}
	}

	else if (message.content.startsWith("marv.stats")) {
		includesCommand = true;
        	final.setTitle('BOT STATS')
        	.setDescription(`**Server Count** - ${client.guilds.size}\n**Channel Count** - ${client.channels.size}\n**User Count** - ${client.users.size}`);
	}

	// -----------------------------------------------------------------------------

	else {
		if (serverSettings.SCPPrefix == true) {
			for (var i = 0; i < splitMessage.length; i++) {
				if (splitMessage[i].toUpperCase().startsWith("TALE-")) {
					finalDesc.push(`[${splitMessage[i].substring(5).split("-").join(" ")}](http://www.scp-wiki.net/${splitMessage[i].substring(5)})`);
					includesSCP = true;
				}

				if (splitMessage[i].toUpperCase().startsWith("SCP-")) {
					finalDesc.push(`[${splitMessage[i].toUpperCase()}](http://www.scp-wiki.net/${splitMessage[i]})`);
					includesSCP = true;
				}
			}
		}
		else {
			for (var i = 0; i < splitMessage.length; i++) {
				if (splitMessage[i].toUpperCase().startsWith("TALE-")) {
					finalDesc.push(`[${splitMessage[i].substring(5).split("-").join(" ")}](http://www.scp-wiki.net/${splitMessage[i].substring(5)})`);
					includesSCP = true;
				}
			}

			for (var i = 5000; i >= 0; i--) {
				if (!done) {
					if (i < 10) {
						i = `00${i}`;
					}
					else if (i < 100) {
						i = `0${i}`;
					}

					if (message.content.toUpperCase().includes(`${i}`)) {
						finalDesc.push(`[SCP-${i}](http://www.scp-wiki.net/scp-${i})`);
						done = true;
						includesSCP = true;
					}
				}
			}
		}
	}

	// -----------------------------------------------------------------------------

	if (includesSCP) {
		final.setDescription(finalDesc.join("\n"));
		message.channel.send(final);
	}
	else if (includesCommand) {
		message.channel.send(final);
	}

	// -----------------------------------------------------------------------------



	let JSONObject = JSON.stringify(serverSettings);
	fs.writeFileSync(`./settings/${message.guild.name}.json`, JSONObject, (err) => {
		if (err) throw err;
	});
});



// -----------------------------------------------------------------------------



client.login(process.argv[2]);