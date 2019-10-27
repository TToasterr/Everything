const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'adddndchannel',
	description: 'Add a DND channel to the server!',
	usage: '[in Character or out Of Character]',
	category: 'dnd',
	passThrough: true,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		args[0] = args[0].slice(1);

		if (args[0] !== `in Character` && args[0] !== `out Of Character`) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`You didn't use the right arguments!\nPlease use either 'in Character' or 'out Of Character' to set the type of channel.\nThis is case sensitive.`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to add a DND channel to '${guildName}' but didn't use the right kind of arguments.`);
		}

		serverSettings[`DNDChannels`][args[0].split(' ').join('')].push(channelID);

		final.setTitle('__**Channel added!**__')
			.setDescription(`<#${channelID}> has been added to the ${args[0].toLowerCase()} DND channels.`);

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guild.id} Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} added to the ${args[0].toLowerCase()} DND channels for '${guildName}'.`);
	},
};