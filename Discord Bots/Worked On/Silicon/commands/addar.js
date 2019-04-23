const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'addar',
	description: 'Add an autoresponse to this server!',
	usage: '[trigger], [response]',
	category: 'autoresponder',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		args[0] = args[0].slice(1);
		let object;

		try {
			object = fs.readFileSync(`./autoresponders/${guildName}.json`, (err) => {
				if (err) throw err;
			});

			object = JSON.parse(object);
			object[args[0]] = args[1];
		}
		catch (err) {
			object = {};
			object[args[0]] = args[1];
		}


		let autoresponses = JSON.stringify(object);
		fs.writeFileSync(`./autoresponders/${guildName}.json`, autoresponses, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s autoresponses file:\n${err}\n`);
		});

		final.setTitle(`__**Autoresponder added!**__`)
			.setDescription(`**Trigger:** ${args[0]}\n**Response:** ${args[1]}`);

		channel.send(final);
		console.log(`[${time}] ${authorName} added an autoresponder to ${guildName}.`);
	},
};