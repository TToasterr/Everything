const fs = require(`fs`); // install filesystems (reading/writing files)
const Discord = require(`discord.js`); // install discord.js (discord stuff)
const client = new Discord.Client(); // make a Discord client (just the bot itself)



// -----------------------------------------------------------------------------



client.once(`ready`, () => { // once the bot turns on
	console.log(`\n\n\n\n\n\n\n`); // partially empty the console
	console.log(`Bot has started! \nUSERS: ${client.users.size} \n CHANNELS: ${client.channels.size} \nSERVERS: ${client.guilds.size}\n`); // log the amount of users, amount of channels, and amount of servers the bot has
	client.user.setActivity('marv.help'); // set the 'playing' to marv.help
})



// -----------------------------------------------------------------------------



client.on(`guildCreate`, guild => { // when the bot joins a server
	console.log(`\n-----------------------------\nNew server joined! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}\n-----------------------------\n`); // log the amout of users and server name
});

client.on(`guildDelete`, guild => { // when the bot leaves a server
	console.log(`\n-----------------------------\nRemoved from server! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}\n-----------------------------\n`); // log the amount of users and server name
});



// -----------------------------------------------------------------------------



client.on(`message`, message => { // when the bot gets a message
	if (message.author.bot) return; // if the message is from a bot, do nothing

	var dm = false; // it isn't a DM by default
	var serverSettings = {
		SCPPrefix: true // the server has the SCP- prefix turned on by default
	};
	var includesSCP = false; // there arent any SCPs or TALEs in the message by default
	var includesCommand = false; // there arent any commands in the message by default
	var splitMessage = message.content.split(" "); // make an array of the message, split by space
	var finalDesc = []; // finalDesc (used for SCPs and TALES) is an array
	var done = false; // done (used for when the SCP- prefix is off) is false

	if (message.guild !== null) { // if the message has a guild (not a DM)
		console.log(`${message.guild.name}  ██  #${message.channel.name}  ██  ${message.author.username}: ${message.content}`); // log the message normally
	}
	else { // else (if the message is a DM)
		dm = true; // dm = true
		console.log(`DM   ██  DM  ██  ${message.author.username}: ${message.content}`); // log it using only a DM instead of the guild name
	}

	let final = new Discord.RichEmbed() // create the richembed (final message)
		.setColor(`#000000`) // make the color black
		.setAuthor(`Marv`, `https://images.discordapp.net/avatars/538173713162567690/07187402dab82f0fd34348a0a5202ecc.png?size=512`, `https://discordapp.com/api/oauth2/authorize?client_id=554490018752626708&permissions=8&scope=bot`); // set the picture, name, and link

	if (dm == false) { // if its not a DM
		try { // try to
			serverSettings = fs.readFileSync(`./settings/${message.guild.name}.json`, (err) => { //read the serversettings
				if (err) throw err; // if an error, say it
			});
			serverSettings = JSON.parse(serverSettings); // parse the settings into a js dictionary
		}
		catch (err) { // if the above gets an error
			serverSettings = {
				SCPPrefix: true // just use the default server settings (prefix = true)
			};
		}
	}

	// -----------------------------------------------------------------------------

	if (message.content.toLowerCase().startsWith("marv.help")) { // if the message starts with marv.help
		includesCommand = true; // the message includes a command
		final.setTitle('__**Here are all of my commands!**__') // set the title of the embed
			.setDescription('*Arguments must be seperated with a comma and space or it will return an error.*') // set the description of the embed
			.addField('General', '```\nhelp\ntoggleprefix\nstats```'); // add a field of all the commands
	}
	else if (message.content.toLowerCase().startsWith("marv.toggleprefix")) { // if the message starts with marv.toggleprefix
		includesCommand = true; // the message includes a command
		if (serverSettings.SCPPrefix == true) { // if the server has the SCP- prefix on
			serverSettings["SCPPrefix"] = false; // turn it off
			final.setTitle('__**The prefix has been turned off!**__') // set the title of the embed
				.setDescription('Marv will now pick up on only numbers, (001) instead of numbers with the prefix (SCP-001).\nTales still require the \'TALE-\' prefix to work.'); // set the description of the embed
		}
		else { // if the server has the SCP- prefix off
			serverSettings.SCPPrefix = true; // turn it on
			final.setTitle('__**The prefix has been turned on!**__') // set the title of the embed
				.setDescription('Marv will now only pick up on numbers with a prefix (SCP-001).'); // set the description of the embed
		}
	}
	else if (message.content.toLowerCase().startsWith("marv.stats")) { // if the message starts with marv.stats
		includesCommand = true; // the message includes a command
		final.setTitle('BOT STATS') // set the title of the embed
			.setDescription(`**Server Count** - ${client.guilds.size}\n**Channel Count** - ${client.channels.size}\n**User Count** - ${client.users.size}`); // set the description of the embed
	}

	// -----------------------------------------------------------------------------
	else { // if there arent any commands
		if (serverSettings.SCPPrefix == true) { // if the SCP- prefix is on
			for (var i = 0; i < splitMessage.length; i++) { // for each word in the message
				if (splitMessage[i].toUpperCase().startsWith("TALE-")) { // if the word starts with TALE-
					finalDesc.push(`[${splitMessage[i].substring(5).split("-").join(" ")}](http://www.scp-wiki.net/${splitMessage[i].substring(5)})`); // add the link to whatever is after TALE-
					includesSCP = true; // the message includes an SCP
				}

				if (splitMessage[i].toUpperCase().startsWith("SCP-")) { // if the word starts with SCP-
					finalDesc.push(`[${splitMessage[i].toUpperCase()}](http://www.scp-wiki.net/${splitMessage[i]})`); // add the link to whatever is after SCP-
					includesSCP = true; // the message includes an SCP
				}
			}
		}
		else { // if the SCP- prefix is off
			for (var i = 0; i < splitMessage.length; i++) { // for each word in the message
				if (splitMessage[i].toUpperCase().startsWith("TALE-")) { // if the word starts with TALE-
					finalDesc.push(`[${splitMessage[i].substring(5).split("-").join(" ")}](http://www.scp-wiki.net/${splitMessage[i].substring(5)})`); // add the link to whatever is after TALE-
					includesSCP = true; // the message includes an SCP
				}
			}

			for (var i = 5000; i >= 0; i--) { // for every number between 1 and 5000
				if (!done) { // if the SCP hasnt already been found
					if (i < 10) { // if the number is less than 10
						i = `00${i}`; // add two zeros (001)
					}
					else if (i < 100) { // if the number is less than 100
						i = `0${i}`; // add one zero (010)
					}

					if (message.content.toUpperCase().includes(`${i}`)) { // if the message includes the number
						finalDesc.push(`[SCP-${i}](http://www.scp-wiki.net/scp-${i})`); // add the link to the SCP
						done = true; // the SCP has been found
						includesSCP = true; // the message includes an SCP
					}
				}
			}
		}
	}

	// -----------------------------------------------------------------------------

	if (includesSCP) { // if the message includes an SCP
		final.setDescription(finalDesc.join("\n")); // set the description of the embed to the array of links spilt by a linebreak
		message.channel.send(final); // send the message
	}
	else if (includesCommand) { // if the message includes a command
		message.channel.send(final); // send the message as it is
	}

	// -----------------------------------------------------------------------------



	if (dm == false) { // if its not a DM
		let JSONObject = JSON.stringify(serverSettings); // turn the serverSettings into a JSON object
		fs.writeFileSync(`./settings/${message.guild.name}.json`, JSONObject, (err) => { // write the serverSettings to the servers JSON file
			if (err) throw err; // if it gets an error, throw it
		});
	}
});



// -----------------------------------------------------------------------------



client.login(process.argv[2]); // login to the bot with whatever argument is put into the console