const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'serverlist',
	description: 'List all servers that Silicon is in!',
	usage: '',
	category: 'general',
	passThrough: false,
	autoExec: false,
	guildOnly: false,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		const allGuilds = client.guilds.map(g => g.name);
		const guildMCount = client.guilds.map(g => g.memberCount);
		let thing = '';

		final.setTitle('__**All Servers Silicon is in, and their member counts:**__');

		for (var i = 0; i < allGuilds.length; i++) {
			thing += `**${allGuilds[i]}** - ${guildMCount[i]}\n`;
		}
		thing += `\n**Total Member Count** - ${client.users.size}`;
		final.setDescription(thing);

		channel.send(final);
		console.log(`[${time}] ${authorName} listed all servers Silicon is in.`);
	},
};