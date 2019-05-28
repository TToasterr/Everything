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
		thing += `\n**Total Member Count** - ${client.users.size}\n*(The server member counts include bots, while the total member count does not.)*`;

		if (thing.length > 2048) {
			let half1 = thing.slice(0, 2047);
			let half2 = thing.slice(2047);
			final.setDescription(half1);

			if (half2.length > 1024) {
				let half2half1 = half2.slice(0, 1023);
				let half2half2 = half2.slice(1023);
				final.addField('*(2048 character limit break)*', half2half1)
					.addField('*(1024 character limit break)*', half2half2);
			}
			else {
				final.addField('*(2048 character limit break)*', half2);
			}
		}
		else {
			final.setDescription(thing);
		}

		channel.send(final);
		console.log(`[${time}] ${authorName} listed all servers Silicon is in.`);
	},
};