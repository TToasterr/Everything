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
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		let object;
		let array = [];

		try {
			object = fs.readFileSync(`./autoresponders/${guildName}.json`, (err) => {
				if (err) throw err;
			});

			object = JSON.parse(object);
		}
		catch (err) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`This server doesnt have any autoresponders!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to list autoresponders for ${guildName} but it doesnt have any.`);
		}



		let keys = Object.keys(object);
		for (let key of keys) {
			array.push(`**'${key}'** - '${object[key]}'`);
		}

		if (object == {} || !object || object == '' || object == '{}' || array == [] || !array || array == '[]' || !array[0]) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`This server doesnt have any autoresponders!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to list autoresponders for ${guildName} but it doesnt have any.`);
		}

		final.setTitle(`__**List of all autoresponses:**__`)
			.setDescription(`${array.join('\n')}`);

		channel.send(final);
		console.log(`[${time}] ${authorName} listed autoresponders for ${guildName}.`);
	},
};