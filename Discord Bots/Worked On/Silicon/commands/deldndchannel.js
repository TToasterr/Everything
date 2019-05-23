const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'deldndchannel',
	description: 'Remove a DND channel from the server!',
	usage: '',
	category: 'dnd',
	passThrough: true,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		if (serverSettings[`DNDChannels`][`outOfCharacter`].includes(channelID)) {
			serverSettings[`DNDChannels`][`outOfCharacter`] = (serverSettings[`DNDChannels`][`outOfCharacter`].join(" ").replace(' ' + channelID, '')).split(" ");
		}
		if (serverSettings[`DNDChannels`][`inCharacter`].includes(channelID)) {
			serverSettings[`DNDChannels`][`inCharacter`] = (serverSettings[`DNDChannels`][`inCharacter`].join(" ").replace(' ' + channelID, '')).split(" ");
		}

		final.setTitle('__**Channel removed!**__')
			.setDescription(`<#${channelID}> has been removed from the ${args[0].toLowerCase()} DND channels.`);

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guild.id} Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} removed from the ${args[0].toLowerCase()} DND channels for '${guildName}'.`);
	},
};