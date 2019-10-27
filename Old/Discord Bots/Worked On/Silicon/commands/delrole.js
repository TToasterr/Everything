const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'delrole',
	description: 'Delete a role from the server!',
	usage: '[role name]',
	category: 'management',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let roles = message.guild.roles;
		args[0] = args[0].slice(1);

		if (roles.find(role => role.name == args[0])) {
			roles.find(role => role.name == args[0])
				.delete(`${authorName} made me.`)
				.catch(err => {
					final.setTitle(`__**Whoops!**__`)
						.setDescription(`I don't have permission to delete that role!`);
					channel.send(final);
					return console.log(`[${time}] ${authorName} tried to delete the ${args[0]} role from ${guildName} but I didn't have permissions do it.`);
				});
		} else {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`That role doesn't exist!\nMake sure you spelled everything right.`);
			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to delete a role from ${guildName} but didn't use a role that existed.`)
		}

		final.setTitle(`__**Role Deleted!**__`)
			.setDescription(`${authorName} deleted the ${args[0]} role.`);

		channel.send(final);
		console.log(`[${time}] ${authorName} deleted the ${args[0]} role from ${guildName}.`);
	},
};