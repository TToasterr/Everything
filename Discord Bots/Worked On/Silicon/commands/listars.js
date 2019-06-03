const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'listars',
	description: 'List all autoresponders for this server!',
	usage: '',
	category: 'autoresponder',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let object;
		let array = [];

		try {
			object = fs.readFileSync(`./autoresponders/${guild.id}.json`, (err) => {
				if (err) throw err;
			});

			object = JSON.parse(object);
		} catch (err) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`This server doesnt have any autoresponders!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to list autoresponders for ${guildName} but it doesnt have any.`);
		}



		let keys = Object.keys(object);
		for (let key of keys) {
			array.push(`**${key}** - ${object[key]}`);
			// final.addField(`**${key}**`, `${object[key]}`);
		}

		if (object == {} || !object || object == '' || object == '{}' || array == [] || !array || array == '[]' || !array[0]) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`This server doesnt have any autoresponders!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to list autoresponders for ${guildName} but it doesnt have any.`);
		}

		array = array.join('\n');
		if (array.length > 2048) {
			let half1 = array.slice(0, 2047);
			let half2 = array.slice(2047);
			final.setDescription(half1);

			if (half2.length > 1024) {
				let half2half1 = half2.slice(0, 1023);
				let half2half2 = half2.slice(1023);
				final.addField('*(2048 character limit break)*', half2half1)
					.addField('*(2048 character limit break)*', half2half2);
			} else {
				final.addField('*(2048 character limit break)*', half2);
			}
		} else {
			final.setDescription(array);
		}

		final.setTitle(`__**List of all autoresponses:**__`)
		// .setDescription(`*(in ${guildName})*`);
		// .setDescription(array.join('\n'));

		channel.send(final);
		console.log(`[${time}] ${authorName} listed autoresponders for ${guildName}.`);
	},
};