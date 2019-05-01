const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'changeprefix',
	description: 'Change the prefix for the server you\'re on!',
	usage: '[prefix]',
	category: 'general',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		serverPrefix = args[0].slice(1).split(' ')[0];

		final.setTitle('__**Success!**__')
			.setDescription(`Prefix sucessfully changed to ${serverPrefix}`);

		serverSettings['prefix'] = serverPrefix;

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guild.id} Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} changed the prefix of '${guildName}' to '${serverPrefix}'.`);
	},
};