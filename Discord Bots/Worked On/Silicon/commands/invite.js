const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'invite',
	description: 'Invite the bot to your server!',
	usage: '',
	category: 'general',
	passThrough: false,
	autoExec: false,
	guildOnly: false,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		final.setTitle('__**Invite Link**__')
			.setDescription('Open an invite link by clicking my name above!');

		channel.send(final);
		console.log(`[${time}] ${authorName} got an invite link.`);
	},
};