const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: '',
	description: '',
	usage: '',
	category: '',
	passThrough: false,
	autoExec: false,
	guildOnly: false,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		// final.setTitle('')
		// .setDescription('')
		// .addField('', '');

		// serverSettings = JSON.stringify(serverSettings);
		// fs.writeFileSync(`./servers/${guild.id}Settings.json`, serverSettings, (err) => {
		// 	if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		// });

		// channel.send(final);
		// console.log(`[${time}] ${authorName} did something.`);
	},
};