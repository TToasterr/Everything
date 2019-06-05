const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'listroles',
	description: 'List all roles in the server!',
	usage: '',
	category: 'management',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let roles = message.guild.roles.map(role => role.name);
		let arr = [];

		for (let role of roles) {
			arr.push(role);
		}

		final.setTitle(`__**All roles in ${guildName}:**__`)
			.setDescription(arr.join(`\n`));

		channel.send(final);
		console.log(`[${time}] ${authorName} listed all roles in ${guildName}.`);
	},
};