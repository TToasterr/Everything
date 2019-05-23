const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'delar',
	description: 'Remove an autoresponse from this server!',
	usage: '[trigger]',
	category: 'autoresponder',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		args[0] = args[0].slice(1);
		let doesntExist = false;
		let response = '';

		try {
			object = fs.readFileSync(`./autoresponders/${guild.id}.json`, (err) => {
				if (err) throw err;
			});

			object = JSON.parse(object);
			if (object[args[0]]) {
				response = object[args[0]];
				delete object[args[0]];
			}
			else {
				doesntExist = true;
			}
		}
		catch (err) {
			doesntExist = true;
		}


		if (doesntExist) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`This server doesnt have that trigger!`);

			channel.send(final);
			console.log(`[${time}] ${authorName} tried to remove a trigger that doesnt exist from ${guildName}.`);
		}
		else {
			let autoresponses = JSON.stringify(object);
			fs.writeFileSync(`./autoresponders/${guild.id}.json`, autoresponses, (err) => {
				if (err) console.log(`Error writing to '${guildName}'s autoresponses file:\n${err}\n`);
			});

			final.setTitle(`__**Autoresponder removed!**__`)
				.setDescription(`**Trigger:** ${args[0]}\n**Response:** ${response}`);

			channel.send(final);
			console.log(`[${time}] ${authorName} removed an autoresponder from ${guildName}.`);
		}
	},
};